
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'programaleftPLUSMINUSleftTIMESDIVIDErightEQUALSleftANDORAND CHAR COMMA CTEC CTEF CTEI CTES DESDE DIVIDE ENTONCES EQUAL EQUALS ESCRIBE FLOAT FUNCION GREATER GREATERO HACER HASTA HAZ ID INT LBRACKET LCURLY LEE LESS LESSO LPAREN MIENTRAS MINUS NOTEQUAL OR PLUS PRINCIPAL PROGRAMA RBRACKET RCURLY REGRESA RPAREN SEMICOLON SI SINO TIMES VAR VOIDempty :programa : PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main showstacksaddMain : emptycreateTable : emptyvars : VAR var2var1 : tipo lista_ids SEMICOLONvar2 : var1 var2\n            | var1 var_decl :  ID\n                |   ID LBRACKET CTEI RBRACKET\n                |   ID LBRACKET exp RBRACKETlista_ids : lista_ids COMMA var_decl\n                | var_decl tipo : INT\n            | FLOAT\n            | CHARfunc_declarations : func_decl funcBody func_declarations\n                        | emptyfunc_decl : FUNCION func2 func3 LPAREN params RPAREN vars\n                 | FUNCION func2 func3 LPAREN RPAREN vars\n                 | FUNCION func2 func3 LPAREN params RPAREN \n                 | FUNCION func2 func3 LPAREN RPARENfuncBody : bloque endFuncfunc3 : IDfunc2 : tipo\n            | VOIDendFunc : emptybloque : LCURLY bloque1 RCURLYbloque1 : estatuto bloque1\n                | emptyestatuto : asig\n                | cond\n                | retorno\n                | lectura\n                | escritura\n                | llamada SEMICOLON\n                | repeticionasig : variable addVar EQUAL addAsig exp genAsig SEMICOLONaddVar : addAsig : genAsig : main : printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque mergetablesfillFirst : emptyparam_decl : tipo IDparams : params COMMA param_decl\n                | param_declretorno : REGRESA LPAREN exp RPAREN SEMICOLONllamada : iniciaLlamada llamada2 endLlamada RPAREN\n                | iniciaLlamada endLlamada RPARENiniciaLlamada : ID LPARENllamada2 : exp COMMA llamada2\n                | expendLlamada : lectura : LEE LPAREN variable RPAREN SEMICOLONescritura : ESCRIBE LPAREN escritura2 RPAREN SEMICOLONescritura1 : CTES\n                | expescritura2 : escritura1 addescritura COMMA escritura2\n                    | escritura1 addescritura addescritura : cond : SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2cond1 : emptycond2 : emptyelsePart : SINO elseActions bloque\n                | emptyelseActions : emptyrepeticion : condicional\n                | nocondicionalcondicional : MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhileregWhile : emptywhileCond : emptyendWhile : emptynocondicional : DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endForcreateFor : endFor : exp : texp exp1exp1 : OR texp exp1\n            | emptytexp : gexp texp1texp1 : AND gexp texp1\n             | emptygexp : mexp gexp1gexp1 : gexp2 mexp gexp1\n             | emptygexp2 : LESS\n            | LESSO\n            | GREATER\n            | GREATERO\n            | NOTEQUAL\n            | EQUALSmexp : termino mexp1mexp1 : mexp2 termino mexp1\n             | emptymexp2 : PLUS\n            | MINUStermino : factor termino1termino1 : TIMES factor termino1\n                | DIVIDE factor termino1\n                | emptyfactor : LPAREN exp RPAREN\n                | varcte\n                | variable\n                | llamadavariable : ID\n                | ID dimensiondimension : LBRACKET exp RBRACKETvarcte :  CTEI\n                | CTEF\n                | CTEC mergetables : emptyshowstacks : emptyprintfuncs : empty'
    
