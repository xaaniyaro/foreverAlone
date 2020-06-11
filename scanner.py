from lexer import tokens
import ply.yacc as yacc
import sys
import operator
import codecs
import collections
import stack
import interpreter
import tNames
import quadruple
#from vm import runcode

# Modulo del parser, incluye todas las funciones necesarias para buscar, identificar y registrar variables y funciones
# Parsea el programa que se le provea de input
# Escribe un archivo con los cuadruplos resultantes
# No funciona correctamente aun, existe un problema con los cuadruplos de asignacion y la pila de saltos no registra correctamente

strucTemp = {}
tablaFunciones = {}
tablaConstantes = {}
tablaTemporales = {}
tablaTemporalesBool = {}
tablaFinal = {}
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
pilaQuads = quadruple.Quadruple([],1)
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

def driver(file_data):
    parser = yacc.yacc()
    parser.parse(file_data)

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

def addFunc(fname, ftype, fparams, fvars, fpos):
    global funcCounter, tablaFunciones, secondaryDirections
    newfunc = funcion(fname, ftype, fparams, fvars, fpos)
    tablaFunciones[funcCounter] = newfunc
    funcCounter = funcCounter + 1
    secondaryDirections = 8000  
    if ftype != 'void':
        registerReturnFunc(fname, ftype)


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
    for k in range(2,funcCounter):
        vartype = None
        if tablaFunciones[k].name == currF:
            listOfItems = tablaFunciones[k].vars.items()
            for item  in listOfItems:
                vartype = item[0]
                for element in item[1]:
                    if element[0] == valueToFind:
                        #type, id, size, memDir 
                        return (vartype, element[0],element[1], element[2])
    listOfItems = tablaFunciones[1].vars.items()
    for item in listOfItems:
        vartype = item[0]
        for element in item[1]:
            if element[0] == valueToFind:
                #type, id, size, memDir 
                return (vartype, element[0],element[1], element[2])
    return None

def registerReturnFunc(funcId, funcT):
    global tablaFunciones, mainDirections
    vartype = None
    dicc = tablaFunciones[1].vars
    if funcT in dicc:
        content = dicc[funcT]
        newVar = (funcId, None, mainDirections)
        content.append(newVar)
        tablaFunciones[1].vars[funcT] = content
    else: 
        newVar = (funcId, None, mainDirections)
        dicc[funcT] = []
        dicc[funcT].append(newVar)
        tablaFunciones[1].vars[funcT] = dicc
    mainDirections += 1

def resetDirTemp():
    global temporayBoolDirections, temporayNumDirections, temporaryPointer, strucTemp, currF
    global tablaTemporales, tablaTemporalesBool, tablaTemporalesPointer
    concentrado = {}
    concentrado.update(tablaTemporales)
    concentrado.update(tablaTemporalesBool)
    concentrado.update(tablaTemporalesPointer)
    strucTemp[currF] = concentrado
    tablaTemporales = {}
    tablaTemporalesBool = {}
    tablaTemporalesPointer = {}
    temporayNumDirections = 13000
    temporayBoolDirections = 14000
    temporaryPointer = 21000
    avail.reset()

def getKeysByValue(dictOfElements, valueToFind):
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            return (True, item[0])
    return None
    
def exportVars():
    global funcCounter, tablaFunciones
    newDicc = {}
    
    f= open("vars.txt","w+")
    for i in range(1,funcCounter):
        f.write('{}\n'.format(tablaFunciones[i].name))
        curr = tablaFunciones[i].vars.items()
        for j in curr:
            for k in j[1]:
                f.write('{} {}\n'.format(k[2], k[0]))
    f.close()

def exportCtes():
    f = open("ctes.txt","w+")
    global tablaConstantes
    f= open("ctes.txt","w+")
    for i in tablaConstantes:
        f.write('{} {}\n'.format(i, tablaConstantes[i]))
    f.close()

