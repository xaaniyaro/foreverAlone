#Ivan Contreras Rodriguez
#A01540379
#ForeverAlone

import codecs

states = (
    ('ctes', 'inclusive'), 
    ('ctec', 'inclusive')
)

reserved = {
    'si' : 'SI',
    'sino' : 'SINO',
    'escribe' : 'ESCRIBE',
    'programa' : 'PROGRAMA',
    'var' : 'VAR',
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'lee' : 'LEE',
    'regresa' : 'REGRESA',
    'principal' : 'PRINCIPAL',
    'void' : 'VOID',
    'funcion' : 'FUNCION',
    'mientras' : 'MIENTRAS',
    'entonces' : 'ENTONCES',
    'haz' : 'HAZ',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER'
}

tokens = [
    'SEMICOLON', 'ID', 'COMMA',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'NOTEQUAL', 'GREATER', 'LESS', 'GREATERO', 'LESSO', 'EQUAL',
    'CTEI', 'CTEF', 'CTES', 'CTEC',
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY',
    'AND', 'OR'
    ]+ list(reserved.values())

#tokens

t_COMMA     = r','
t_SEMICOLON = r';'

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'

t_NOTEQUAL  = r'!='
t_EQUALS    = r'=='
t_LESS      = r'<'
t_LESSO     = r'<='
t_GREATER   = r'>'
t_GREATERO  = r'>='
t_EQUAL     = r'='

t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCURLY  = r'\{'
t_RCURLY  = r'\}'
t_LBRACKET= r'\['
t_RBRACKET= r'\]'

t_AND     = r'&'
t_OR      = r'\|'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTEF(t):
    r'\d+\.\d+'   
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floating value too large %f", t.value)
        t.value = 0.0   
    return t

def t_CTEI(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CTES(t):
    r'[\"]'
    t.lexer.begin('ctes')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value

def t_ctes_chars(t):
    r'[^"\n]+'


def t_ctes_newline(t):
    r'\n+'
    print("Incorrectly terminated string %s" % t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1])
    t.lexer.skip(1)


def t_ctes_end(t):
    r'[\"]'

    if t.lexer.str_marker == t.value:
        t.type = 'CTES'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        t.lexer.begin('INITIAL')
        return t

def t_CTEC(t):
    r'[\']'
    t.lexer.begin('ctec')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value

def t_ctec_chars(t):
    r'[^\'\n]{1}'


def t_ctec_newline(t):
    r'\n+'
    print("Incorrectly terminated char %s" % t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1])
    t.lexer.skip(1)


def t_ctec_end(t):
    r'[\']'

    if t.lexer.str_marker == t.value:
        t.type = 'CTEC'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        t.lexer.begin('INITIAL')
        return t

# Ignored characters
t_ignore=' \t\r\n\f\v'

# Para detectar los saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Para mostrar errores lexicos    
def t_error(t):
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

#Para definir el archivo que contiene el programa
filename = "test.txt"

#Para leer el contenido del archivo
fp = codecs.open(filename,"r","utf-8")
cadena = fp.read()
fp.close()

f = open("lexeroutput.txt","w+")

lexer.input(cadena)
while True:
    tok = lexer.token()
    if not tok:
        break
    f.write(str(tok) + "\n")

f.close()