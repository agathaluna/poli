import do

err = 0.0001

def f(m):
    return -12*(m**8) + 6*(m**7) + (4*N-2)*(m**6) - 6*N*(m**5) + 2*N*(m**4) - (N**2)*(m**3) + 3*(N**2)*(m**2) - 3*(N**2)*m + N**2 + 4

def df(m):
    return -96*(m**7) + 42*(m**6) + (24*N-12)*(m**5) - 30*N*(m**4) + 8*N*(m**3) - 3*(N**2)*(m**2) + 6*(N**2)*m - 3*(N**2)

def crossbar():
    divisores = do.calculardivisores(N)
    x0 = 0
    lista_clos = []
    lista_n = []
    lista_m = []
    for i in range(0, 50):
        raiz = do.newton(f,df,x0,err)
        relaciona_m = {abs(divisor - raiz): divisor for divisor in divisores}
        m = relaciona_m[min(relaciona_m)]
        n0 = (N * (m -1))/(2 * (m**3))
        relaciona_n = {abs(divisor - n0): divisor for divisor in divisores}
        n = relaciona_n[min(relaciona_n)]
        clos = (2 * n - 1) *(2*N + (2 * m - 1) * (((2*N)/n) + ((N**2)/((n**2) * (m**2)))))
        lista_clos.append(clos)
        lista_n.append(n)
        lista_m.append(m)
        x0 = x0 + 1
    cruzamentos = do.remove_repetidos(lista_clos)
    menor_cruzamento = min(cruzamentos)
    posicao = cruzamentos.index(menor_cruzamento)
    inteiro = int(posicao)
    n_lista = do.remove_repetidos(lista_n)
    m_lista = do.remove_repetidos(lista_m)
    n = n_lista[posicao]
    m = m_lista[posicao]
    print("O menor número de cruzamentos é: {}\nO m ótimo é: {}\nO n ótimo é: {}\n".format(menor_cruzamento, m, n))

if __name__ == "__main__":
    N = int(input('Digite um valor para N: '))
    crossbar()
