
##################### LLAMADA

#def p_llamada(p):
    '''llamada : ID LPAREN llamada2 RPAREN'''
    #'''llamada : ID llamadaSearch LPAREN prepEra llamada2 llamaVer RPAREN llamaEnd
    #            | ID llamadaSearch LPAREN prepEra RPAREN llamaEnd'''    


'''def p_llamadaSearch(p):
    'llamadaSearch : '
    global currFuncID
    if not searchFunc(p[-1]):
        print("Function " + p[-1] + " not defined")
        exit()
    else:
        currFuncID.push(p[-1])
    

def p_prepEra(p):
    'prepEra : empty'
    global tablaFunciones, pilaQuads, currFuncID, pilaParams
    funcID = currFuncID.peek()
    gen = quad('ERA', None, None, searchFuncSize(funcID)) #como definir la size
    pilaQuads.push(gen)
    quadCounter += 1
    #params = getParams(funcID)
    #if len(params) > 1:
    #    pilaParams.push(params)'''

#def p_llamada2(p):
    '''llamada2 : exp COMMA llamada2
                | exp'''
    '''global pilaOpd, pilaTipos, pilaQuads, currFuncID, parameterCounter
    funcID = currFuncID.peek()
    argument = pilaOpd.pop()
    argument_type = pilaTipos.pop()
    params = getParams(funcID)
    if len(p) > 2:
        if params[parameterCounter] != argument_type:
            print("Parameter mismatch")
            exit()
        else:
            arg = 'Argument #' + str(parameterCounter)
            gen = quad('PARAMETER', argument, None, arg)
            pilaQuads.push(gen)
            quadCounter += 1
            parameterCounter += 1
    else:
        if params[0] != argument_type:
            print("Parameter mismatch")
            exit()
        else:
            arg = 'Argument #' + str(1)
            gen = quad('PARAMETER', argument, None, arg)
            pilaQuads.push(gen)
            quadCounter += 1'''

'''def p_llamaVer(p):
    'llamaVer : empty'
    global pilaParams, parameterCounter, currFuncID
    funcID = currFuncID.peek()
    params = getParams(funcID)
    if parameterCounter != len(params) - 1:
        print("Parameter number do not match")
        exit()
    else:
        parameterCounter = 0

def p_llamaEnd(p):
    'llamaEnd : empty'
    global pilaQuads, quadCounter, currFuncID
    funcID = currFuncID.pop()
    gen = quad('GOSUB', funcID, None, getFuncDirection(funcID)) #rellenar 4to con un numero
    quadCounter += 1'''


######################## DESDE
'''def p_addDesde(p):
    'addDesde : empty'
    global pilaQuads, pilaSaltos, quadCounter
    pilaSaltos.push(quadCounter)'''

'''def p_genDesde(p):
    'genDesde : ID EQUAL CTEI HASTA CTEI'
    global pilaQuads, quadCounter, tablaFunciones, tablaTemporalesBool, cteDirections, temporayBoolDirections
    varContador = searchVar(p[1])
    tablaConstantes[cteDirections] = p[3]
    cteDirections += 1
    tablaConstantes[cteDirections] = p[5]
    gen = quad('>', varContador, cteDirections, temporayBoolDirections)
    tablaTemporalesBool[temporayBoolDirections] = 
    cteDirections += 1
    temporayBoolDirections += 1



    global pilaQuads, quadCounter, pilaOpd
    resultType = pilaTipos.pop()
    if resultType != 'bool':
        print("TYPE MISMATCH")
        exit()
    else:
        result = pilaOpd.pop()
        gen = quad('GOTOV', result, None, None)
        pilaSaltos.push(quadCounter-1)'''

'''def p_endDesde(p):
    global pilaQuads, pilaSaltos
    end = pilaSaltos.pop()
    regreso = pilaSaltos.pop()
    gen = quad('GOTO', None, None, regreso)
    pilaQuads.push(gen)
    quadCounter += 1
    pilaQuads.members[quadCounter].fill(quadCounter)'''