#Ivan Contreras Rodriguez
#A01540379
#ForeverAlone

import codecs

# Set up a logging object
import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

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
    'haz' : 'HAZ',
    'desde' : 'DESDE',
    'hasta' : 'HASTA',
    'hacer' : 'HACER'
}

tokennames = [
    'ID', 'NOMPROG', 'NOMMOD', 
    'SEMICOLON', 'COMMA', 'DOUBLEP',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'NOTEQUAL', 'GREATER', 'LESS', 'GREATERO', 'LESSO', 'EQUAL',
    'CTEI', 'CTEF', 'CTES', 'CTEC',
    'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY',
    'AND', 'OR'
    ]+ list(reserved.values())

#tokens

t_COMMA     = r','
t_SEMICOLON = r';'
t_DOUBLEP   = r':'

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

def t_NOMPROG(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NOMPROG')    # Check for reserved words
    return t

def t_NOMMOD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NOMMOD')    # Check for reserved words
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
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_CTEC(t):
    r'\w{1}'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Ignored characters
t_ignore = " \t"

# Para detectar los saltos de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Para mostrar errores lexicos    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

##################### Parsing rules

#Para evitar conflictos en la gramatica
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    )

start = 'programa'

def p_empty(p):
    'empty :'
    pass

##### PROGRAMA

def p_programa(t):
    'programa : PROGRAMA NOMPROG SEMICOLON pro1 pro2 main'
    t[0] = t[4], t[5], t[6]

def p_pro1(t):
    'pro1 : vars'
    t[0] = t[1]

def p_pro1_empty(t):
    'pro1 : empty'

def p_pro2(t):
    'pro2 : func'
    t[0] = t[1]

def p_pro2_empty(t):
    'pro2 : empty'


##### VARS

def p_vars(t):
    'vars: VAR var1 var2'
    t[0] = t[2], t[3]

def p_var1(t):
    'var1 : tipo DOUBLEP lista_ids SEMICOLON'
    t[0] = t[1], t[3]

def p_var2(t):
    'var2 : var1 var2'
    t[0] = t[1], t[2]

def p_var2_empty(t):
    'var2 : empty'

##### FUNC

def p_func(t):
    'func : FUNCION tipo_retorno NOMMOD LPAREN params RPAREN func1 bloque'
    t[0] = t[2], t[5], t[7], t[8]

def p_func1(t):
    'func1 : vars'
    t[0] = t[1]

def p_func1_empty(t):
    'func1 : empty'

##### BLOQUE

def p_bloque(t):
    'bloque : LCURLY bloque1 bloque2 RCURLY'
    t[0] = t[2], t[3]

def p_bloque1(t):
    'bloque1 : estatuto'
    t[0] = t[1]

def p_bloque2(t):
    'bloque2 : bloque1 bloque2'
    t[0] = t[1], t[2]

def p_bloque2_empty(t):
    'bloque2 : empty'

##### ESTATUTO

def p_estatuto1(t):
    'estatuto: asig'
    t[0] = t[1]

def p_estatuto2(t):
    'estatuto: cond'
    t[0] = t[1]

def p_estatuto3(t):
    'estatuto: retorno'
    t[0] = t[1]

def p_estatuto4(t):
    'estatuto: lectura'
    t[0] = t[1]

def p_estatuto5(t):
    'estatuto: escritura'
    t[0] = t[1]

def p_estatuto6(t):
    'estatuto: llamadav'
    t[0] = t[1]

def p_estatuto7(t):
    'estatuto: repeticion'
    t[0] = t[1]

##### ASIG

def p_asig(t):
    'asig : ID asig1 EQUAL asig2'
    t[0] = t[2], t[4]

def p_asig1(t):
    'asig1 : dimension'
    t[0] = t[1]

def p_asig1_empty(t):
    'asig1 : empty'

def p_asig2_a(t):
    'asig2 : superexp'
    t[0] = t[1]

def p_asig2_b(t):
    'asig2 : asig3'
    t[0] = t[1]

def p_asig2_c(t):
    'asig2 : empty'

def p_asig3(t):
    'asig3 : NOMMOD LPAREN asig4 asig5 RPAREN'
    t[0] = t[3], t[4]

def p_asig4(t):
    'asig4 : superexp'

