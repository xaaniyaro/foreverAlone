
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaleftPLUSMINUSleftTIMESDIVIDErightEQUALSleftANDORAND CHAR COMMA CTEC CTEF CTEI CTES DESDE DIVIDE ENTONCES EQUAL EQUALS ESCRIBE FLOAT FUNCION GREATER GREATERO HACER HASTA HAZ ID INT LBRACKET LCURLY LEE LESS LESSO LPAREN MIENTRAS MINUS NOTEQUAL OR PLUS PRINCIPAL PROGRAMA RBRACKET RCURLY REGRESA RPAREN SEMICOLON SI SINO TIMES VAR VOIDempty :programa : PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main showstacksaddMain : emptycreateTable : emptyvars : VAR var2var1 : tipo lista_ids SEMICOLONvar2 : var1 var2\n            | var1 var_decl :  ID\n                |   ID LBRACKET CTEI RBRACKET\n                |   ID LBRACKET exp RBRACKETlista_ids : lista_ids COMMA var_decl\n                | var_decl tipo : INT\n            | FLOAT\n            | CHARfunc_declarations : func_decl funcBody func_declarations\n                        | emptyfunc_decl : FUNCION func2 func3 LPAREN params RPAREN vars\n                 | FUNCION func2 func3 LPAREN RPAREN vars\n                 | FUNCION func2 func3 LPAREN params RPAREN \n                 | FUNCION func2 func3 LPAREN RPARENfuncBody : bloque endFuncfunc3 : IDfunc2 : tipo\n            | VOIDendFunc : emptybloque : LCURLY bloque1 RCURLYbloque1 : estatuto bloque1\n                | emptyestatuto : asig\n                | cond\n                | retorno\n                | lectura\n                | escritura\n                | llamada SEMICOLON\n                | repeticionasig : variable addVar EQUAL addAsig exp genAsig SEMICOLONaddVar : addAsig : genAsig : main : printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque mergetablesfillFirst : emptyparam_decl : tipo IDparams : params COMMA param_decl\n                | param_declretorno : REGRESA LPAREN exp RPAREN SEMICOLONllamada : iniciaLlamada llamada2 endLlamada RPAREN\n                | iniciaLlamada endLlamada RPARENiniciaLlamada : ID LPARENllamada2 : exp COMMA llamada2\n                | expendLlamada : lectura : LEE LPAREN variable RPAREN SEMICOLONescritura : ESCRIBE LPAREN escritura2 RPAREN SEMICOLONescritura1 : CTES\n                | expescritura2 : escritura1 addescritura COMMA escritura2\n                    | escritura1 addescritura addescritura : cond : SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2cond1 : emptycond2 : emptyelsePart : SINO elseActions bloque\n                | emptyelseActions : emptyrepeticion : condicional\n                | nocondicionalcondicional : MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhileregWhile : emptywhileCond : emptyendWhile : emptynocondicional : DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endForcreateFor : endFor : exp : texp exp1exp1 : OR texp exp1\n            | emptytexp : gexp texp1texp1 : AND gexp texp1\n             | emptygexp : mexp gexp1gexp1 : gexp2 mexp gexp1\n             | emptygexp2 : LESS\n            | LESSO\n            | GREATER\n            | GREATERO\n            | NOTEQUAL\n            | EQUALSmexp : termino mexp1mexp1 : mexp2 termino mexp1\n             | emptymexp2 : PLUS\n            | MINUStermino : factor termino1termino1 : TIMES factor termino1\n                | DIVIDE factor termino1\n                | emptyfactor : LPAREN exp RPAREN\n                | varcte\n                | variable\n                | llamadavariable : IDvarcte :  CTEI\n                | CTEF\n                | CTEC mergetables : emptyshowstacks : emptyprintfuncs : empty'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,25,37,38,81,173,185,186,],[0,-1,-2,-109,-28,-1,-42,-108,]),'ID':([2,13,14,15,16,30,31,32,33,35,36,44,46,47,48,49,50,52,58,59,60,63,74,81,83,85,86,87,88,93,101,104,107,109,110,111,112,113,114,116,118,119,121,122,126,137,138,143,153,177,178,179,180,193,194,197,199,200,202,203,206,207,208,209,210,],[3,24,-14,-15,-16,61,65,-25,-26,24,61,61,-31,-32,-33,-34,-35,-37,61,-67,-68,96,61,-28,-36,61,61,130,61,-50,61,61,61,-85,-86,-87,-88,-89,-90,61,-94,-95,61,61,-40,61,61,166,61,-47,-54,-55,61,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'SEMICOLON':([3,22,23,24,51,61,66,69,70,71,72,73,75,76,77,78,79,92,98,99,100,102,103,105,106,108,115,117,120,123,136,144,145,146,147,148,149,150,155,156,157,159,167,168,169,170,171,172,174,187,],[4,34,-13,-9,83,-104,-12,-1,-1,-1,-1,-1,-101,-102,-103,-106,-107,-105,-10,-11,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-49,-1,-1,-1,-1,-1,-1,-100,177,178,179,-48,-77,-80,-83,-92,-97,-98,-41,193,]),'VAR':([4,5,6,141,163,],[-1,8,-3,8,8,]),'FUNCION':([7,9,10,11,12,21,28,29,34,41,42,81,],[-1,20,-4,-5,-8,-7,20,-1,-6,-23,-27,-28,]),'PRINCIPAL':([7,9,10,11,12,17,19,21,26,27,28,29,34,40,41,42,81,],[-1,-1,-4,-5,-8,-1,-18,-7,39,-110,-1,-1,-6,-17,-23,-27,-28,]),'INT':([8,12,20,34,97,164,],[14,14,14,-6,14,14,]),'FLOAT':([8,12,20,34,97,164,],[15,15,15,-6,15,15,]),'CHAR':([8,12,20,34,97,164,],[16,16,16,-6,16,16,]),'LCURLY':([11,12,18,21,34,125,141,151,152,163,165,183,188,195,198,201,204,205,],[-5,-8,30,-7,-6,-1,-22,30,-43,-21,-20,-19,30,30,-1,30,30,-66,]),'VOID':([20,],[33,]),'COMMA':([22,23,24,61,66,69,70,71,72,73,75,76,77,78,79,91,92,98,99,100,102,103,105,106,108,115,117,120,123,132,133,134,136,140,142,144,145,146,147,148,149,150,158,159,166,167,168,169,170,171,172,184,],[35,-13,-9,-104,-12,-1,-1,-1,-1,-1,-101,-102,-103,-106,-107,137,-105,-10,-11,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-60,-56,-57,-49,164,-46,-1,-1,-1,-1,-1,-1,-100,180,-48,-44,-77,-80,-83,-92,-97,-98,-45,]),'LBRACKET':([24,],[36,]),'RCURLY':([30,43,44,45,46,47,48,49,50,52,59,60,81,82,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[-1,81,-1,-30,-31,-32,-33,-34,-35,-37,-67,-68,-28,-29,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'SI':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[54,54,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'REGRESA':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[55,55,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'LEE':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[56,56,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'ESCRIBE':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[57,57,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'MIENTRAS':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[62,62,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'DESDE':([30,44,46,47,48,49,50,52,59,60,81,83,177,178,179,193,194,197,199,200,202,203,206,207,208,209,210,],[63,63,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'CTEI':([36,58,74,85,86,88,93,101,104,107,109,110,111,112,113,114,116,118,119,121,122,126,137,138,139,153,180,182,],[67,92,92,92,92,92,-50,92,92,92,-85,-86,-87,-88,-89,-90,92,-94,-95,92,92,-40,92,92,162,92,92,192,]),'LPAREN':([36,39,54,55,56,57,58,61,62,64,65,74,85,86,88,93,94,95,101,104,107,109,110,111,112,113,114,116,118,119,121,122,126,137,138,153,180,],[74,80,85,86,87,88,74,93,-1,97,-24,74,74,74,74,-50,138,-70,74,74,74,-85,-86,-87,-88,-89,-90,74,-94,-95,74,74,-40,74,74,74,74,]),'CTEF':([36,58,74,85,86,88,93,101,104,107,109,110,111,112,113,114,116,118,119,121,122,126,137,138,153,180,],[78,78,78,78,78,78,-50,78,78,78,-85,-86,-87,-88,-89,-90,78,-94,-95,78,78,-40,78,78,78,78,]),'CTEC':([36,58,74,85,86,88,93,101,104,107,109,110,111,112,113,114,116,118,119,121,122,126,137,138,153,180,],[79,79,79,79,79,79,-50,79,79,79,-85,-86,-87,-88,-89,-90,79,-94,-95,79,79,-40,79,79,79,79,]),'EQUAL':([53,61,84,96,],[-39,-104,126,139,]),'RPAREN':([58,61,69,70,71,72,73,75,76,77,78,79,80,89,90,91,92,93,97,100,102,103,105,106,108,115,117,120,123,124,127,128,129,130,131,132,133,134,135,136,140,142,144,145,146,147,148,149,150,158,159,160,161,166,167,168,169,170,171,172,184,189,],[-53,-104,-1,-1,-1,-1,-1,-101,-102,-103,-106,-107,125,-53,136,-52,-105,-50,141,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,150,154,155,156,-104,157,-60,-56,-57,159,-49,163,-46,-1,-1,-1,-1,-1,-1,-100,-59,-48,-51,181,-44,-77,-80,-83,-92,-97,-98,-45,-58,]),'TIMES':([61,67,73,75,76,77,78,79,92,136,148,149,150,159,],[-104,-105,121,-101,-102,-103,-106,-107,-105,-49,121,121,-100,-48,]),'DIVIDE':([61,67,73,75,76,77,78,79,92,136,148,149,150,159,],[-104,-105,122,-101,-102,-103,-106,-107,-105,-49,122,122,-100,-48,]),'PLUS':([61,67,72,73,75,76,77,78,79,92,120,123,136,147,148,149,150,159,171,172,],[-104,-105,118,-1,-101,-102,-103,-106,-107,-105,-96,-99,-49,118,-1,-1,-100,-48,-97,-98,]),'MINUS':([61,67,72,73,75,76,77,78,79,92,120,123,136,147,148,149,150,159,171,172,],[-104,-105,119,-1,-101,-102,-103,-106,-107,-105,-96,-99,-49,119,-1,-1,-100,-48,-97,-98,]),'LESS':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,109,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,109,-1,-1,-1,-100,-48,-92,-97,-98,]),'LESSO':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,110,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,110,-1,-1,-1,-100,-48,-92,-97,-98,]),'GREATER':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,111,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,111,-1,-1,-1,-100,-48,-92,-97,-98,]),'GREATERO':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,112,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,112,-1,-1,-1,-100,-48,-92,-97,-98,]),'NOTEQUAL':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,113,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,113,-1,-1,-1,-100,-48,-92,-97,-98,]),'EQUALS':([61,67,71,72,73,75,76,77,78,79,92,115,117,120,123,136,146,147,148,149,150,159,170,171,172,],[-104,-105,114,-1,-1,-101,-102,-103,-106,-107,-105,-91,-93,-96,-99,-49,114,-1,-1,-1,-100,-48,-92,-97,-98,]),'AND':([61,67,70,71,72,73,75,76,77,78,79,92,106,108,115,117,120,123,136,145,146,147,148,149,150,159,169,170,171,172,],[-104,-105,104,-1,-1,-1,-101,-102,-103,-106,-107,-105,-82,-84,-91,-93,-96,-99,-49,104,-1,-1,-1,-1,-100,-48,-83,-92,-97,-98,]),'OR':([61,67,69,70,71,72,73,75,76,77,78,79,92,103,105,106,108,115,117,120,123,136,144,145,146,147,148,149,150,159,168,169,170,171,172,],[-104,-105,101,-1,-1,-1,-1,-101,-102,-103,-106,-107,-105,-79,-81,-82,-84,-91,-93,-96,-99,-49,101,-1,-1,-1,-1,-1,-100,-48,-80,-83,-92,-97,-98,]),'RBRACKET':([61,67,68,69,70,71,72,73,75,76,77,78,79,92,100,102,103,105,106,108,115,117,120,123,136,144,145,146,147,148,149,150,159,167,168,169,170,171,172,],[-104,98,99,-1,-1,-1,-1,-1,-101,-102,-103,-106,-107,-105,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-49,-1,-1,-1,-1,-1,-1,-100,-48,-77,-80,-83,-92,-97,-98,]),'SINO':([81,194,],[-28,198,]),'CTES':([88,180,],[133,133,]),'ENTONCES':([154,175,176,],[-1,188,-62,]),'HASTA':([162,],[182,]),'HAZ':([181,190,191,],[-1,195,-71,]),'HACER':([192,196,],[-74,201,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'addMain':([4,],[5,]),'empty':([4,7,9,17,25,28,29,30,44,62,69,70,71,72,73,125,144,145,146,147,148,149,154,173,181,194,197,198,200,],[6,10,19,27,38,19,42,45,45,95,102,105,108,117,123,152,102,105,108,117,123,123,176,186,191,199,203,205,207,]),'vars':([5,141,163,],[7,165,183,]),'createTable':([7,],[9,]),'var2':([8,12,],[11,21,]),'var1':([8,12,],[12,12,]),'tipo':([8,12,20,97,164,],[13,13,32,143,143,]),'func_declarations':([9,28,],[17,40,]),'func_decl':([9,28,],[18,18,]),'lista_ids':([13,],[22,]),'var_decl':([13,35,],[23,66,]),'main':([17,],[25,]),'printfuncs':([17,],[26,]),'funcBody':([18,],[28,]),'bloque':([18,151,188,195,201,204,],[29,173,194,200,208,209,]),'func2':([20,],[31,]),'showstacks':([25,],[37,]),'endFunc':([29,],[41,]),'bloque1':([30,44,],[43,82,]),'estatuto':([30,44,],[44,44,]),'asig':([30,44,],[46,46,]),'cond':([30,44,],[47,47,]),'retorno':([30,44,],[48,48,]),'lectura':([30,44,],[49,49,]),'escritura':([30,44,],[50,50,]),'llamada':([30,36,44,58,74,85,86,88,101,104,107,116,121,122,137,138,153,180,],[51,77,51,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'repeticion':([30,44,],[52,52,]),'variable':([30,36,44,58,74,85,86,87,88,101,104,107,116,121,122,137,138,153,180,],[53,76,53,76,76,76,76,129,76,76,76,76,76,76,76,76,76,76,76,]),'iniciaLlamada':([30,36,44,58,74,85,86,88,101,104,107,116,121,122,137,138,153,180,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'condicional':([30,44,],[59,59,]),'nocondicional':([30,44,],[60,60,]),'func3':([31,],[64,]),'exp':([36,58,74,85,86,88,137,138,153,180,],[68,91,124,127,128,134,91,161,174,134,]),'texp':([36,58,74,85,86,88,101,137,138,153,180,],[69,69,69,69,69,69,144,69,69,69,69,]),'gexp':([36,58,74,85,86,88,101,104,137,138,153,180,],[70,70,70,70,70,70,70,145,70,70,70,70,]),'mexp':([36,58,74,85,86,88,101,104,107,137,138,153,180,],[71,71,71,71,71,71,71,71,146,71,71,71,71,]),'termino':([36,58,74,85,86,88,101,104,107,116,137,138,153,180,],[72,72,72,72,72,72,72,72,72,147,72,72,72,72,]),'factor':([36,58,74,85,86,88,101,104,107,116,121,122,137,138,153,180,],[73,73,73,73,73,73,73,73,73,73,148,149,73,73,73,73,]),'varcte':([36,58,74,85,86,88,101,104,107,116,121,122,137,138,153,180,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'addVar':([53,],[84,]),'llamada2':([58,137,],[89,160,]),'endLlamada':([58,89,],[90,135,]),'regWhile':([62,],[94,]),'exp1':([69,144,],[100,167,]),'texp1':([70,145,],[103,168,]),'gexp1':([71,146,],[106,169,]),'gexp2':([71,146,],[107,107,]),'mexp1':([72,147,],[115,170,]),'mexp2':([72,147,],[116,116,]),'termino1':([73,148,149,],[120,171,172,]),'escritura2':([88,180,],[131,189,]),'escritura1':([88,180,],[132,132,]),'params':([97,],[140,]),'param_decl':([97,164,],[142,184,]),'fillFirst':([125,],[151,]),'addAsig':([126,],[153,]),'addescritura':([132,],[158,]),'cond1':([154,],[175,]),'mergetables':([173,],[185,]),'genAsig':([174,],[187,]),'whileCond':([181,],[190,]),'createFor':([192,],[196,]),'elsePart':([194,],[197,]),'cond2':([197,],[202,]),'elseActions':([198,],[204,]),'endWhile':([200,],[206,]),'endFor':([208,],[210,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','scanner.py',285),
  ('programa -> PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main showstacks','programa',9,'p_programa','scanner.py',296),
  ('addMain -> empty','addMain',1,'p_addMain','scanner.py',300),
  ('createTable -> empty','createTable',1,'p_createTable','scanner.py',307),
  ('vars -> VAR var2','vars',2,'p_vars','scanner.py',318),
  ('var1 -> tipo lista_ids SEMICOLON','var1',3,'p_var1','scanner.py',334),
  ('var2 -> var1 var2','var2',2,'p_var2','scanner.py',340),
  ('var2 -> var1','var2',1,'p_var2','scanner.py',341),
  ('var_decl -> ID','var_decl',1,'p_var_decl','scanner.py',351),
  ('var_decl -> ID LBRACKET CTEI RBRACKET','var_decl',4,'p_var_decl','scanner.py',352),
  ('var_decl -> ID LBRACKET exp RBRACKET','var_decl',4,'p_var_decl','scanner.py',353),
  ('lista_ids -> lista_ids COMMA var_decl','lista_ids',3,'p_lista_ids','scanner.py',380),
  ('lista_ids -> var_decl','lista_ids',1,'p_lista_ids','scanner.py',381),
  ('tipo -> INT','tipo',1,'p_tipo','scanner.py',395),
  ('tipo -> FLOAT','tipo',1,'p_tipo','scanner.py',396),
  ('tipo -> CHAR','tipo',1,'p_tipo','scanner.py',397),
  ('func_declarations -> func_decl funcBody func_declarations','func_declarations',3,'p_func_declarations','scanner.py',403),
  ('func_declarations -> empty','func_declarations',1,'p_func_declarations','scanner.py',404),
  ('func_decl -> FUNCION func2 func3 LPAREN params RPAREN vars','func_decl',7,'p_func_decl','scanner.py',407),
  ('func_decl -> FUNCION func2 func3 LPAREN RPAREN vars','func_decl',6,'p_func_decl','scanner.py',408),
  ('func_decl -> FUNCION func2 func3 LPAREN params RPAREN','func_decl',6,'p_func_decl','scanner.py',409),
  ('func_decl -> FUNCION func2 func3 LPAREN RPAREN','func_decl',5,'p_func_decl','scanner.py',410),
  ('funcBody -> bloque endFunc','funcBody',2,'p_funcBody','scanner.py',460),
  ('func3 -> ID','func3',1,'p_func3','scanner.py',463),
  ('func2 -> tipo','func2',1,'p_func2','scanner.py',470),
  ('func2 -> VOID','func2',1,'p_func2','scanner.py',471),
  ('endFunc -> empty','endFunc',1,'p_endFunc','scanner.py',475),
  ('bloque -> LCURLY bloque1 RCURLY','bloque',3,'p_bloque','scanner.py',484),
  ('bloque1 -> estatuto bloque1','bloque1',2,'p_bloque1','scanner.py',487),
  ('bloque1 -> empty','bloque1',1,'p_bloque1','scanner.py',488),
  ('estatuto -> asig','estatuto',1,'p_estatuto','scanner.py',493),
  ('estatuto -> cond','estatuto',1,'p_estatuto','scanner.py',494),
  ('estatuto -> retorno','estatuto',1,'p_estatuto','scanner.py',495),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','scanner.py',496),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','scanner.py',497),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','scanner.py',498),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','scanner.py',499),
  ('asig -> variable addVar EQUAL addAsig exp genAsig SEMICOLON','asig',7,'p_asig','scanner.py',504),
  ('addVar -> <empty>','addVar',0,'p_addVar','scanner.py',507),
  ('addAsig -> <empty>','addAsig',0,'p_addAsig','scanner.py',517),
  ('genAsig -> <empty>','genAsig',0,'p_genAsig','scanner.py',522),
  ('main -> printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque mergetables','main',7,'p_main','scanner.py',538),
  ('fillFirst -> empty','fillFirst',1,'p_fillFirst','scanner.py',542),
  ('param_decl -> tipo ID','param_decl',2,'p_param_decl','scanner.py',557),
  ('params -> params COMMA param_decl','params',3,'p_params','scanner.py',561),
  ('params -> param_decl','params',1,'p_params','scanner.py',562),
  ('retorno -> REGRESA LPAREN exp RPAREN SEMICOLON','retorno',5,'p_retorno','scanner.py',574),
  ('llamada -> iniciaLlamada llamada2 endLlamada RPAREN','llamada',4,'p_llamada','scanner.py',583),
  ('llamada -> iniciaLlamada endLlamada RPAREN','llamada',3,'p_llamada','scanner.py',584),
  ('iniciaLlamada -> ID LPAREN','iniciaLlamada',2,'p_iniciaLlamada','scanner.py',601),
  ('llamada2 -> exp COMMA llamada2','llamada2',3,'p_llamada2','scanner.py',616),
  ('llamada2 -> exp','llamada2',1,'p_llamada2','scanner.py',617),
  ('endLlamada -> <empty>','endLlamada',0,'p_endLlamada','scanner.py',625),
  ('lectura -> LEE LPAREN variable RPAREN SEMICOLON','lectura',5,'p_lectura','scanner.py',650),
  ('escritura -> ESCRIBE LPAREN escritura2 RPAREN SEMICOLON','escritura',5,'p_escritura','scanner.py',657),
  ('escritura1 -> CTES','escritura1',1,'p_escritura1','scanner.py',660),
  ('escritura1 -> exp','escritura1',1,'p_escritura1','scanner.py',661),
  ('escritura2 -> escritura1 addescritura COMMA escritura2','escritura2',4,'p_escritura2_a','scanner.py',665),
  ('escritura2 -> escritura1 addescritura','escritura2',2,'p_escritura2_a','scanner.py',666),
  ('addescritura -> <empty>','addescritura',0,'p_addescritura','scanner.py',669),
  ('cond -> SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2','cond',9,'p_cond','scanner.py',681),
  ('cond1 -> empty','cond1',1,'p_cond1','scanner.py',684),
  ('cond2 -> empty','cond2',1,'p_cond2','scanner.py',696),
  ('elsePart -> SINO elseActions bloque','elsePart',3,'p_elsePart','scanner.py',702),
  ('elsePart -> empty','elsePart',1,'p_elsePart','scanner.py',703),
  ('elseActions -> empty','elseActions',1,'p_elseActions','scanner.py',706),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','scanner.py',720),
  ('repeticion -> nocondicional','repeticion',1,'p_repeticion','scanner.py',721),
  ('condicional -> MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhile','condicional',9,'p_condicional','scanner.py',727),
  ('regWhile -> empty','regWhile',1,'p_regWhile','scanner.py',730),
  ('whileCond -> empty','whileCond',1,'p_whileCond','scanner.py',736),
  ('endWhile -> empty','endWhile',1,'p_endWhile','scanner.py',748),
  ('nocondicional -> DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endFor','nocondicional',10,'p_nocondicional','scanner.py',758),
  ('createFor -> <empty>','createFor',0,'p_createFor','scanner.py',761),
  ('endFor -> <empty>','endFor',0,'p_endFor','scanner.py',777),
  ('exp -> texp exp1','exp',2,'p_exp','scanner.py',809),
  ('exp1 -> OR texp exp1','exp1',3,'p_exp1','scanner.py',836),
  ('exp1 -> empty','exp1',1,'p_exp1','scanner.py',837),
  ('texp -> gexp texp1','texp',2,'p_texp','scanner.py',845),
  ('texp1 -> AND gexp texp1','texp1',3,'p_texp1','scanner.py',872),
  ('texp1 -> empty','texp1',1,'p_texp1','scanner.py',873),
  ('gexp -> mexp gexp1','gexp',2,'p_gexp','scanner.py',881),
  ('gexp1 -> gexp2 mexp gexp1','gexp1',3,'p_gexp1','scanner.py',909),
  ('gexp1 -> empty','gexp1',1,'p_gexp1','scanner.py',910),
  ('gexp2 -> LESS','gexp2',1,'p_gexp2','scanner.py',916),
  ('gexp2 -> LESSO','gexp2',1,'p_gexp2','scanner.py',917),
  ('gexp2 -> GREATER','gexp2',1,'p_gexp2','scanner.py',918),
  ('gexp2 -> GREATERO','gexp2',1,'p_gexp2','scanner.py',919),
  ('gexp2 -> NOTEQUAL','gexp2',1,'p_gexp2','scanner.py',920),
  ('gexp2 -> EQUALS','gexp2',1,'p_gexp2','scanner.py',921),
  ('mexp -> termino mexp1','mexp',2,'p_mexp','scanner.py',927),
  ('mexp1 -> mexp2 termino mexp1','mexp1',3,'p_mexp1','scanner.py',955),
  ('mexp1 -> empty','mexp1',1,'p_mexp1','scanner.py',956),
  ('mexp2 -> PLUS','mexp2',1,'p_mexp2','scanner.py',962),
  ('mexp2 -> MINUS','mexp2',1,'p_mexp2','scanner.py',963),
  ('termino -> factor termino1','termino',2,'p_termino','scanner.py',969),
  ('termino1 -> TIMES factor termino1','termino1',3,'p_termino1','scanner.py',998),
  ('termino1 -> DIVIDE factor termino1','termino1',3,'p_termino1','scanner.py',999),
  ('termino1 -> empty','termino1',1,'p_termino1','scanner.py',1000),
  ('factor -> LPAREN exp RPAREN','factor',3,'p_factor','scanner.py',1008),
  ('factor -> varcte','factor',1,'p_factor','scanner.py',1009),
  ('factor -> variable','factor',1,'p_factor','scanner.py',1010),
  ('factor -> llamada','factor',1,'p_factor','scanner.py',1011),
  ('variable -> ID','variable',1,'p_variable','scanner.py',1042),
  ('varcte -> CTEI','varcte',1,'p_varcte','scanner.py',1101),
  ('varcte -> CTEF','varcte',1,'p_varcte','scanner.py',1102),
  ('varcte -> CTEC','varcte',1,'p_varcte','scanner.py',1103),
  ('mergetables -> empty','mergetables',1,'p_mergetables','scanner.py',1107),
  ('showstacks -> empty','showstacks',1,'p_showstacks','scanner.py',1131),
  ('printfuncs -> empty','printfuncs',1,'p_printfuncs','scanner.py',1150),
]
