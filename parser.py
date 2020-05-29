from lexer import tokens
import ply.yacc as yacc
import sys
import operator
import codecs
import collections
import stack
import interpreter

tablaFunciones = {}
funcCounter = 1
firstVars = {}
pilaOpd = stack.Stack()
pilaTipos = stack.Stack()
pilaOpr = stack.Stack()
tempResult = 0
pilaQuads = stack.Stack()

#Direcciones virtuales
mainDirections = 5000
secondaryDirections = 8000
cteDirections = 12000
temporayNumDirections = 13000
temporayBoolDirections = 14000
#temporaryPointer = 21000

class quad:
    def __init__(self, operator, leftOperand, rightOperand, result):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.result = result

class funcion:
    def __init__(self, name, functype, params, vars):
        self.name = name
        self.functype = functype
        self.params = params
        self.vars = vars

def checkDuplicateVars(varList):
    flag = False
    val = collections.Counter(varList) 
    uniqueList = list(set(varList))
      
    for i in uniqueList: 
        if val[i]>= 2: 
            flag = True
            print("Error de declaracion")
            return 1
              
    if flag == False: 
        return 0 

def checkDuplicateFuncs(funcName):
    global tablaFunciones
    global funcCounter
    for i in range(2, funcCounter):
        if tablaFunciones[i].name == funcName:
            print("Error de declaracion de funcion")
            return 1
        else:
            return 0

def printFuncTable():
    global funcCounter
    global tablaFunciones
    for i in range(1, funcCounter):
        print("Func",i,"------")
        print(tablaFunciones[i].name)
        print(tablaFunciones[i].functype)
        print(tablaFunciones[i].params)
        print(tablaFunciones[i].vars)

def searchVar(valueToFind):
    global tablaFunciones
    global funcCounter
    for k in range(1,funcCounter):
        vartype = None
        listOfItems = tablaFunciones[k].vars.items()
        for item  in listOfItems:
            vartype = item[0]
            for element in item[1]:
                if element[0] == valueToFind:
                    #type, id, value, memDir 
                    return (vartype, element[0],element[1], element[2])

def registerReturnFunc(funcId, funcT):
    global tablaFunciones, mainDirections
    vartype = None
    dicc = tablaFunciones[1].vars
    content = dicc[funcT]
    newVar = (funcId, None, mainDirections)
    content.append(newVar)
    tablaFunciones[1].vars[funcT] = content
    mainDirections += 1

##################### Parsing rules

#Para definir el archivo que contiene el programa
filename = "test.txt"

#Para leer el contenido del archivo
fp = codecs.open(filename,"r","utf-8")
cadena = fp.read()
fp.close()

#Para evitar conflictos en la gramatica
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    )

start = 'programa'

def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

##### PROGRAMA

def p_programa(p):
    'programa : PROGRAMA ID SEMICOLON vars createTable func_declarations main'
    #'programa : PROGRAMA ID SEMICOLON vars createTable func_declarations main showstacks'

def p_createTable(p):
    'createTable : empty'
    global funcCounter
    global tablaFunciones
    global firstVars
    entry = funcion('global', 'void', None, firstVars)
    tablaFunciones[funcCounter] = entry
    funcCounter = funcCounter + 1

##### VARS

def p_vars(p):
    '''vars : VAR var2
            | empty'''
    global funcCounter
    global firstVars
    if funcCounter == 1:
        dicc = {}
        for i in p[2]:
            if i[0] in dicc.keys():
                past = dicc[i[0]]
                past = past + i[1]
                dicc[i[0]] = past
            else:
                dicc[i[0]] = i[1]
        firstVars = dicc
    p[0] = p[2]

def p_var1(p):
    'var1 : tipo lista_ids SEMICOLON'
    p[0] = (p[1], p[2])

