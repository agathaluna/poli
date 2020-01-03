import numpy as np

def calculardivisores(num):
    n = np.arange(1,(num + 1))
    d = num % n
    resultado = d == 0
    return n[resultado]  

def newton(f, flin, m0, epsilon):
    if abs(f(m0))<= epsilon:
        return m0
    for i in range(1, 50):
        m1=m0-f(m0)/flin(m0)
        if abs(f(m1))<= epsilon or abs(flin(m1)) == 0:
            return m1
        m0 = m1
    print("ERRO: Número máximo de iterações atingido")
    return m1

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    return l

def fatorial(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat