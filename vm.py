
# Simulacion de maquina virtual
# Utiliza un diccionario para llevar un registro de las variables
# Lee el archivo de texto generado por el parser 
######## EN PROCESO #########
#Se puede utilizar el archivo de prueba adjunto, pero genera un ciclo infinito
#Se requiere mas tiempo para revisar como se esta comportando el contador
# que es el que se encarga de romper el ciclo
#se deben combinar todas las tablas generadas en el parser

#dicc = {'5000': 'fact', '12000': 1, '12001': 9, '13000': 'i', '13001': 't2', '13002': 't3','14000': 't1'}
#dicc = {5000: 'fact', 12000: 1, 12001: 9, 13000: 'i', 13001: 't2', 13002: 't3',14000: 't1'}

def runcode(dicc):
    #Leyendo archivo y guardando en una lista de listas
    f = open("correct.txt", "r")
    quads = []
    for x in f:
        splitted = x.split()
        quads.append(splitted)

    i = 0
    regresa = 0

    while(1):
        if quads[i][0] == '+':
            #print("sumando")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) + int(dicc[quads[i][2]])
        elif quads[i][0] == '-':
            #print("restando")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) - int(dicc[quads[i][2]])
        elif quads[i][0] == '*':
            #print("multiplicando")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) * int(dicc[quads[i][2]])
        elif quads[i][0] == '/':
            #print("dividiendo")
            dicc[quads[i][3]] = int(dicc[quads[i][1]]) / int(dicc[quads[i][2]])
        elif quads[i][0] == '=':
            #print("asignando")
            #print(quads[i][3])
            #print(dicc[quads[i][1]])
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
            #print("Final de funcion")
            i = regresa
            #print("El contador ahora vale {}".format(i))
        elif quads[i][0] == 'ERA':
            pass
            #print("Se requieren {} espacios de memoria".format(len(dicc)-1))
        elif quads[i][0] == 'GOTO':
            #print("Llendo al cuadruplo {}".format(int(quads[i][3])))
            i = int(quads[i][3]) - 1
            continue
        elif quads[i][0] == 'GOTOV':
            if dicc[quads[i][1]]:
                #print("i vale {}".format(i))
                i = int(quads[i][3]) - 2
                #print("saltando al cuadruplo {}".format(i))
            #else:
                #print("se sigue el curso")
        elif quads[i][0] == 'GOTOF':
            if not dicc[quads[i][1]]:
                #print("i vale {}".format(i))
                i = int(quads[i][3]) - 2
                #print("saltando al cuadruplo {}".format(i))
            else:
                print("se sigue el curso")
        elif quads[i][0] == 'GOSUB':
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
    