def addToTable(tableName, varvalue):
    global tablaFunciones, tablaConstantes, tablaTemporales
    global tablaTemporalesBool, tablaTemporalesPointer
    global cteDirections, temporayNumDirections, temporayBoolDirections

    if tableName == 'ctes':
        ver = getKeysByValue(tablaConstantes, varvalue)
        if ver != None:
            if ver[0] == True:
                print("Variable ya existe")
                return ver[1] #regresa la dirV de la variable
        else:
            print("Agregando a tabla")
            tablaConstantes[cteDirections] = varvalue
            cteDirections += 1
            return cteDirections - 1
    
    elif tableName == 'num':
        ver = getKeysByValue(tablaTemporales, varvalue)
        if ver != None:
            if ver[0] == True:
                #print("Variable ya existe")
                return ver[1] #regresa la dirV de la variable
        else:
            tablaTemporales[temporayNumDirections] = varvalue
            temporayNumDirections
            return temporayNumDirections

    elif tableName == 'bool':
        ver = getKeysByValue(tablaTemporalesBool, varvalue)
        if ver != None:
            if ver[0] == True:
                #print("Variable ya existe")
                return ver[1] #regresa la dirV de la variable
        else:
            tablaTemporalesBool[temporayBoolDirections] = varvalue
            temporayBoolDirections += 1
            return temporayBoolDirections - 1

def writeTemps():
    global strucTemp
    f= open("temps.txt","w+")
    for i in strucTemp:
        f.write('{}\n'.format(i))
        f.write('{}\n'.format(strucTemp[i]))
    f.close()
    #f = open("")
    
##################### Parsing rules

#Para definir el archivo que contiene el programa
#filename = "test.txt"

#Para leer el contenido del archivo
#fp = codecs.open(filename,"r","utf-8")
#cadena = fp.read()
#fp.close()

#Para evitar conflictos en la gramatica
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right', 'EQUALS'),
    ('left', 'AND', 'OR'),
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
    global pilaQuads
    pilaSaltos.push(pilaQuads.contador)
    #print(pilaQuads.contador)
    pilaQuads.generate('GOTO', None, None, None)

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
    '''vars : VAR var2'''
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
                p[0] = (p[1], p[3], mainDirections)
                mainDirections += p[3]
            else:
                print("LIST SIZE ERROR")
                exit()
        else:
            if isinstance(p[3], int):
                p[0] = (p[1], p[3], secondaryDirections)
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
    '''func_declarations : func_decl funcBody func_declarations
                        | empty'''

def p_func_decl(p):
    '''func_decl : FUNCION func2 func3 LPAREN params RPAREN vars
                 | FUNCION func2 func3 LPAREN RPAREN vars
                 | FUNCION func2 func3 LPAREN params RPAREN 
                 | FUNCION func2 func3 LPAREN RPAREN'''
    global secondaryDirections, startFunc
    if bool(checkDuplicateFuncs(p[3])):
        exit()
    else:
        if len(p) > 7:
            dicc = {}
            updateList = []
            for i in p[7]: #extracting vars, es un array de tuplas
                dicc[i[0]] = i[1]
            for i in p[5]:
                currID = i[1]
                currType = i[0]
                for key in dicc:
                    if key == currType:
                        dicc[key].append((currID, None, secondaryDirections)) 
                updateList.append(currType)
            # nombre, tipo, params, vars, sizeofparms, position
            addFunc(p[3], p[2], updateList, dicc, startFunc)
        elif len(p) > 6:
            #print(p[4],p[5],p[6],p[7])
            #when no vars but params
            if p[5] != ')':
                dicc = {}
                #dicc['int'] = []
                updateList = []
                for i in p[5]:
                    #print(i)
                    currID = i[1]
                    currType = i[0]
                    if currType in dicc:
                        dicc[currType].append((currID, None, secondaryDirections))
                    else:
                        dicc[currType] = []
                        dicc[currType].append((currID, None, secondaryDirections))
                    
                    secondaryDirections += 1
                    updateList.append(currType)
                addFunc(p[3], p[2], updateList, dicc, startFunc)
            #when no params but vars
            elif p[6] != ')':
                dicc = {}
                for i in p[6]: #extracting vars, es un array de tuplas
                    dicc[i[0]] = i[1]
                addFunc(p[3], p[2], [], dicc, startFunc)
        else:
            #when no params and no vars
            addFunc(p[3], p[2], [], {}, startFunc)
            
