#!usr/bin/python3
from behave import step, when


def soma(x, y):
    return x + y



@when(u'somar "{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))

@step('O resultado deve ser "{esperado}"')
def test_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "Erro"
