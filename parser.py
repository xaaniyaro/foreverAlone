from lexer import tokens
import ply.yacc as yacc
import sys
import operator
import codecs
import collections
import stack
import interpreter
import tNames

tablaFunciones = {}
tablaConstantes = {}
tablaTemporales = {}
tablaTemporalesBool = {}
tablaTemporalesPointer = {}
funcCounter = 1
startFunc = 0
parameterCounter = 1
firstVars = {}
currFuncID = stack.Stack()
currF = ""
pilaOpd = stack.Stack()
pilaTipos = stack.Stack()
pilaOpr = stack.Stack()
pilaQuads = Quadruple()
pilaSaltos = stack.Stack()
pilaParams = stack.Stack()
avail = tNames.tnames()

############### Direcciones virtuales
mainDirections = 5000
secondaryDirections = 8000
cteDirections = 12000
temporayNumDirections = 13000
temporayBoolDirections = 14000
temporaryPointer = 21000

class Quadruple:
    
    def __init__(self):
        items = []
        contador = 1

    def generate(self, label, lOpd, rOpd, result):
        newQuad = [label, lOpd, rOpd, result]
        self.items.append(newQuad)
        contador += 1

    def fill(self, index, content):
        if self.items[index][3] == None:
            self.items[index][3] = content
        else:
            print("Wrong quadruple")

class funcion:
    def __init__(self, name, functype, params, vars, position):
        self.name = name
        self.functype = functype
        self.params = params
        self.vars = vars
        self.position = position

    def getSize(self):
        # Restar la direccion inicial para obtener el numero de variables temporales creadas
        return len(self.vars) + (int(temporayNumDirections) - 13000)  