def p_funcBody(p):
    'funcBody : bloque endFunc'

def p_func3(p):
    'func3 : ID'
    global currF, pilaQuads, startFunc
    currF = p[1]
    startFunc = pilaQuads.contador
    p[0] = p[1]

def p_func2(p):
    '''func2 : tipo
            | VOID'''
    p[0] = p[1]

def p_endFunc(p):
    'endFunc : empty'
    global pilaQuads
    pilaQuads.generate('ENDFUNC',None,None,None)
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
    'asig : variable addVar EQUAL addAsig exp genAsig SEMICOLON'

def p_addVar(p):
    'addVar : '
    global pilaOpd, pilaTipos
    currVar = p[-1]
    #print(currVar)
    #print(currVar)
    print("Agregando una asignacion {}".format(currVar))
    pilaOpd.push(currVar[3])
    pilaTipos.push(currVar[0])

def p_addAsig(p):
    'addAsig : '
    global pilaOpr
    pilaOpr.push(p[-1])

def p_genAsig(p):
    'genAsig : '
    global pilaOpd, pilaTipos, pilaOpr, pilaQuads
    if pilaOpr.peek() == '=':
        #print("Generando asignacion")
        oper = pilaOpr.pop()
        rOpd = pilaOpd.pop()
        rType = pilaTipos.pop()
        if interpreter.operations[oper][(p[-5][0], rType)] != 'err':
            pilaQuads.generate(oper, rOpd, None, p[-5][3])
        else:
            print("TYPE MISMATCH")
            exit()

##### MAIN

def p_main(p):
    'main : printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque mergetables'
    #'main : printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque'

def p_fillFirst(p):
    'fillFirst : empty'
    global pilaSaltos, currF
    currF = 'main'
    pilaQuads.fill(0,pilaQuads.contador)
    #print(pilaQuads.contador)
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
    global pilaQuads, pilaOpd
    result = pilaOpd.pop()
    pilaQuads.generate('RETURN', None, None, result) #handle llamada


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
    global pilaQuads, parameterCounter, pilaOpd, pilaTipos, temporayNumDirections
    getVar = searchVar(p[1])
    if getVar != None:
        tablaTemporales[temporayNumDirections] = avail.next()
        pilaQuads.generate('=', getVar[3], None, temporayNumDirections)
        pilaOpd.push(temporayNumDirections)
        temporayNumDirections += 1
        p[0] = getVar

def p_iniciaLlamada(p):
    '''iniciaLlamada : ID LPAREN'''
    global pilaQuads, parameterCounter, currF
    #print(p[1])
    #print(searchFuncSize(p[1]))
    if currF == p[1]:
        pilaQuads.generate('ERA',None,None,p[1]) #pendiente introducir esto
        p[0] = p[1]
    elif searchFunc(p[1]):
        pilaQuads.generate('ERA',None,None,p[1]) #pendiente introducir esto
        p[0] = p[1]
    else:
        print("Function {} not defined".format(p[1]))
        exit()

def p_llamada2(p):
    '''llamada2 : exp COMMA llamada2
                | exp'''
    global pilaQuads, parameterCounter, pilaOpd
    paramName = 'par' + str(parameterCounter)
    result = pilaOpd.pop()
    pilaQuads.generate('PARAM', result, None, paramName)
    parameterCounter += 1