def p_asig5(t):
    'asig5 : asig4 asig5'
    t[0] = t[1], t[2]

def p_asig5_empty(t):
    'asig5 : empty'

##### MAIN

def p_main(t):
    'main : PRINCIPAL LPAREN RPAREN bloque'
    t[0] = t[4]

##### TIPO

def p_tipo1(t):
    'tipo : INT'
    t[0] = t[1]

def p_tipo2(t):
    'tipo : FLOAT'
    t[0] = t[1]

def p_tipo3(t):
    'tipo : CHAR'
    t[0] = t[1]

##### TIPO_RETORNO

def p_tipo_retorno1(t):
    'tipo_retorno : INT'
    t[0] = t[1]

def p_tipo_retorno2(t):
    'tipo_retorno : FLOAT'
    t[0] = t[1]

def p_tipo_retorno3(t):
    'tipo_retorno : CHAR'

def p_tipo_retorno4(t):
    'tipo_retorno : VOID'

##### LISTA_IDS

def p_listaids(t):
    'lista_ids : lista1 lista2'
    t[0] = t[1], t[2]

def p_listaids1(t):
    'lista1 : ID dimension SEMICOLON'
    t[0] = t[2]

def p_listaids2(t):
    'lista2 : lista1 lista2'
    t[0] = t[1], t[2]

def p_listaids2(t):
    'lista2 : empty'

##### PARAMS

def p_params(t):
    'params : params1 params2'
    t[0] = t[1], t[2]

def p_params1(t):
    'params1 : tipo ID'
    t[0] = t[1]

def p_params2(t):
    'params2 : COMMA params1 params2'
    t[0] = t[2], t[3]

def p_params2_empty(t):
    'params2 : empty'

##### FACTOR

def p_factor_a(t):
    'factor : LPAREN superexp RPAREN'
    t[0] = t[2]

def p_factor_b(t):
    'factor : factor1'
    t[0] = t[1]

def p_factor_c(t):
    'factor : factor2'

def p_factor1_a(t):
    'factor1 : PLUS varcte'
    t[0] = t[2]

def p_factor1_b(t):
    'factor1 : MINUS varcte'
    t[0] = t[2]

def p_factor1_c(t):
    'factor1 : varcte'
    t[0] = t[1]

def factor2_a(t):
    'factor2 : ID factor3'
    t[0] = t[2]

def factor2_b(t):
    'factor2 : ID factor4'
    t[0] = t[2]

def factor3(t):
    'factor3 : LPAREN factor5 factor6 RPAREN'
    t[0] = t[2], t[3]

def factor4_a(t):
    'factor4 : dimension'
    t[0] = t[1]

def factor4_b(t):
    'factor4 : empty'

def factor5(t):
    'factor5 : exp'
    t[0] = t[1]

def factor6_a(t):
    'factor6 : COMMA factor5 factor6'
    t[0] = t[2], t[3]

def factor6_b(t):
    'factor6 : empty'

##### DIMENSION

def p_dimension(t):
    'dimension : LBRACKET exp RBRACKET'
    t[0] = t[2]

##### DIMENSIONI

def p_dimensioni(t):
    'dimensioni : LBRACKET CTEI RBRACKET'

###### RETORNO

def p_retorno(t):
    'retorno : REGRESA LPAREN exp RPAREN SEMICOLON'
    t[0] = t[3]

###### LLAMADAV

def p_llamadav(t):
    'llamadav : NOMMOD LPAREN llamada1 llamada2 RPAREN SEMICOLON'
    t[0] = t[3], t[4]

def p_llamada1(t):
    'llamada1 : exp'
    t[0] = t[1]

def p_llamada2_a(t):
    'llamada2 : COMMA llamada1 llamada2'
    t[0] = t[2], t[3]

def p_llamada2_b(t):
    'llamada2 : empty'

##### LECTURA

def p_lectura(t):
    'lectura : LEE LPAREN lectura1 lectura2 RPAREN SEMICOLON'
    t[0] = t[3], t[4]

def p_lectura1(t):
    'lectura1 : ID lectura3'
    t[0] = t[2]

def p_lectura2_a(t):
    'lectura2 : COMMA lectura1 lectura2'
    t[0] = t[2], t[3]

def p_lectura2_b(t):
    'lectura2 : empty'