def p_var2(p):
    '''var2 : var1 var2
            | var1'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[2]
        p[0].append(p[1])

##### LISTA_IDS

def p_var_decl(p):
    ''' var_decl :  ID
                |   ID LBRACKET CTEI RBRACKET
                |   ID LBRACKET exp RBRACKET'''
    #Var definition (id, value, memDir, array)
    global mainDirections, secondaryDirections, funcCounter
    if len(p) == 2:
        if funcCounter == 1:
            p[0] = (p[1], None, mainDirections)
            mainDirections += 1
        else:
            p[0] = (p[1], None, secondaryDirections)
            secondaryDirections += 1
    else:
        if funcCounter == 1:
            if isinstance(p[3], int):
                p[0] = (p[1], None, mainDirections)
                mainDirections += p[3]
            else:
                print("LIST SIZE ERROR")
                exit()
        else:
            if isinstance(p[3], int):
                p[0] = (p[1], None, secondaryDirections)
                secondaryDirections += p[3]
            else:
                print("LIST SIZE ERROR")
                exit()

def p_lista_ids(p):
    '''lista_ids : lista_ids COMMA var_decl
                | var_decl '''
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        if bool(checkDuplicateVars([p[1]])):
            exit()
        else: 
            p[0] = [p[1]]
    

##### TIPO

def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | CHAR'''
    p[0] = p[1]

##### FUNC

def p_func_declarations(p):
    '''func_declarations : func_decl func_declarations
                        | empty'''
    global funcCounter, tablaFunciones, secondaryDirections
    # nombre, tipo, params, vars
    if p[1] != None:
        newfunc = funcion(p[1][0], p[1][1],p[1][2],p[1][3])
        tablaFunciones[funcCounter] = newfunc
        funcCounter = funcCounter + 1
        secondaryDirections = 8000
        registerReturnFunc(p[1][0], p[1][1])

def p_func_decl(p):
    '''func_decl : FUNCION func2 ID LPAREN params RPAREN vars bloque'''
    global secondaryDirections
    if bool(checkDuplicateFuncs(p[3])):
        exit()
    else:
        dicc = {}
        updateList = []
        for i in p[7]:
            dicc[i[0]] = i[1]
        for i in p[5]:
            currID = i[1]
            currType = i[0]
            for key in dicc:
                if key == currType:
                    dicc[key].append((currID, None, secondaryDirections)) 
            updateList.append(currType)
        #nombre, tipo, params, vars
        p[0] = (p[3], p[2], updateList, dicc)
    

def p_func2(p):
    '''func2 : tipo
            | VOID'''
    p[0] = p[1]

##### BLOQUE

def p_bloque(p):
    '''bloque : LCURLY bloque1 RCURLY'''

def p_bloque1(p):
    '''bloque1 : estatuto bloque1
                | empty'''

##### ESTATUTO

def p_estatuto(p):
    '''estatuto : asig
                | cond
                | retorno
                | lectura
                | escritura
                | llamada
                | repeticion'''

##### ASIG

def p_asig(p):
    'asig : variable EQUAL exp SEMICOLON'

##### MAIN

def p_main(p):
    #'main : PRINCIPAL LPAREN RPAREN bloque'
    'main : printfuncs PRINCIPAL LPAREN RPAREN bloque'

##### PARAMS

def p_param_decl(p):
    'param_decl : tipo ID'
    p[0] = (p[1], p[2])

def p_params(p):
    '''params : params COMMA param_decl
                | param_decl'''
    if len(p) > 2 :
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]
    #print(p[0])


###### RETORNO

def p_retorno(p):
    'retorno : REGRESA LPAREN exp RPAREN SEMICOLON'

###### LLAMADA

def p_llamada(p):
    '''llamada : ID LPAREN exp llamada2 RPAREN llama'''

def p_llamada2(p):
    '''llamada2 : COMMA exp llamada2
                | empty'''

def p_llama(p):
    '''llama : SEMICOLON
            | empty'''

##### LECTURA

def p_lectura(p):
    'lectura : LEE LPAREN variable RPAREN SEMICOLON'

##### ESCRITURA

def p_escritura(p):
    'escritura : ESCRIBE LPAREN escritura1 escritura2 RPAREN SEMICOLON'

def p_escritura1(p):
    '''escritura1 : CTES
                | exp'''

def p_escritura2_a(p):
    '''escritura2 : COMMA escritura1 escritura2
                | empty'''


##### CONDICION

def p_cond(p):
    'cond : SI LPAREN exp RPAREN ENTONCES bloque condicion1'

def p_condicion1(p):
    '''condicion1 : SINO bloque
                | empty'''

##### REPETICION

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''

###### CONDICIONAL

def p_condicional(p):
    'condicional : MIENTRAS LPAREN exp RPAREN HAZ bloque'

###### NOCONDICIONAL