def p_endLlamada(p):
    'endLlamada : '
    global pilaQuads, parameterCounter, pilaOpd, pilaTipos, temporayNumDirections
    if len(p) > 4:
        position = getFuncDirection(p[-2])
        if position != None:
            #print("La funcion tiene posicion")
            pilaQuads.generate('GOSUB', p[-2], None, position)
        else:
            #print("Tomando el start de la funcion")
            pilaQuads.generate('GOSUB', p[-2], None, startFunc)
        parameterCounter = 1
    else:
        position = getFuncDirection(p[-1])
        if position != None:
            #print("La funcion tiene posicion")
            pilaQuads.generate('GOSUB', p[-1], None, position)
        else:
            #print("Tomando el start de la funcion")
            pilaQuads.generate('GOSUB', p[-1], None, startFunc)
        parameterCounter = 1
        

##### LECTURA

def p_lectura(p):
    'lectura : LEE LPAREN variable RPAREN SEMICOLON'
    global pilaQuads, pilaQuads
    pilaQuads.generate('INPUT', None, None, p[3][3])

##### ESCRITURA

def p_escritura(p):
    'escritura : ESCRIBE LPAREN escritura2 RPAREN SEMICOLON'

def p_escritura1(p):
    '''escritura1 : CTES
                | exp'''
    p[0] = p[1]

def p_escritura2_a(p):
    '''escritura2 : escritura1 addescritura COMMA escritura2
                    | escritura1 addescritura'''

def p_addescritura(p):
    ' addescritura : '
    global pilaQuads, pilaOpd
    if pilaOpd.is_empty():
        vardir = addToTable('ctes',p[-1])
        pilaQuads.generate('PRINT', None, None, vardir)
    else:
        vardir = pilaOpd.pop()
        pilaQuads.generate('PRINT', None, None, vardir)

##### CONDICION

def p_cond(p):
    'cond : SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2'

def p_cond1(p):
    'cond1 : empty'
    global pilaTipos, pilaOpd, pilaSaltos, pilaQuads
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("ERROR: Type mismatch")
    else:
        result = pilaOpd.pop()
        pilaQuads.generate('GOTOF',result,None,None)
        pilaSaltos.push(pilaQuads.contador - 1)
        #print(pilaQuads.contador)

def p_cond2(p):
    'cond2 : empty'
    global pilaSaltos
    end = pilaSaltos.pop()
    pilaQuads.fill(end - 1, pilaQuads.contador)

def p_elsePart(p):
    '''elsePart : SINO elseActions bloque
                | empty'''  

def p_elseActions(p):
    'elseActions : empty'
    global pilaQuads
    pilaQuads.generate('GOTO', None,None,None)
    false = pilaSaltos.pop()
    pilaSaltos.push(pilaQuads.contador - 1)
    #print(pilaQuads.contador)
    pilaQuads.fill(false - 1, pilaQuads.contador)
    #print(tablaConstantes)
    #print(tablaTemporales)
    #print(tablaTemporalesBool)

##### REPETICION

def p_repeticion(p):
    '''repeticion : condicional
                | nocondicional'''


###### CONDICIONAL

def p_condicional(p):
    'condicional : MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhile'

def p_regWhile(p):
    'regWhile : empty'
    global pilaSaltos, pilaQuads
    pilaSaltos.push(pilaQuads.contador)
    #print(pilaQuads.contador)

def p_whileCond(p):
    'whileCond : empty'
    global pilaTipos, pilaOpd, pilaQuads, pilaSaltos
    exp_type = pilaTipos.pop()
    if exp_type != 'bool':
        print("TYPE MISTACH")
    else:
        result = pilaOpd.pop()
        pilaQuads.generate('GOTOF', result, None, None)
        pilaSaltos.push(pilaQuads.contador)
        #print(pilaQuads.contador)

def p_endWhile(p):
    'endWhile : empty'
    global pilaSaltos, pilaQuads
    end = pilaSaltos.pop()
    regresa = pilaSaltos.pop()
    pilaQuads.generate('GOTO',None, None, regresa)
    pilaQuads.fill(end, pilaQuads.contador)

