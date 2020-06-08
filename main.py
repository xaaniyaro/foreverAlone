import sys
from scanner import driver
#from vm import runcode
import codecs

def main(filename):
    contents = open_file(filename)
    driver(contents)

def open_file(filename):
    fp = codecs.open(filename,"r","utf-8")
    cadena = fp.read()  
    fp.close()
    return cadena

#Obtener el nombre del archivo desde el command line

if len(sys.argv) >= 2:
    main(sys.argv[1])
else:
    print("Por favor introduce el nombre del archivo a parsear")

