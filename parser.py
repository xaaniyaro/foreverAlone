from lexer import tokens
import ply.yacc as yacc
import sys
import operator
import codecs
import collections
import stack
import interpreter

tablaFunciones = {}         #diccionario de funciones
funcCounter = 1             #contador de funciones
firstVars = []              #lista para primeras variables
pilaOpd = stack.Stack()     #pila de operandos
pilaTipos = stack.Stack()   #pila de tipos
pilaOpr = stack.Stack()     #pila de operadores
tempResult = 0              #contador de cuadruplos
pilaQuads = stack.Stack()   #pila de cuadruplos
pilaSaltos = stack.Stack()  #pila de saltos
currFuncID = stack.Stack()
parameterCounter = 1
pilaParams = stack.Stack()
semanticCube = interpreter.operations

class quad:
    def __init__(self, label, leftOperand, rightOperand, result):
        self.label = label
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.result = result
    
    def fill(self, content):
        if self.result == None:
            self.result = content
        else:
            print("Hubo un problema rellenando un cuadruplo con etiqueta: " + self.label)

class funcion:
    def __init__(self, name, functype, params, vars):
        self.name = name
        self.functype = functype
        self.params = params
        self.vars = vars

def searchFunc(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return True
    return False

def getParams(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return tablaFunciones[i].params

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

def searchVar(varname):
    global tablaFunciones
    global funcCounter
    for k in range(1,funcCounter):
        vartype = None
        for i in tablaFunciones[k].vars:
            vartype = i[0]
            for j in i[1]:
                if j[0] == varname:
                    return (varname, vartype, j[1])

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
    #'programa : PROGRAMA ID SEMICOLON vars createTable func_declarations main'
    'programa : PROGRAMA ID SEMICOLON vars createTable func_declarations main showstacks'

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
        firstVars = p[2]
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
    if len(p) == 2:
        p[0] = (p[1], None, None)
    else:
        p[0] = (p[1], None, p[3])

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
    global funcCounter
    global tablaFunciones
    if p[1] != None:
        newfunc = funcion(p[1][0], p[1][1],p[1][2],p[1][3])
        tablaFunciones[funcCounter] = newfunc
        funcCounter = funcCounter + 1
    

def p_func_decl(p):
    '''func_decl : FUNCION func2 ID LPAREN params RPAREN vars bloque'''
    if bool(checkDuplicateFuncs(p[3])):
        exit()
    else:
        p[0] = (p[3], p[2], p[5], p[7])
    

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

#changed this 

def p_estatuto(p):
    '''estatuto : asig
                | cond
                | retorno
                | lectura
                | escritura
                | llamada SEMICOLON
                | repeticion'''

##### ASIG

def p_asig(p):
    'asig : variable EQUAL exp SEMICOLON'
    global pilaQuads, tempResult, pilaOpd
    opd = pilaOpd.pop()
    opd_type = pilaTipos.pop()
    var = p[1] #revisar que regresa 'variable', si se puede obtener el tipo
    if interpreter.operations['='][(opd_type,var)] != 'err':
        gen = quad('=',opd, None, var)
        pilaQuads.push(gen)

##### MAIN

def p_main(p):
    'main : PRINCIPAL LPAREN RPAREN bloque'
    #'main : printfuncs PRINCIPAL LPAREN RPAREN bloque'

##### PARAMS

def p_param_decl(p):
    'param_decl : tipo ID'
    p[0] = (p[1], None, p[2])

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
    global pilaQuads, tempResult
    gen = quad('RETURN',None,None,p[3])
    #tempResult += 1

###### LLAMADA

def p_llamada(p):
    '''llamada : llamadaSearch LPAREN prepEra llamada2 llamaVer RPAREN llamaEnd
                | llamadaSearch LPAREN prepEra RPAREN llamaEnd'''    

def p_llamadaSearch(p):
    ' llamadaSearch : ID'
    if not searchFunc(p[1]):
        print("Function" + p[1] + "not defined")
        exit()
    else:
        currFuncID.push(p[1])

def p_prepEra(p):
    'prepEra : empty'
    global tablaFunciones, pilaQuads, currFuncID, pilaParams
    funcID = currFuncID.peek()
    gen = quad('ERA', None, None, funcID) #como definir la size
    pilaQuads.push(gen)
    tempResult += 1
    params = getParams(funcID)
    if len(params) > 1:
        pilaParams.push(params)

def p_llamada2(p):
    '''llamada2 : exp COMMA llamada2
                | exp'''
    global pilaOpd, pilaTipos, pilaQuads
    if len(p) > 2:
        argument = pilaOpd.pop()
        argument_type = pilaTipos.pop()
         #checar esto, sigue siendo confuso
        if pilaParams.peek()[parameterCounter][0] != argument_type:
            print("Parameter error")
            exit()
        else:
            arg = 'Argument #' + str(parameterCounter)
            gen = quad('PARAMETER', argument, None, arg)
            pilaQuads.push(gen)
            tempResult += 1
            parameterCounter += 1
    else:
        currP = pilaParams.pop()
        if len(currP) != 1:
            print("Parameter error with size")
            exit()
        else:
            arg = 'Argument #' + str(1)
            gen = quad('PARAMETER', argument, None, arg)
            pilaQuads.push(gen)
            tempResult += 1

def p_llamaVer(p):
    'llamaVer : empty'
    global pilaParams, parameterCounter
    currP = pilaParams.pop()
    if parameterCounter != len(currP):
        print("Parameter number do not match")
        exit()
    else:
        parameterCounter = 1

def p_llamaEnd(p):
    'llamaEnd: empty'
    global pilaQuads, tempResult, currFuncID
    gen = quad('GOSUB',currFuncID.pop(),None,'initialAdress') #rellenar 4to con un numero
    tempResult += 1

##### LECTURA

def p_lectura(p):
    'lectura : LEE LPAREN variable RPAREN SEMICOLON'
    global pilaQuads, tempResult
    gen = quad('INPUT', None, None, p[3]) #revisar que revisa 'variable'
    pilaQuads.push(gen)
    tempResult += 1

##### ESCRITURA

def p_escritura(p):
    'escritura : ESCRIBE LPAREN escritura1 escritura2 RPAREN SEMICOLON'

def p_escritura1(p):
    '''escritura1 : CTES
                | exp'''
    p[0] = p[1] #revisar que regresa exp

def p_escritura2_a(p):
    '''escritura2 : COMMA escritura1 escritura2
                | escritura1'''
    global pilaQuads, tempResult
    if len(p) > 4:
        gen = quad('PRINT', None, None, p[2])
        pilaQuads.push(gen)
        #tempResult += 1


##### CONDICION

def p_cond(p):
    'cond : SI LPAREN exp RPAREN cond1 ENTONCES bloque condicion1 cond2'

def p_cond1(p):
    'cond1 : empty'
    global pilaTipos, pilaOpd, pilaSaltos, tempResult
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("ERROR: Type mismatch")
    else:
        result = pilaOpd.pop()
        gen = quad('GOTOF',result,None,None)
        pilaQuads.push(gen)
        tempResult += 1
        pilaSaltos.push(tempResult-1)

def p_cond2(p):
    'cond2 : empty'
    global pilaSaltos, tempResult
    end = pilaSaltos.pop()
    pilaQuads.members[end].fill(tempResult)

def p_condicion1(p):
    '''condicion1 : elseActions SINO bloque
                | empty'''  

def p_elseActions(p):
    'elseActions : empty'
    global pilaQuads, tempResult
    gen = quad('GOTO', None,None,None)
    pilaQuads.push(gen)
    tempResult += 1
    false = pilaSaltos.pop()
    pilaSaltos.push(tempResult-1)
    pilaQuads.members[false].fill(tempResult)

##### REPETICION

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''

###### CONDICIONAL

def p_condicional(p):
    'condicional : MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhile'

def p_regWhile(p):
    'regWhile : empty'
    global pilaSaltos, tempResult
    pilaSaltos.push(tempResult)

def p_whileCond(p):
    'whileCond : empty'
    global pilaTipos, pilaOpd, pilaQuads, pilaSaltos, tempResult
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("TYPE MISTACH")
    else:
        result = pilaOpd.pop()
        gen = quad('GOTOF', result, None, None)
        pilaQuads.push(gen)
        tempResult += 1
        pilaSaltos.push(tempResult-1)

def p_endWhile(p):
    'endWhile: empty'
    global pilaSaltos, tempResult, pilaQuads
    end = pilaSaltos.pop()
    regresa = pilaSaltos.pop()
    gen = quad('GOTO',None, None, regresa)
    pilaQuads.members[end].fill(tempResult)
    pilaQuads.push(gen)
    tempResult += 1

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
    global pilaOpr, pilaOpd, tempResult, pilaTipos, tempResult, pilaQuads
    if pilaOpr.items != []:
        if pilaOpr.peek() == '+' or pilaOpr.peek() == '-':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            #print((lType, rType, resultType))
            if(resultType != 'err'):
                tempResult = tempResult + 1
                quadObj = quad(operator, lOpd, rOpd, tempResult)
                pilaQuads.push(quadObj)
                pilaOpd.push(tempResult)
                pilaTipos.push(resultType)
                #if isinstance(lOpd, (int)) or isinstance(rOpd, (int)):
                #    tempResult = tempResult - 1
            else:
                print("TYPE MISMATCH")
                exit()


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
    global pilaOpr, pilaOpd, tempResult, pilaTipos, tempResult, pilaQuads
    if pilaOpr.items != []:
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
                #if isinstance(lOpd, (int)) or isinstance(rOpd, (int)):
                #    tempResult = tempResult - 1
            else:
                print("TYPE MISMATCH")
                exit()

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
    if len(p) < 3:   
        if isinstance(p[1],(int)):
            pilaOpd.push(p[1])
            pilaTipos.push('int')
        elif isinstance(p[1],(float)):
            pilaOpd.push(p[1])
            pilaTipos.push('float')
        else:
            #varTuple = (varname, vartype, varvalue)
            varTuple = searchVar(p[1])
            if varTuple != None:
                pilaOpd.push(varTuple[0])
                pilaTipos.push(varTuple[1])
            # TO-DO: handle when a 'llamada' es registrada
    

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

#Para mostrar lo que se ha guardado en los stacks al correrse todo el parser
 
def p_showstacks(p):
    'showstacks : empty'
    global pilaQuads
    print("Pila quads")
    while pilaQuads.is_empty() != True:
        q = pilaQuads.pop()
        print((q.operator,q.leftOperand,q.rightOperand,q.result))
    '''
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




#def p_printfuncs(p):
#    'printfuncs : empty'
#    printFuncTable()

parser = yacc.yacc()

parser.parse(cadena)