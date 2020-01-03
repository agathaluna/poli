import do

def crossbar():
    N = int(input('Digite um valor para N: '))
    divisores = do.calculardivisores(N)
    n0 = (N/2)**(1/2)
    relaciona = {abs(divisor - n0): divisor for divisor in divisores}
    n = relaciona[min(relaciona)]
    k = (2*n)-1
    C = (k)*((2*N) + ((N/n)**2))
    print("O valor de n é: {} \nO valor de k é: {} \nO valor de cruzamento é: {}".format(n, k, C))

if __name__ == "__main__":
    crossbar()