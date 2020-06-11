import re
import ast

# Simulacion de maquina virtual
# Utiliza un diccionario para llevar un registro de las variables
# Lee el archivo de texto generado por el parser 
######## EN PROCESO #########
#Se puede utilizar el archivo de prueba adjunto, pero genera un ciclo infinito
#Se requiere mas tiempo para revisar como se esta comportando el contador
# que es el que se encarga de romper el ciclo
#se deben combinar todas las tablas generadas en el parser

#dicc = {'5000': 'fact', '12000': 1, '12001': 9, '13000': 'i', '13001': 't2', '13002': 't3','14000': 't1'}
#dicc = {5000: 'fact', 12000: 1, 12001: 9, 13000: 'i', 13001: 't2', 13002: 't3', 14000: 't1'}
quads = []
temp = {}

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b

def readquadfile():
    global quads
    f = open("output.txt", "r")
    for x in f:
        splitted = x.split()
        quads.append(splitted)

def readtempsfile():
    global temp
    f = open("temps.txt", "r")
    curr = ""
    for x in f:
        z = re.match("\w",x)
        if z:
            x = x.rstrip()
            temp[x] = {}
            curr = x
        else:
            newd = ast.literal_eval(x)
            strdicc = {}
            for j in newd:
                strdicc[str(j)] = newd[j]
            del newd
            temp[curr].update(strdicc)
            del strdicc

def readvarfile():
    global temp
    f = open("vars.txt", "r")
    curr = ""
    for x in f:
        x = x.split()
        #print(x)
        if len(x) > 1:
            #print("Registrando var")
            #regresa un dicc
            old = temp[curr]
            #crea un nuevo registro en el dicc
            old[x[0]] = x[1]
            #curr es la key nombre de la funcion
            #igualar al nuevo dicc con el viejo y nuevo content
            temp[curr] = old 
        else:
            #print("Cambiando curr")
            curr = x[0]
    globalvars = {}
    maincontent = temp['main']
    for i in maincontent:
        if int(i) > 4999 and int(i) < 5999:
            globalvars[i] = maincontent[i]
    for j in temp:
        temp[j].update(globalvars)
    #print(temp)



def readctes():
    global temp
    ctes = {}
    f = open("ctes.txt", "r")
    for x in f:
        x = x.split()
        if isint(x[1]):
            ctes[x[0]] = int(x[1])
        elif isfloat(x[1]):
            ctes[x[0]] = float(x[1])
        else:
            ctes[x[0]] = x[1]
    f.close()
    for i in temp:
        old = temp[i]
        old.update(ctes)
        temp[i] = old
    #print(temp)

def runcode():
    #Leyendo archivo y guardando en una lista de listas
    global quads, temp
    readquadfile()
    readtempsfile()
    readvarfile()
    readctes()
    #print(temp)
    dicc = temp['main']
    currF = ""
    i = 0
    regresa = 0
    while(1):
        if quads[i][0] == '+':
            print("sumando")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) + int(dicc[quads[i][2]])
        elif quads[i][0] == '-':
            print("restando")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) - int(dicc[quads[i][2]])
        elif quads[i][0] == '*':
            print("multiplicando {} por {}".format(dicc[quads[i][1]], dicc[quads[i][2]]))
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) * int(dicc[quads[i][2]])
        elif quads[i][0] == '/':
            print("dividiendo")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) / int(dicc[quads[i][2]])
        elif quads[i][0] == '=':
            print("asignando")
            print(quads[i][3])
            print(dicc[quads[i][1]])
            dicc[quads[i][3]] = dicc[quads[i][1]]
        elif quads[i][0] == '>':
            #print("comparando dir {} dir {} {} con {}".format(quads[i][1],quads[i][2]),dicc[quads[i][1]],dicc[quads[i][2]])
            dicc[quads[i][3]] = dicc[quads[i][1]] > dicc[quads[i][2]]
            #print("El resultado fue {}".format(dicc[quads[i][3]]))
        elif quads[i][0] == '<':
            dicc[quads[i][3]] = dicc[quads[i][1]] < dicc[quads[i][2]]
        elif quads[i][0] == '>=':
            dicc[quads[i][3]] = dicc[quads[i][1]] >= dicc[quads[i][2]]
        elif quads[i][0] == '<=':
            dicc[quads[i][3]] = dicc[quads[i][1]] <= dicc[quads[i][2]]
        elif quads[i][0] == '==':
            dicc[quads[i][3]] = dicc[quads[i][1]] == dicc[quads[i][2]]
        elif quads[i][0] == '!=':
            dicc[quads[i][3]] = dicc[quads[i][1]] != dicc[quads[i][2]]
        elif quads[i][0] == '|':
            dicc[quads[i][3]] = dicc[quads[i][1]] or dicc[quads[i][2]]
        elif quads[i][0] == '&':
            dicc[quads[i][3]] = dicc[quads[i][1]] and dicc[quads[i][2]]
        elif quads[i][0] == 'ENDFUNC':
            print("Final de funcion")
            i = regresa
            print(dicc)
            for j in dicc:
                if j in temp['main']:
                    temp['main'][j] = dicc[j]
            dicc = temp['main']
            #print("El contador ahora vale {}".format(i))
        elif quads[i][0] == 'ERA':
            currF = quads[i][3]
            #print("Se requieren {} espacios de memoria".format(len(dicc)-1))
        elif quads[i][0] == 'PARAM':
            value = dicc[quads[i][1]]
            word = quads[i][3]
            filtered = re.findall('\d+', word)
            for j in filtered:
                direction = str(int(j) + 7999)
            if direction in temp[currF]:
                temp[currF][direction] = value
        elif quads[i][0] == 'GOTO':
            #print("Llendo al cuadruplo {}".format(int(quads[i][3])))
            i = int(quads[i][3]) - 1
            continue
        elif quads[i][0] == 'GOTOV':
            if dicc[quads[i][1]]:
                print("i vale {}".format(i))
                i = int(quads[i][3]) - 2
                print("saltando al cuadruplo {}".format(i))
            else:
                print("se sigue el curso")
        elif quads[i][0] == 'GOTOF':
            if not dicc[quads[i][1]]:
                #print("i vale {}".format(i))
                i = int(quads[i][3]) - 2
                #print("saltando al cuadruplo {}".format(i))
            else:
                print("se sigue el curso")
        elif quads[i][0] == 'GOSUB':
            print(temp)
            toupdate = temp[quads[i][1]]
            for j in dicc:
                if j in toupdate:
                    toupdate[j] = dicc[j]
            dicc = toupdate
            #print("Llendo al cuadruplo {}".format(int(quads[i][3])))
            regresa = i
            #print("Se tiene que regresar al cuadruplo {}".format(regresa))
            i = int(quads[i][3]) - 1
            continue
        elif quads[i][0] == 'PRINT':
            print(dicc[quads[i][3]])
        elif quads[i][0] == 'INPUT':
            lee = input("leyendo...")
            dicc[quads[i][3]] = lee
            
        if i == len(quads) - 1:
            break
        i += 1
        #print("Contador: {}".format(i))

runcode()