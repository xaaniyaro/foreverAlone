resultsArith = {
            ('int','int') : 'int',
            ('int','float') : 'float',
            ('int','char') : 'err',
            ('int', 'bool') : 'err',
            ('float', 'float') : 'float',
            ('float','bool') : 'err',
            ('float', 'char') : 'err',
            ('bool', 'bool') : 'err',
            ('bool','char') : 'err',
            ('char','char') : 'ctes'
            }

resultsLogic = {
            ('int','int') : 'bool',
            ('int','float') : 'bool',
            ('int','char') : 'err',
            ('int', 'bool') : 'err',
            ('float', 'float') : 'bool',
            ('float','bool') : 'err',
            ('float', 'char') : 'err',
            ('bool', 'bool') : 'bool',
            ('bool','char') : 'err',
            ('char','char') : 'bool'
        }

operations = {'+' : resultsArith,
              '-' : resultsArith,
              '*' : resultsArith,
              '/' : resultsArith,
              '&' : resultsLogic,
              '|' : resultsLogic,
              '>' : resultsLogic,
              '<' : resultsLogic,
              '>=' : resultsLogic,
              '<=' : resultsLogic,
              '==' : resultsLogic,
              '!=' : resultsLogic
            }