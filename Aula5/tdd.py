import unittest


# def fun(x):
#     return x + 1



# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(fun(3), 7)

# if __name__ == '__main__':
#     unittest.main()


def soma(x, y):
    return x + y

def subtrai(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiplica(x, y):
    return x * y



class Testes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(5, 2), 7, msg=f'falha na soma')
        self.assertTrue(soma(1, 2) != soma(2,2), msg='Função incorreta')

    def test_sub(self):
        self.assertEqual(subtrai(5, 2), 3, msg=f'falha na subtração')
    
    def test_div(self):
        self.assertEqual(divide(5, 2), 2.5, msg=f'falha na divisão')
    
    def test_mult(self):
        self.assertEqual(multiplica(5, 2), 10, msg=f'falha na multiplicação')


if __name__ == "__main__":
    unittest.main()


    