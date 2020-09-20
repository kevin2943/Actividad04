def factorial(n):
    if(n < 0):
        raise Exception("No existe factorial negativo")
    if(n == 1 or n == 0):
        return 1
    return factorial(n-1)*n


def calc(limite):
    n = 0
    e = 0
    while(n <= limite):
        e += 1.0/factorial(n)
        n += 1
    return e

limite = int(input("Limite superior: "))
print("{:f}".format(calc(limite)))