###### NOCONDICIONAL

def p_nocondicional(p):
    '''nocondicional : DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endFor'''

def p_createFor(p):
    'createFor : '
    global temporayNumDirections, tablaTemporales, tablaConstantes, cteDirections
    global temporayBoolDirections, pilaSaltos
    print("Makin a for")
    #vartuple = searchVar(p[-5])
    basevar = addToTable('num', p[-5])
    varEnd = addToTable('ctes', p[-3])
    pilaQuads.generate('=', varEnd, None, basevar)
    varIni = addToTable('ctes', p[-1])
    pilaSaltos.push(pilaQuads.contador)
    #print(pilaQuads.contador)
    varbool = addToTable('bool', avail.next())
    pilaQuads.generate('<', basevar, varIni, varbool)
    pilaQuads.generate('GOTOV', varbool, None, None)

def p_endFor(p):
    'endFor : '
    global pilaQuads, pilaSaltos, tablaConstantes, temporayNumDirections
    #print(p[-8])
    #vartuple = searchVar(p[-8])
    vardir = addToTable('num',p[-8])
    #print("Imprimiendo tupla de variable")
    #print(vartuple)
    
    onedir = getKeysByValue(tablaConstantes,1)
    #print("Imprimiendo direccion de 1: {}".format(onedir))
    temporayNumDirections += 1
    tablaTemporales[temporayNumDirections] = avail.next()
    pilaQuads.generate('+', vardir-1, onedir[1], temporayNumDirections)
    pilaQuads.generate('=', temporayNumDirections, None, vardir-1)
    


    start = pilaSaltos.pop()
    pilaQuads.generate('GOTO', None, None, start)
    #print("Contador vale ->")
    #print(pilaQuads.contador)
    #print("Size de la quadPila ->")
    #print(len(pilaQuads.items))
    pilaQuads.fill(start, pilaQuads.contador)

    #print(tablaConstantes)
    #print(tablaTemporales)
    #print(tablaTemporalesBool)

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
                pilaQuads.generate(operator, lOpd, rOpd, temporayBoolDirections)
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
                pilaQuads.generate(operator, lOpd, rOpd, temporayBoolDirections)
                pilaOpd.push(temporayBoolDirections)
                temporayBoolDirections = temporayBoolDirections + 1
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
                pilaQuads.generate(operator, lOpd, rOpd, temporayBoolDirections)
                pilaOpd.push(temporayBoolDirections)
                temporayBoolDirections = temporayBoolDirections + 1
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

def p_gexp2(p):
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
    global pilaOpr, temporayNumDirections, pilaQuads, tablaTemporales, pilaOpd, pilaTipos
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
                pilaQuads.generate(operator, lOpd, rOpd, temporayNumDirections)
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
    global pilaOpr, temporayNumDirections, pilaQuads, tablaTemporales, pilaTipos, pilaOpd, pilaOpr
    if pilaOpr.items != []:
        if pilaOpr.peek() == '*' or pilaOpr.peek() == '/':
            rOpd = pilaOpd.pop()
            #print("Operador derecho: {}".format(rOpd))
            rType = pilaTipos.pop()
            lOpd = pilaOpd.pop()
            #print("Operador izquierdo: {}".format(lOpd))
            lType = pilaTipos.pop()
            operator = pilaOpr.pop()
            resultType = interpreter.operations[operator][(lType,rType)]
            if(resultType != 'err'):
                tablaTemporales[temporayNumDirections] = avail.next()
                temporayNumDirections = temporayNumDirections + 1
                pilaQuads.generate(operator, lOpd, rOpd, temporayNumDirections)
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
            #p[0] = pilaOpd.peek()
        elif isinstance(p[1],(float)):
            reg = addToTable('ctes', p[1])
            #tablaConstantes[cteDirections] = p[1]
            pilaOpd.push(reg)
            #cteDirections += 1
            pilaTipos.push('float')
            #p[0] = pilaOpd.peek()
        elif type(p[1]) is tuple:
            pilaOpd.push(p[1][3])
            #p[0] = pilaOpd.peek()
            pilaTipos.push(p[1][0])
            print(pilaOpd.items)
            #print("Haciendo una llamada")
            # TO-DO: handle when a 'llamada' es registrada'''
        #else:

    