#returns if a function exists or not
def searchFunc(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return True #existe
    return False #no existe

#returns the size of the function
def searchFuncSize(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return tablaFunciones[i].getSize()

#returns a list with the types of parameters
def getParams(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return tablaFunciones[i].params

def getFuncDirection(funcName):
    global funcCounter, tablaFunciones
    for i in range (1, funcCounter):
        if tablaFunciones[i].name == funcName:
            return tablaFunciones[i].position

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
    global tablaFunciones, currF
    for k in range(1,funcCounter):
        vartype = None
        if tablaFunciones[k].name == currF:
            listOfItems = tablaFunciones[k].vars.items()
            for item  in listOfItems:
                vartype = item[0]
                for element in item[1]:
                    if element[0] == valueToFind:
                        #type, id, value, memDir 
                        return (vartype, element[0],element[1], element[2])
        else:
            listOfItems = tablaFunciones[1].vars.items()
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

def resetDirTemp():
    global temporayBoolDirections, temporayNumDirections, temporaryPointer
    tablaTemporales = {}
    tablaTemporalesBool = {}
    tablaTemporalesPointer = {}
    temporayNumDirections = 13000
    temporayBoolDirections = 14000
    temporaryPointer = 21000

def getKeysByValue(dictOfElements, valueToFind):
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            return (True, item[0])
    return None
    

def addToTable(tableName, varvalue):
    global tablaFunciones, tablaConstantes, tablaTemporales
    global tablaTemporalesBool, tablaTemporalesPointer
    global cteDirections

    if tableName == 'ctes':
        ver = getKeysByValue(tablaConstantes, varvalue)
        if ver != None:
            if ver[0] == True:
                print("Variable ya existe")
                return ver[1]
        else:
            tablaConstantes[cteDirections] = varvalue
            cteDirections += 1
            return cteDirections - 1

    
    
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
    exit()

##### PROGRAMA

def p_programa(p):
    #'programa : PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main'
    'programa : PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main showstacks'

def p_addMain(p):
    'addMain : empty'
    global quadCounter
    pilaSaltos.push(quadCounter)
    gen = quad('GOTO', None, None, None)
    pilaQuads.push(gen)
    quadCounter += 1

def p_createTable(p):
    'createTable : empty'
    global funcCounter
    global tablaFunciones
    global firstVars
    entry = funcion('main', 'void', None, firstVars, None)
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
    global funcCounter, tablaFunciones, secondaryDirections, quadCounter, startFunc
    # nombre, tipo, params, vars, sizeofparms, position
    if p[1] != None:
        newfunc = funcion(p[1][0], p[1][1],p[1][2],p[1][3], startFunc)
        tablaFunciones[funcCounter] = newfunc
        funcCounter = funcCounter + 1
        secondaryDirections = 8000
        registerReturnFunc(p[1][0], p[1][1])

def p_func_decl(p):
    '''func_decl : FUNCION func2 func3 LPAREN params RPAREN vars bloque endFunc'''
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

def p_func3(p):
    'func3 : ID'
    global currF, quadCounter, startFunc
    currF = p[1]
    startFunc = quadCounter
    p[0] = p[1]

def p_func2(p):
    '''func2 : tipo
            | VOID'''
    p[0] = p[1]

def p_endFunc(p):
    'endFunc : empty'
    global pilaQuads, quadCounter
    gen = quad('ENDFUNC',None,None,None)
    pilaQuads.push(gen)
    quadCounter += 1
    resetDirTemp()


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
                | llamada SEMICOLON
                | repeticion'''

##### ASIG *_*

def p_asig(p):
    'asig : variable addAsig exp genAsig SEMICOLON'

def p_addAsig(p):
    'addAsig : EQUAL'
    global pilaOpr
    pilaOpr.push(p[1])

def p_genAsig(p):
    'genAsig : '
    global pilaOpd, pilaTipos, pilaOpr, quadCounter, pilaQuads
    if pilaOpr.peek() == '=':
        opd = pilaOpd.pop()
        opd_type = pilaTipos.pop()
        operator = pilaOpr.pop()
        cvar = p[-3]
        if interpreter.operations[operator][(opd_type,cvar[0])] != 'err':
            gen = quad(operator, opd, None, cvar[3])
            pilaQuads.push(gen)
            quadCounter += 1

'''def regAsig(p):
    'regAsig :'
    global pilaQuads, quadCounter, pilaOpd
    opd = pilaOpd.pop()
    opd_type = pilaTipos.pop()
    var = p[1]
    if interpreter.operations['='][(opd_type,var[0])] != 'err':
        gen = quad('=', opd, None, var[3])
        pilaQuads.push(gen)
        quadCounter += 1
        #print(quadCounter)'''

##### MAIN

def p_main(p):
    #'main : PRINCIPAL LPAREN RPAREN fillFirst bloque'
    'main : printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque'

def p_fillFirst(p):
    'fillFirst : empty'
    global pilaSaltos, quadCounter, currF
    currF = 'main'
    #pilaQuads.items[0].fill(quadCounter)
    #print("PRIMER CUADRUPLO")
    #print("1: " + str(hola.label))
    #print("2: " + str(hola.leftOperand))
    #print("3: " + str(hola.rightOperand))
    #print("4: " + str(hola.result))
    #pilaQuads.items[0].fill()

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


###### RETORNO :S

def p_retorno(p):
    'retorno : REGRESA LPAREN exp RPAREN SEMICOLON'
    global pilaQuads, quadCounter
    gen = quad('RETURN', None, None, p[3]) #handle llamada
    pilaQuads.push(gen)
    quadCounter += 1


###### LLAMADA

def p_llamada(p):
    '''llamada : iniciaLlamada llamada2 endLlamada RPAREN
                | iniciaLlamada endLlamada RPAREN'''
    #generar cuadruplo ERA fact
    #resover exp y guardar cuadruplos
    #llamada2 que se encargue de generar los cuadruplos de params
    #cuando se hayan generado todos los params gen GOSUB
    #asignar a variable del mismo nombre el resultado
    #guardar en temporal este resultado para recursividad

def p_iniciaLlamada(p):
    '''iniciaLlamada : ID LPAREN'''
    global pilaQuads, quadCounter, parameterCounter
    #print(p[1])
    #print(searchFuncSize(p[1]))
    gen = quad('ERA',None,None,p[1]) #pendiente introducir esto
    pilaQuads.push(gen)
    quadCounter += 1
    p[0] = p[1]

def p_llamada2(p):
    '''llamada2 : exp COMMA llamada2
                | exp'''
    global pilaQuads, quadCounter, parameterCounter, pilaOpd
    paramName = 'par' + str(parameterCounter)
    result = pilaOpd.pop()
    gen = quad('PARAM', result, None, paramName)
    pilaQuads.push(gen)
    quadCounter += 1
    parameterCounter += 1

def p_endLlamada(p):
    'endLlamada : '
    global pilaQuads, quadCounter, parameterCounter
    position = getFuncDirection(p[-2])
    if position != None:
        print("La funcion tiene posicion")
        gen = quad('GOSUB', p[-2], None, position)
        pilaQuads.push(gen)
    else:
        print("Tomando el start de la funcion")
        gen = quad('GOSUB', p[-2], None, startFunc)
        pilaQuads.push(gen)
    parameterCounter = 1
    quadCounter += 1

##### LECTURA

def p_lectura(p):
    'lectura : LEE LPAREN variable RPAREN SEMICOLON'
    global pilaQuads, quadCounter
    gen = quad('INPUT', None, None, p[3][3])
    pilaQuads.push(gen)
    quadCounter += 1

##### ESCRITURA

def p_escritura(p):
    'escritura : ESCRIBE LPAREN escritura1 escritura2 RPAREN SEMICOLON'

def p_escritura1(p):
    '''escritura1 : CTES
                | exp'''
    p[0] = p[1]

def p_escritura2_a(p):
    '''escritura2 : COMMA escritura1 escritura2
                | escritura1'''
    global pilaQuads, quadCounter
    if len(p) > 2:
        gen = quad('PRINT', None, None, p[2])
        pilaQuads.push(gen)
        quadCounter += 1
    else:
        gen = quad('PRINT', None, None, p[1])
        pilaQuads.push(gen)
        quadCounter += 1

##### CONDICION

def p_cond(p):
    'cond : SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2'

def p_cond1(p):
    'cond1 : empty'
    global pilaTipos, pilaOpd, pilaSaltos, quadCounter
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("ERROR: Type mismatch")
    else:
        result = pilaOpd.pop()
        gen = quad('GOTOF',result,None,None)
        pilaQuads.push(gen)
        pilaSaltos.push(quadCounter-1)
        quadCounter += 1

def p_cond2(p):
    'cond2 : empty'
    global pilaSaltos, quadCounter
    end = pilaSaltos.pop()
    #pilaQuads.items[end].fill(quadCounter)

def p_elsePart(p):
    '''elsePart : SINO elseActions bloque
                | empty'''  

def p_elseActions(p):
    'elseActions : empty'
    global pilaQuads, quadCounter
    gen = quad('GOTO', None,None,None)
    pilaQuads.push(gen)
    quadCounter += 1
    false = pilaSaltos.pop()
    pilaSaltos.push(quadCounter-1)
    #pilaQuads.items[false-1].fill(quadCounter)

##### REPETICION

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''

###### CONDICIONAL

def p_condicional(p):
    'condicional : MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhile'

def p_regWhile(p):
    'regWhile : empty'
    global pilaSaltos, quadCounter
    pilaSaltos.push(quadCounter)

def p_whileCond(p):
    'whileCond : empty'
    global pilaTipos, pilaOpd, pilaQuads, pilaSaltos, quadCounter
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("TYPE MISTACH")
    else:
        result = pilaOpd.pop()
        gen = quad('GOTOF', result, None, None)
        pilaSaltos.push(quadCounter-1)
        pilaQuads.push(gen)
        quadCounter += 1

def p_endWhile(p):
    'endWhile : empty'
    global pilaSaltos, quadCounter, pilaQuads
    end = pilaSaltos.pop()
    regresa = pilaSaltos.pop()
    gen = quad('GOTO',None, None, regresa)
    pilaQuads.push(gen)
    quadCounter += 1
    #pilaQuads.members[end].fill(quadCounter)

###### NOCONDICIONAL

def p_nocondicional(p):
    '''nocondicional : DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endFor'''

def p_createFor(p):
    'createFor : '
    global temporayNumDirections, tablaTemporales, tablaConstantes, cteDirections
    global temporayBoolDirections, quadCounter, pilaSaltos

    vartuple = searchVar(p[-5])
    varEnd = addToTable('ctes', p[-3])
    gen = quad('=', varEnd, None, vartuple[3])
    pilaQuads.push(gen)
    quadCounter += 1
    varIni = addToTable('ctes', p[-1])
    pilaSaltos.push(quadCounter)
    gen = quad('<', vartuple[3], varIni, temporayBoolDirections)
    pilaQuads.push(gen)
    quadCounter += 1
    gen = quad('GOTOV', temporayBoolDirections, None, None)
    pilaQuads.push(gen)
    quadCounter += 1
    temporayBoolDirections += 1

def p_endFor(p):
    'endFor : '
    global pilaQuads, quadCounter, pilaSaltos, tablaConstantes, temporayNumDirections
    vartuple = searchVar(p[-8])
    
    print(tablaConstantes)
    
    #onevar = getKeysByValue(tablaConstantes,'1')
    #print(onevar)
    #gen = quad('+', vartuple[3], onevar, temporayNumDirections)
    #pilaQuads.push(gen)
    #quadCounter += 1
    
    #gen = ('=', temporayNumDirections, None, vartuple[3])
    #pilaQuads.push(gen)
    #quadCounter += 1
    #temporayNumDirections += 1

    start = pilaSaltos.pop()
    gen = quad('GOTO', None, None, start)
    pilaQuads.push(gen)
    quadCounter += 1
    #print("Contador vale ->")
    #print(quadCounter)
    #print("Size de la quadPila ->")
    #print(len(pilaQuads.items))
    pilaQuads.items[start+1].fill('Por rellenar')

##### EXP

def p_exp(p):
    'exp : texp exp1'
    global pilaOpr, temporayBoolDirections, pilaQuads, tablaTemporalesBool
    if pilaOpr.items != []:
        if pilaOpr.peek() == '|':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporalesBool[temporayBoolDirections] = avail.next()
                temporayBoolDirections = temporayBoolDirections + 1
                quadObj = quad(operator, lOpd, rOpd, temporayBoolDirections)
                pilaQuads.push(quadObj)
                pilaOpd.push(temporayBoolDirections)
                pilaTipos.push(resultType)
                '''if lOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(lOpd)
                    temporayBoolDirections =- 1
                if rOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(rOpd)
                    temporayBoolDirections =- 1'''
            else:
                print("TYPE MISMATCH")
                exit()

def p_exp1(p):
    '''exp1 : OR texp exp1
            | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 

###### TEXP

def p_texp(p):
    'texp : gexp texp1'
    global pilaOpr, temporayBoolDirections, pilaQuads, tablaTemporalesBool
    if pilaOpr.items != []:
        if pilaOpr.peek() == '&':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporalesBool[temporayBoolDirections] = avail.next()
                temporayBoolDirections = temporayBoolDirections + 1
                quadObj = quad(operator, lOpd, rOpd, temporayBoolDirections)
                pilaQuads.push(quadObj)
                pilaOpd.push(temporayBoolDirections)
                pilaTipos.push(resultType)
                '''if lOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(lOpd)
                    temporayBoolDirections =- 1
                if rOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(rOpd)
                    temporayBoolDirections =- 1'''
            else:
                print("TYPE MISMATCH")
                exit()

def p_texp1(p):
    '''texp1 : AND gexp texp1
             | empty'''
    global pilaOpr
    if len(p) > 2:
        pilaOpr.push(p[1]) 

###### GEXP

def p_gexp(p):
    'gexp : mexp gexp1'
    global pilaOpr, temporayBoolDirections, pilaQuads, tablaTemporalesBool
    if pilaOpr.items != []:
        logic = ['>','<','>=','<=','==', '!=']
        if pilaOpr.peek() in logic:
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporalesBool[temporayBoolDirections] = avail.next()
                temporayBoolDirections = temporayBoolDirections + 1
                quadObj = quad(operator, lOpd, rOpd, temporayBoolDirections)
                pilaQuads.push(quadObj)
                pilaOpd.push(temporayBoolDirections)
                pilaTipos.push(resultType)
                '''if lOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(lOpd)
                    temporayBoolDirections =- 1
                if rOpd > 13999 and lOpd < 14999:
                    tablaTemporalesBool.pop(rOpd)
                    temporayBoolDirections =- 1'''
            else:
                print("TYPE MISMATCH")
                exit()

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
    global pilaOpr, temporayNumDirections, pilaQuads, tablaTemporales, pilaOpd
    global pilaTipos, quadCounter
    if pilaOpr.items != []:
        if pilaOpr.peek() == '+' or pilaOpr.peek() == '-':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporales[temporayNumDirections] = avail.next()
                temporayNumDirections = temporayNumDirections + 1
                quadObj = quad(operator, lOpd, rOpd, temporayNumDirections)
                pilaQuads.push(quadObj)
                quadCounter += 1
                pilaOpd.push(temporayNumDirections)
                pilaTipos.push(resultType)
                '''if lOpd > 12999 and lOpd < 13999:
                    tablaTemporales.pop(lOpd)
                    temporayNumDirections =- 1
                if rOpd > 12999 and rOpd < 13999:
                    tablaTemporales.pop(rOpd)
                    temporayNumDirections =- 1'''
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
    global pilaOpr, temporayNumDirections, pilaQuads, tablaTemporales, pilaTipos, pilaOpd
    global quadCounter
    if pilaOpr.items != []:
        if pilaOpr.peek() == '*' or pilaOpr.peek() == '/':
            rOpd = pilaOpd.pop()
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporales[temporayNumDirections] = avail.next()
                temporayNumDirections = temporayNumDirections + 1
                quadObj = quad(operator, lOpd, rOpd, temporayNumDirections)
                pilaQuads.push(quadObj)
                quadCounter += 1
                pilaOpd.push(temporayNumDirections)
                pilaTipos.push(resultType)
                '''if lOpd > 12999 and lOpd < 13999:
                    tablaTemporales.pop(lOpd)
                    temporayNumDirections =- 1
                if rOpd > 12999 and rOpd < 13999:
                    tablaTemporales.pop(rOpd)
                    temporayNumDirections =- 1'''
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
    global pilaOpd, pilaQuads, pilaTipos, cteDirections, tablaConstantes
    if len(p) < 3:   
        if isinstance(p[1],(int)):
            reg = addToTable('ctes', p[1])
            #tablaConstantes[cteDirections] = p[1]
            pilaOpd.push(reg)
            #cteDirections += 1
            pilaTipos.push('int')
            p[0] = pilaOpd.peek()
        elif isinstance(p[1],(float)):
            reg = addToTable('ctes', p[1])
            #tablaConstantes[cteDirections] = p[1]
            pilaOpd.push(reg)
            #cteDirections += 1
            pilaTipos.push('float')
            p[0] = pilaOpd.peek()
        elif type(p[1]) is tuple:
            pilaOpd.push(p[1][3])
            p[0] = pilaOpd.peek()
            pilaTipos.push(p[1][0])
        else:
            print("Haciendo una llamada")
            # TO-DO: handle when a 'llamada' es registrada'''
    else:
        #cuando se encuentra un parentesis
        p[0] = p[2]
    

###### VARIABLE

def p_variable(p):
    'variable : ID dimension'
    # varTuple -> (vartype, varname, value, memDir)
    varTuple = searchVar(p[1])
    p[0] = varTuple

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

def p_showstacks(p):
    'showstacks : empty'
    global pilaOpd, pilaOpr, pilaTipos
    
    print("Pila quads")
    while pilaQuads.is_empty() != True:
        print("Cuadruplo #" + str(len(pilaQuads.items)) + ": " )
        curr = pilaQuads.pop()
        print("1: " + str(curr.label))
        print("2: " + str(curr.leftOperand))
        print("3: " + str(curr.rightOperand))
        print("4: " + str(curr.result))

    #print("Pila operadores")
    #while pilaOpr.is_empty() != True:
    #    print(pilaOpr.pop())
        
    #print("Pila tipos")
    #while pilaTipos.is_empty() != True:
    #    print(pilaTipos.pop())

def p_printfuncs(p):
    'printfuncs : empty'
    printFuncTable()

parser = yacc.yacc()

parser.parse(cadena)