def p_lectura3_a(t):
    'lectura3 : dimension'
    t[0] = t[1]

def p_lectura3_b(t):
    'lectura3 : empty'

##### ESCRITURA

def p_escritura(t):
    'escritura : ESCRIBE LPAREN escritura1 escritura2 RPAREN SEMICOLON'
    t[0] = t[3]., t[4]

def p_escritura1_a(t):
    'escritura1 : CTES'

def p_escritura1_b(t):
    'escritura1 : superexp'
    t[0] = t[1]

def p_escritura2_a(t):
    'escritura2 : COMMA escritura1 escritura2'
    t[0] = t[2], t[3]

def p_escritura2_b(t):
    'escritura2 : empty'

##### CONDICION

def p_condicion(t):
    'condicion : SI LPAREN superexp RPAREN ENTONCES bloque condicion1'
    t[0] = t[3], t[6], t[7]

def p_condicion1_a(t):
    'condicion1 : SINO bloque'
    t[0] = t[2]

def p_condicion1_b(t):
    'condicion1 : empty'

##### REPETICION

def p_repeticion_a(t):
    'repeticion : condicional'
    t[0] = t[1]

def p_repeticion_b(t):
    'repeticion : nocondicional'
    t[0] = t[1]

###### CONDICIONAL

def p_condicional(t):
    'condicional : mientras LPAREN superexp RPAREN HAZ bloque'
    t[0] = t[1], t[3]

###### NOCONDICIONAL

def p_nocondicional(t):
    'nocondicional : DESDE ID dimension EQUAL exp HASTA exp HACER bloque'
    t[0] = t[3], t[5], t[7], t[9]

##### SUPEREXP

def p_superexp(t):
    'superexp : exp superexp1'
    t[0] = t[1], t[2]

def p_superexp1_a(t):
    'superexp1 : AND expresion'
    t[0] = t[2]

def p_superexp1_b(t):
    'superexp1 : OR expresion'
    t[0] = t[2]

def p_superexp1_c(t):
    'superexp1 : empty'

##### EXPRESION

def p_expresion(t):
    'expresion : exp expresion1'
    t[0] = t[1], t[2]

def p_expresion1_a(t):
    'expresion1 : GREATER expresion2 expresion3'
    t[0] = t[2], t[3]

def p_expresion1_b(t):
    'expresion1 : LESS expresion2 expresion3'
    t[0] = t[2], t[3]

def p_expresion1_c(t):
    'expresion1 : EQUALS expresion3'
    t[0] = t[2]

def p_expresion1_d(t):
    'expresion1 : NOTEQUAL expresion3'
    t[0] = t[2]

def p_expresion2_a(t):
    'expresion2 : EQUAL'

def p_expresion2_b(t):
    'expresion2 : empty'

def p_expresion3(t):
    'expresion3 : exp'

##### EXP

def p_exp(t):
    'exp : termino exp1'
    t[0] = t[1], t[2]

def p_exp1_a(t):
    'exp1 : exp2 termino exp1'
    t[0] = t[1], t[2], t[3]

def p_exp2_b(t):
    'exp1 : empty'

def p_exp2_a(t):
    'exp2 : PLUS'

def p_exp2_b(t):
    'exp2 : MINUS'

##### TERMINO

def p_termino(t):
    'termino : factor termino1'
    t[0] = t[1], t[2]

def p_termino1_a(t):
    'termino1 : TIMES factor termino1'
    t[0] = t[2], t[3]

def p_termino1_b(t):
    'termino1 : DIVIDE factor termino1'
    t[0] = t[2], t[3]

def p_termino1_c(t):
    'termino1 : empty'

##### VARCTE

def p_varcte_a(t):
    'varcte : ID'

def p_varcte_b(t):
    'varcte : CTEI'

def p_varcte_c(t):
    'varcte : CTEF'

def p_varcte_d(t):
    'varcte : CTEC'

import ply.yacc as yacc
parser = yacc.yacc(start='programa',debug=True,debuglog=log,errorlog=log)

#Para definir el archivo que contiene el programa
filename = "test.txt"

#Para leer el contenido del archivo
fp = codecs.open(filename,"r","utf-8")
cadena = fp.read()
fp.close()

#Poner en marcha el parser
parser.parse(cadena)