###### VARIABLE

def p_variable(p):
    'variable : ID'
    # varTuple -> (vartype, varname, value, memDir)
    varTuple = searchVar(p[1])
    #print(p[1])
    if varTuple == None:
        tempVar = getKeysByValue(tablaTemporales,p[1])
        if tempVar == None:
            print("Variable not found {}".format(p[1]))
            exit()
        else:
            p[0] = ('int', p[1], None, tempVar[1])
    else:
        p[0] = varTuple

'''def p_variable(p):
    variable : ID
                | ID dimension
    # varTuple -> (vartype, varname, size, memDir)
    global pilaQuads, temporayNumDirections, temporaryPointer, tablaTemporales
    if len(p) > 2:
        varTuple = searchVar(p[1])
        #print(varTuple)
        onedir = addToTable('ctes', 1)
        secondir = addToTable('ctes', varTuple[2],)
        currsize = addToTable('ctes',p[2])
        pilaQuads.generate('VER', currsize, onedir, secondir)
        pilaQuads.generate('-', currsize, onedir, temporayNumDirections)
        tablaTemporales[temporayNumDirections] = avail.next()
        startdir = addToTable('ctes', varTuple[3])
        pilaQuads.generate('+', temporayNumDirections, startdir, temporaryPointer)
        tablaTemporalesPointer[temporaryPointer] = avail.next()
        temporaryPointer += 1
        temporayNumDirections += 1
        p[0] = (varTuple[0], varTuple[1], varTuple[2], temporaryPointer-1)

    else:
        varTuple = searchVar(p[1])
        #print(p[1])
        if varTuple == None:
            tempVar = getKeysByValue(tablaTemporales,p[1])
            if tempVar == None:
                print("Variable not found {}".format(p[1]))
                exit()
            else:
                p[0] = ('int', p[1], None, tempVar[1])
        else:
            p[0] = varTuple'''
        

#### DIMENSION

#def p_dimension(p):
    #'''dimension : LBRACKET exp RBRACKET'''
    #global pilaOpd
    #p[0] = pilaOpd.pop()

##### VARCTE

def p_varcte(p):
    '''varcte :  CTEI
                | CTEF
                | CTEC '''
    p[0] = p[1]

def p_mergetables(p):
    'mergetables : empty'
    exportVars()
    resetDirTemp()
    #print("Dicc de variables {}".format(exporta))
    writeTemps()
    exportCtes()
    
    '''dicckeys = dicc.keys()
    values = dicc.values()
    array = []
    for i in dicckeys:
        array.append(str(i))

    del dicckeys
    del dicc

    dicc = dict(zip(array, values))
    print(dicc)
    del array
    del values'''
    #runcode(dicc)


def p_showstacks(p):
    'showstacks : empty'
    global pilaOpd, pilaOpr, pilaTipos, pilaQuads
    f= open("output.txt","w+")
    quadList = pilaQuads.items
    quadList.reverse()
    while len(quadList) > 0:
        curr = quadList.pop()
        f.write('{} {} {} {}\n'.format(curr[0], curr[1], curr[2], curr[3]))
    f.close()

    #print("Pila operadores")
    #while pilaOpr.is_empty() != True:
    #    print(pilaOpr.pop())
        
    #print("Pila tipos")
    #while pilaTipos.is_empty() != True:
    #    print(pilaTipos.pop())

def p_printfuncs(p):
    'printfuncs : empty'
    printFuncTable()
