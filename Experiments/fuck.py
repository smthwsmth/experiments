def get_operator(operator):
    def run_operator(y):
        if callable(y):
            y = y()
        def doit(x):
            nonlocal y
            return eval(operator)
        return doit
    return run_operator

plus = get_operator('x + y')
minus = get_operator('x - y')
multiply = get_operator('x * y')
division = get_operator('x / y')

def get_digit(n):
    def digit(instruction=None):
        if instruction:
            return instruction(n)
        else:
            return n
    return digit

zero =   get_digit(0)
one =    get_digit(1)
two =    get_digit(2)
three =  get_digit(3)
four =   get_digit(4)
five =   get_digit(5)
six =    get_digit(6)
seven =  get_digit(7)
eight =  get_digit(8)
nine =   get_digit(9)

# Теперь можем писать простые вычисления функциями ;-)
a = one(plus(three))              # последнюю функцию можно передать без скобок
b = eight(division(five()))     # а можно и со скобками
c = nine(multiply(four))

print(a)  # 4
print(b)  # 1.6
print(c)  # 36