_lr_action_items = {'PROGRAMA':([0,],[2,]),'$end':([1,25,37,38,81,177,189,190,],[0,-1,-2,-111,-28,-1,-42,-110,]),'ID':([2,13,14,15,16,30,31,32,33,35,36,44,46,47,48,49,50,52,58,59,60,63,74,81,83,85,86,87,88,94,95,103,106,109,111,112,113,114,115,116,118,120,121,123,124,128,139,141,146,156,181,182,183,184,197,198,201,203,204,206,207,210,211,212,213,214,],[3,24,-14,-15,-16,61,65,-25,-26,24,61,61,-31,-32,-33,-34,-35,-37,61,-67,-68,98,61,-28,-36,61,61,132,61,-50,61,61,61,61,-85,-86,-87,-88,-89,-90,61,-94,-95,61,61,-40,61,61,170,61,-47,-54,-55,61,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'SEMICOLON':([3,22,23,24,51,61,66,69,70,71,72,73,75,76,77,78,79,92,93,100,101,102,104,105,107,108,110,117,119,122,125,138,147,148,149,150,151,152,153,158,159,160,162,164,171,172,173,174,175,176,178,191,],[4,34,-13,-9,83,-104,-12,-1,-1,-1,-1,-1,-101,-102,-103,-108,-109,-107,-105,-10,-11,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-49,-1,-1,-1,-1,-1,-1,-100,181,182,183,-48,-106,-77,-80,-83,-92,-97,-98,-41,197,]),'VAR':([4,5,6,144,167,],[-1,8,-3,8,8,]),'FUNCION':([7,9,10,11,12,21,28,29,34,41,42,81,],[-1,20,-4,-5,-8,-7,20,-1,-6,-23,-27,-28,]),'PRINCIPAL':([7,9,10,11,12,17,19,21,26,27,28,29,34,40,41,42,81,],[-1,-1,-4,-5,-8,-1,-18,-7,39,-112,-1,-1,-6,-17,-23,-27,-28,]),'INT':([8,12,20,34,99,168,],[14,14,14,-6,14,14,]),'FLOAT':([8,12,20,34,99,168,],[15,15,15,-6,15,15,]),'CHAR':([8,12,20,34,99,168,],[16,16,16,-6,16,16,]),'LCURLY':([11,12,18,21,34,127,144,154,155,167,169,187,192,199,202,205,208,209,],[-5,-8,30,-7,-6,-1,-22,30,-43,-21,-20,-19,30,30,-1,30,30,-66,]),'VOID':([20,],[33,]),'COMMA':([22,23,24,61,66,69,70,71,72,73,75,76,77,78,79,91,92,93,100,101,102,104,105,107,108,110,117,119,122,125,134,135,136,138,143,145,147,148,149,150,151,152,153,161,162,164,170,171,172,173,174,175,176,188,],[35,-13,-9,-104,-12,-1,-1,-1,-1,-1,-101,-102,-103,-108,-109,139,-107,-105,-10,-11,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-60,-56,-57,-49,168,-46,-1,-1,-1,-1,-1,-1,-100,184,-48,-106,-44,-77,-80,-83,-92,-97,-98,-45,]),'LBRACKET':([24,61,132,],[36,95,95,]),'RCURLY':([30,43,44,45,46,47,48,49,50,52,59,60,81,82,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[-1,81,-1,-30,-31,-32,-33,-34,-35,-37,-67,-68,-28,-29,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'SI':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[54,54,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'REGRESA':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[55,55,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'LEE':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[56,56,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'ESCRIBE':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[57,57,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'MIENTRAS':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[62,62,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'DESDE':([30,44,46,47,48,49,50,52,59,60,81,83,181,182,183,197,198,201,203,204,206,207,210,211,212,213,214,],[63,63,-31,-32,-33,-34,-35,-37,-67,-68,-28,-36,-47,-54,-55,-38,-1,-1,-65,-1,-61,-63,-69,-72,-75,-64,-73,]),'CTEI':([36,58,74,85,86,88,94,95,103,106,109,111,112,113,114,115,116,118,120,121,123,124,128,139,141,142,156,184,186,],[67,92,92,92,92,92,-50,92,92,92,92,-85,-86,-87,-88,-89,-90,92,-94,-95,92,92,-40,92,92,166,92,92,196,]),'LPAREN':([36,39,54,55,56,57,58,61,62,64,65,74,85,86,88,94,95,96,97,103,106,109,111,112,113,114,115,116,118,120,121,123,124,128,139,141,156,184,],[74,80,85,86,87,88,74,94,-1,99,-24,74,74,74,74,-50,74,141,-70,74,74,74,-85,-86,-87,-88,-89,-90,74,-94,-95,74,74,-40,74,74,74,74,]),'CTEF':([36,58,74,85,86,88,94,95,103,106,109,111,112,113,114,115,116,118,120,121,123,124,128,139,141,156,184,],[78,78,78,78,78,78,-50,78,78,78,78,-85,-86,-87,-88,-89,-90,78,-94,-95,78,78,-40,78,78,78,78,]),'CTEC':([36,58,74,85,86,88,94,95,103,106,109,111,112,113,114,115,116,118,120,121,123,124,128,139,141,156,184,],[79,79,79,79,79,79,-50,79,79,79,79,-85,-86,-87,-88,-89,-90,79,-94,-95,79,79,-40,79,79,79,79,]),'EQUAL':([53,61,84,93,98,164,],[-39,-104,128,-105,142,-106,]),'RPAREN':([58,61,69,70,71,72,73,75,76,77,78,79,80,89,90,91,92,93,94,99,102,104,105,107,108,110,117,119,122,125,126,129,130,131,132,133,134,135,136,137,138,143,145,147,148,149,150,151,152,153,161,162,163,164,165,170,171,172,173,174,175,176,188,193,],[-53,-104,-1,-1,-1,-1,-1,-101,-102,-103,-108,-109,127,-53,138,-52,-107,-105,-50,144,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,153,157,158,159,-104,160,-60,-56,-57,162,-49,167,-46,-1,-1,-1,-1,-1,-1,-100,-59,-48,-51,-106,185,-44,-77,-80,-83,-92,-97,-98,-45,-58,]),'TIMES':([61,67,73,75,76,77,78,79,92,93,138,151,152,153,162,164,],[-104,-107,123,-101,-102,-103,-108,-109,-107,-105,-49,123,123,-100,-48,-106,]),'DIVIDE':([61,67,73,75,76,77,78,79,92,93,138,151,152,153,162,164,],[-104,-107,124,-101,-102,-103,-108,-109,-107,-105,-49,124,124,-100,-48,-106,]),'PLUS':([61,67,72,73,75,76,77,78,79,92,93,122,125,138,150,151,152,153,162,164,175,176,],[-104,-107,120,-1,-101,-102,-103,-108,-109,-107,-105,-96,-99,-49,120,-1,-1,-100,-48,-106,-97,-98,]),'MINUS':([61,67,72,73,75,76,77,78,79,92,93,122,125,138,150,151,152,153,162,164,175,176,],[-104,-107,121,-1,-101,-102,-103,-108,-109,-107,-105,-96,-99,-49,121,-1,-1,-100,-48,-106,-97,-98,]),'LESS':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,111,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,111,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'LESSO':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,112,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,112,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'GREATER':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,113,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,113,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'GREATERO':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,114,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,114,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'NOTEQUAL':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,115,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,115,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'EQUALS':([61,67,71,72,73,75,76,77,78,79,92,93,117,119,122,125,138,149,150,151,152,153,162,164,174,175,176,],[-104,-107,116,-1,-1,-101,-102,-103,-108,-109,-107,-105,-91,-93,-96,-99,-49,116,-1,-1,-1,-100,-48,-106,-92,-97,-98,]),'AND':([61,67,70,71,72,73,75,76,77,78,79,92,93,108,110,117,119,122,125,138,148,149,150,151,152,153,162,164,173,174,175,176,],[-104,-107,106,-1,-1,-1,-101,-102,-103,-108,-109,-107,-105,-82,-84,-91,-93,-96,-99,-49,106,-1,-1,-1,-1,-100,-48,-106,-83,-92,-97,-98,]),'OR':([61,67,69,70,71,72,73,75,76,77,78,79,92,93,105,107,108,110,117,119,122,125,138,147,148,149,150,151,152,153,162,164,172,173,174,175,176,],[-104,-107,103,-1,-1,-1,-1,-101,-102,-103,-108,-109,-107,-105,-79,-81,-82,-84,-91,-93,-96,-99,-49,103,-1,-1,-1,-1,-1,-100,-48,-106,-80,-83,-92,-97,-98,]),'RBRACKET':([61,67,68,69,70,71,72,73,75,76,77,78,79,92,93,102,104,105,107,108,110,117,119,122,125,138,140,147,148,149,150,151,152,153,162,164,171,172,173,174,175,176,],[-104,100,101,-1,-1,-1,-1,-1,-101,-102,-103,-108,-109,-107,-105,-76,-78,-79,-81,-82,-84,-91,-93,-96,-99,-49,164,-1,-1,-1,-1,-1,-1,-100,-48,-106,-77,-80,-83,-92,-97,-98,]),'SINO':([81,198,],[-28,202,]),'CTES':([88,184,],[135,135,]),'ENTONCES':([157,179,180,],[-1,192,-62,]),'HASTA':([166,],[186,]),'HAZ':([185,194,195,],[-1,199,-71,]),'HACER':([196,200,],[-74,205,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'addMain':([4,],[5,]),'empty':([4,7,9,17,25,28,29,30,44,62,69,70,71,72,73,127,147,148,149,150,151,152,157,177,185,198,201,202,204,],[6,10,19,27,38,19,42,45,45,97,104,107,110,119,125,155,104,107,110,119,125,125,180,190,195,203,207,209,211,]),'vars':([5,144,167,],[7,169,187,]),'createTable':([7,],[9,]),'var2':([8,12,],[11,21,]),'var1':([8,12,],[12,12,]),'tipo':([8,12,20,99,168,],[13,13,32,146,146,]),'func_declarations':([9,28,],[17,40,]),'func_decl':([9,28,],[18,18,]),'lista_ids':([13,],[22,]),'var_decl':([13,35,],[23,66,]),'main':([17,],[25,]),'printfuncs':([17,],[26,]),'funcBody':([18,],[28,]),'bloque':([18,154,192,199,205,208,],[29,177,198,204,212,213,]),'func2':([20,],[31,]),'showstacks':([25,],[37,]),'endFunc':([29,],[41,]),'bloque1':([30,44,],[43,82,]),'estatuto':([30,44,],[44,44,]),'asig':([30,44,],[46,46,]),'cond':([30,44,],[47,47,]),'retorno':([30,44,],[48,48,]),'lectura':([30,44,],[49,49,]),'escritura':([30,44,],[50,50,]),'llamada':([30,36,44,58,74,85,86,88,95,103,106,109,118,123,124,139,141,156,184,],[51,77,51,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'repeticion':([30,44,],[52,52,]),'variable':([30,36,44,58,74,85,86,87,88,95,103,106,109,118,123,124,139,141,156,184,],[53,76,53,76,76,76,76,131,76,76,76,76,76,76,76,76,76,76,76,76,]),'iniciaLlamada':([30,36,44,58,74,85,86,88,95,103,106,109,118,123,124,139,141,156,184,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'condicional':([30,44,],[59,59,]),'nocondicional':([30,44,],[60,60,]),'func3':([31,],[64,]),'exp':([36,58,74,85,86,88,95,139,141,156,184,],[68,91,126,129,130,136,140,91,165,178,136,]),'texp':([36,58,74,85,86,88,95,103,139,141,156,184,],[69,69,69,69,69,69,69,147,69,69,69,69,]),'gexp':([36,58,74,85,86,88,95,103,106,139,141,156,184,],[70,70,70,70,70,70,70,70,148,70,70,70,70,]),'mexp':([36,58,74,85,86,88,95,103,106,109,139,141,156,184,],[71,71,71,71,71,71,71,71,71,149,71,71,71,71,]),'termino':([36,58,74,85,86,88,95,103,106,109,118,139,141,156,184,],[72,72,72,72,72,72,72,72,72,72,150,72,72,72,72,]),'factor':([36,58,74,85,86,88,95,103,106,109,118,123,124,139,141,156,184,],[73,73,73,73,73,73,73,73,73,73,73,151,152,73,73,73,73,]),'varcte':([36,58,74,85,86,88,95,103,106,109,118,123,124,139,141,156,184,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'addVar':([53,],[84,]),'llamada2':([58,139,],[89,163,]),'endLlamada':([58,89,],[90,137,]),'dimension':([61,132,],[93,93,]),'regWhile':([62,],[96,]),'exp1':([69,147,],[102,171,]),'texp1':([70,148,],[105,172,]),'gexp1':([71,149,],[108,173,]),'gexp2':([71,149,],[109,109,]),'mexp1':([72,150,],[117,174,]),'mexp2':([72,150,],[118,118,]),'termino1':([73,151,152,],[122,175,176,]),'escritura2':([88,184,],[133,193,]),'escritura1':([88,184,],[134,134,]),'params':([99,],[143,]),'param_decl':([99,168,],[145,188,]),'fillFirst':([127,],[154,]),'addAsig':([128,],[156,]),'addescritura':([134,],[161,]),'cond1':([157,],[179,]),'mergetables':([177,],[189,]),'genAsig':([178,],[191,]),'whileCond':([185,],[194,]),'createFor':([196,],[200,]),'elsePart':([198,],[201,]),'cond2':([201,],[206,]),'elseActions':([202,],[208,]),'endWhile':([204,],[210,]),'endFor':([212,],[214,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','scanner.py',260),
  ('programa -> PROGRAMA ID SEMICOLON addMain vars createTable func_declarations main showstacks','programa',9,'p_programa','scanner.py',271),
  ('addMain -> empty','addMain',1,'p_addMain','scanner.py',275),
  ('createTable -> empty','createTable',1,'p_createTable','scanner.py',282),
  ('vars -> VAR var2','vars',2,'p_vars','scanner.py',293),
  ('var1 -> tipo lista_ids SEMICOLON','var1',3,'p_var1','scanner.py',309),
  ('var2 -> var1 var2','var2',2,'p_var2','scanner.py',315),
  ('var2 -> var1','var2',1,'p_var2','scanner.py',316),
  ('var_decl -> ID','var_decl',1,'p_var_decl','scanner.py',326),
  ('var_decl -> ID LBRACKET CTEI RBRACKET','var_decl',4,'p_var_decl','scanner.py',327),
  ('var_decl -> ID LBRACKET exp RBRACKET','var_decl',4,'p_var_decl','scanner.py',328),
  ('lista_ids -> lista_ids COMMA var_decl','lista_ids',3,'p_lista_ids','scanner.py',355),
  ('lista_ids -> var_decl','lista_ids',1,'p_lista_ids','scanner.py',356),
  ('tipo -> INT','tipo',1,'p_tipo','scanner.py',370),
  ('tipo -> FLOAT','tipo',1,'p_tipo','scanner.py',371),
  ('tipo -> CHAR','tipo',1,'p_tipo','scanner.py',372),
  ('func_declarations -> func_decl funcBody func_declarations','func_declarations',3,'p_func_declarations','scanner.py',378),
  ('func_declarations -> empty','func_declarations',1,'p_func_declarations','scanner.py',379),
  ('func_decl -> FUNCION func2 func3 LPAREN params RPAREN vars','func_decl',7,'p_func_decl','scanner.py',382),
  ('func_decl -> FUNCION func2 func3 LPAREN RPAREN vars','func_decl',6,'p_func_decl','scanner.py',383),
  ('func_decl -> FUNCION func2 func3 LPAREN params RPAREN','func_decl',6,'p_func_decl','scanner.py',384),
  ('func_decl -> FUNCION func2 func3 LPAREN RPAREN','func_decl',5,'p_func_decl','scanner.py',385),
  ('funcBody -> bloque endFunc','funcBody',2,'p_funcBody','scanner.py',435),
  ('func3 -> ID','func3',1,'p_func3','scanner.py',438),
  ('func2 -> tipo','func2',1,'p_func2','scanner.py',445),
  ('func2 -> VOID','func2',1,'p_func2','scanner.py',446),
  ('endFunc -> empty','endFunc',1,'p_endFunc','scanner.py',450),
  ('bloque -> LCURLY bloque1 RCURLY','bloque',3,'p_bloque','scanner.py',459),
  ('bloque1 -> estatuto bloque1','bloque1',2,'p_bloque1','scanner.py',462),
  ('bloque1 -> empty','bloque1',1,'p_bloque1','scanner.py',463),
  ('estatuto -> asig','estatuto',1,'p_estatuto','scanner.py',468),
  ('estatuto -> cond','estatuto',1,'p_estatuto','scanner.py',469),
  ('estatuto -> retorno','estatuto',1,'p_estatuto','scanner.py',470),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','scanner.py',471),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','scanner.py',472),
  ('estatuto -> llamada SEMICOLON','estatuto',2,'p_estatuto','scanner.py',473),
  ('estatuto -> repeticion','estatuto',1,'p_estatuto','scanner.py',474),
  ('asig -> variable addVar EQUAL addAsig exp genAsig SEMICOLON','asig',7,'p_asig','scanner.py',479),
  ('addVar -> <empty>','addVar',0,'p_addVar','scanner.py',482),
  ('addAsig -> <empty>','addAsig',0,'p_addAsig','scanner.py',492),
  ('genAsig -> <empty>','genAsig',0,'p_genAsig','scanner.py',497),
  ('main -> printfuncs PRINCIPAL LPAREN RPAREN fillFirst bloque mergetables','main',7,'p_main','scanner.py',513),
  ('fillFirst -> empty','fillFirst',1,'p_fillFirst','scanner.py',517),
  ('param_decl -> tipo ID','param_decl',2,'p_param_decl','scanner.py',532),
  ('params -> params COMMA param_decl','params',3,'p_params','scanner.py',536),
  ('params -> param_decl','params',1,'p_params','scanner.py',537),
  ('retorno -> REGRESA LPAREN exp RPAREN SEMICOLON','retorno',5,'p_retorno','scanner.py',549),
  ('llamada -> iniciaLlamada llamada2 endLlamada RPAREN','llamada',4,'p_llamada','scanner.py',558),
  ('llamada -> iniciaLlamada endLlamada RPAREN','llamada',3,'p_llamada','scanner.py',559),
  ('iniciaLlamada -> ID LPAREN','iniciaLlamada',2,'p_iniciaLlamada','scanner.py',576),
  ('llamada2 -> exp COMMA llamada2','llamada2',3,'p_llamada2','scanner.py',591),
  ('llamada2 -> exp','llamada2',1,'p_llamada2','scanner.py',592),
  ('endLlamada -> <empty>','endLlamada',0,'p_endLlamada','scanner.py',600),
  ('lectura -> LEE LPAREN variable RPAREN SEMICOLON','lectura',5,'p_lectura','scanner.py',625),
  ('escritura -> ESCRIBE LPAREN escritura2 RPAREN SEMICOLON','escritura',5,'p_escritura','scanner.py',632),
  ('escritura1 -> CTES','escritura1',1,'p_escritura1','scanner.py',635),
  ('escritura1 -> exp','escritura1',1,'p_escritura1','scanner.py',636),
  ('escritura2 -> escritura1 addescritura COMMA escritura2','escritura2',4,'p_escritura2_a','scanner.py',640),
  ('escritura2 -> escritura1 addescritura','escritura2',2,'p_escritura2_a','scanner.py',641),
  ('addescritura -> <empty>','addescritura',0,'p_addescritura','scanner.py',644),
  ('cond -> SI LPAREN exp RPAREN cond1 ENTONCES bloque elsePart cond2','cond',9,'p_cond','scanner.py',656),
  ('cond1 -> empty','cond1',1,'p_cond1','scanner.py',659),
  ('cond2 -> empty','cond2',1,'p_cond2','scanner.py',671),
  ('elsePart -> SINO elseActions bloque','elsePart',3,'p_elsePart','scanner.py',677),
  ('elsePart -> empty','elsePart',1,'p_elsePart','scanner.py',678),
  ('elseActions -> empty','elseActions',1,'p_elseActions','scanner.py',681),
  ('repeticion -> condicional','repeticion',1,'p_repeticion','scanner.py',695),
  ('repeticion -> nocondicional','repeticion',1,'p_repeticion','scanner.py',696),
  ('condicional -> MIENTRAS regWhile LPAREN exp RPAREN whileCond HAZ bloque endWhile','condicional',9,'p_condicional','scanner.py',701),
  ('regWhile -> empty','regWhile',1,'p_regWhile','scanner.py',704),
  ('whileCond -> empty','whileCond',1,'p_whileCond','scanner.py',710),
  ('endWhile -> empty','endWhile',1,'p_endWhile','scanner.py',722),
  ('nocondicional -> DESDE ID EQUAL CTEI HASTA CTEI createFor HACER bloque endFor','nocondicional',10,'p_nocondicional','scanner.py',732),
  ('createFor -> <empty>','createFor',0,'p_createFor','scanner.py',735),
  ('endFor -> <empty>','endFor',0,'p_endFor','scanner.py',751),
  ('exp -> texp exp1','exp',2,'p_exp','scanner.py',783),
  ('exp1 -> OR texp exp1','exp1',3,'p_exp1','scanner.py',810),
  ('exp1 -> empty','exp1',1,'p_exp1','scanner.py',811),
  ('texp -> gexp texp1','texp',2,'p_texp','scanner.py',819),
  ('texp1 -> AND gexp texp1','texp1',3,'p_texp1','scanner.py',846),
  ('texp1 -> empty','texp1',1,'p_texp1','scanner.py',847),
  ('gexp -> mexp gexp1','gexp',2,'p_gexp','scanner.py',855),
  ('gexp1 -> gexp2 mexp gexp1','gexp1',3,'p_gexp1','scanner.py',883),
  ('gexp1 -> empty','gexp1',1,'p_gexp1','scanner.py',884),
  ('gexp2 -> LESS','gexp2',1,'p_gexp2','scanner.py',890),
  ('gexp2 -> LESSO','gexp2',1,'p_gexp2','scanner.py',891),
  ('gexp2 -> GREATER','gexp2',1,'p_gexp2','scanner.py',892),
  ('gexp2 -> GREATERO','gexp2',1,'p_gexp2','scanner.py',893),
  ('gexp2 -> NOTEQUAL','gexp2',1,'p_gexp2','scanner.py',894),
  ('gexp2 -> EQUALS','gexp2',1,'p_gexp2','scanner.py',895),
  ('mexp -> termino mexp1','mexp',2,'p_mexp','scanner.py',901),
  ('mexp1 -> mexp2 termino mexp1','mexp1',3,'p_mexp1','scanner.py',929),
  ('mexp1 -> empty','mexp1',1,'p_mexp1','scanner.py',930),
  ('mexp2 -> PLUS','mexp2',1,'p_mexp2','scanner.py',936),
  ('mexp2 -> MINUS','mexp2',1,'p_mexp2','scanner.py',937),
  ('termino -> factor termino1','termino',2,'p_termino','scanner.py',943),
  ('termino1 -> TIMES factor termino1','termino1',3,'p_termino1','scanner.py',972),
  ('termino1 -> DIVIDE factor termino1','termino1',3,'p_termino1','scanner.py',973),
  ('termino1 -> empty','termino1',1,'p_termino1','scanner.py',974),
  ('factor -> LPAREN exp RPAREN','factor',3,'p_factor','scanner.py',982),
  ('factor -> varcte','factor',1,'p_factor','scanner.py',983),
  ('factor -> variable','factor',1,'p_factor','scanner.py',984),
  ('factor -> llamada','factor',1,'p_factor','scanner.py',985),
  ('variable -> ID','variable',1,'p_variable','scanner.py',1016),
  ('variable -> ID dimension','variable',2,'p_variable','scanner.py',1017),
  ('dimension -> LBRACKET exp RBRACKET','dimension',3,'p_dimension','scanner.py',1053),
  ('varcte -> CTEI','varcte',1,'p_varcte','scanner.py',1060),
  ('varcte -> CTEF','varcte',1,'p_varcte','scanner.py',1061),
  ('varcte -> CTEC','varcte',1,'p_varcte','scanner.py',1062),
  ('mergetables -> empty','mergetables',1,'p_mergetables','scanner.py',1066),
  ('showstacks -> empty','showstacks',1,'p_showstacks','scanner.py',1099),
  ('printfuncs -> empty','printfuncs',1,'p_printfuncs','scanner.py',1118),
]
