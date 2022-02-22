def funcao(arg, arg2):
    return arg * arg2

var = funcao(2,2)
print(var)

#com lambda, a mesma expressão seria:

a = lambda x, y: x * y

print(a(2,2))