def p_nocondicional(p):
    '''nocondicional : DESDE ID dimension EQUAL CTEI HASTA CTEI HACER bloque
                    | DESDE ID EQUAL CTEI HASTA CTEI HACER bloque'''

##### EXP

def p_exp(p):
    'exp : texp exp1'

def p_exp1(p):
    '''exp1 : OR texp exp1
            | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 

###### TEXP

def p_texp(p):
    'texp : gexp texp1'

def p_texp1(p):
    '''texp1 : AND gexp texp1
             | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 

###### GEXP

def p_gexp(p):
    'gexp : mexp gexp1'

def p_gexp1(p):
    '''gexp1 : gexp2 mexp gexp1
             | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 

def p_exp2(p):
    '''gexp2 : LESS
            | LESSO
            | GREATER
            | GREATERO
            | NOTEQUAL
            | EQUALS'''
    p[0] = p[1]

####### MEXP

def p_mexp(p):
    'mexp : termino mexp1'
    global pilaOpr, tempResult, pilaQuads
    '''if pilaOpr.items != []:
        if pilaOpr.peek() == '+' or pilaOpr.peek() == '-':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tempResult = tempResult + 1
                quadObj = quad(operator, lOpd, rOpd, tempResult)
                pilaQuads.push(quadObj)
                pilaOpd.push(tempResult)
                pilaTipos.push(resultType)
                if isinstance(lOpd, (int)) or isinstance(rOpd, (int)):
                    tempResult = tempResult - 1
            else:
                print("TYPE MISMATCH")
                exit()'''


def p_mexp1(p):
    '''mexp1 : mexp2 termino mexp1
             | empty'''
    global pilaOpr
    if len(p) > 2:
            pilaOpr.push(p[1]) 

def p_mexp2(p):
    '''mexp2 : PLUS
            | MINUS'''
    p[0] = p[1]

##### TERMINO

def p_termino(p):
    'termino : factor termino1'
    global pilaOpr, tempResult, pilaQuads
    '''if pilaOpr.items != []:
        if pilaOpr.peek() == '*' or pilaOpr.peek() == '/':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tempResult = tempResult + 1
                quadObj = quad(operator, lOpd, rOpd, tempResult)
                pilaQuads.push(quadObj)
                pilaOpd.push(tempResult)
                pilaTipos.push(resultType)
                if isinstance(lOpd, (int)) or isinstance(rOpd, (int)):
                    tempResult = tempResult - 1
            else:
                print("TYPE MISMATCH")
                exit()'''

def p_termino1(p):
    '''termino1 : TIMES factor termino1
                | DIVIDE factor termino1
                | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 
        
###### FACTOR

def p_factor(p):
    '''factor : LPAREN exp RPAREN
                | varcte
                | variable
                | llamada'''
    global pilaOpd
    global pilaTipos
    '''if len(p) < 3:   
        if isinstance(p[1],(int)):
            pilaOpd.push(p[1])
            pilaTipos.push('int')
        elif isinstance(p[1],(float)):
            pilaOpd.push(p[1])
            pilaTipos.push('float')
        else:
            #varTuple = (vartype, varname, value, memDir)
            varTuple = searchVar(p[1])
            if varTuple != None:
                pilaOpd.push(varTuple[0])
                pilaTipos.push(varTuple[1])
            # TO-DO: handle when a 'llamada' es registrada'''
    

###### VARIABLE

def p_variable(p):
    'variable : ID dimension'
    p[0] = p[1]

#### DIMENSION

def p_dimension(p):
    '''dimension : LBRACKET exp RBRACKET
                | empty'''

##### VARCTE

def p_varcte(p):
    '''varcte :  CTEI
                | CTEF
                | CTEC '''
    p[0] = p[1]

'''def p_showstacks(p):
    'showstacks : empty'
    global pilaOpd, pilaOpr, pilaTipos
    
    print("Pila operandos")
    while pilaOpd.is_empty() != True:
        print(pilaOpd.pop())

    print("Pila operadores")
    while pilaOpr.is_empty() != True:
        print(pilaOpr.pop())
        
    print("Pila tipos")
    while pilaTipos.is_empty() != True:
        print(pilaTipos.pop())'''

def p_printfuncs(p):
    'printfuncs : empty'
    printFuncTable()

parser = yacc.yacc()

parser.parse(cadena)