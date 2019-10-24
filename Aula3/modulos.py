import sys
import datetime
import json
from sys import builtin_module_names


def teste():
    return 'tentando...'


teste()

if len(sys.argv) == 2:
    print('O parâmetro passado fori {}'.format(sys.argv[1]))
if len(sys.argv) == 3:
    print('O parâmetro passado foi {}, {}'.format(sys.argv[1], sys.argv[2]))

# print(datetime.datetime.now())
# print(datetime.timedelta())
# print(datetime.time(14, 0, 0))
# print(datetime.date(2017, 1, 1)) # só aceita essa formatação


acesso = datetime.datetime(2018, 1, 22, 21, 00, 00)
atual = datetime.datetime.now()

print(acesso, atual)

print(json.dumps({'nome': 'python',
                  'modulos': 'fundamentals'
                  }))

string = '{"nome": "python"}'

print(json.loads(string))