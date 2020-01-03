import do

def lee():
    opcao = int(input('Escolha uma das opções:\n- Cruzamentos SEM bloqueio (1)\n- Cruzamentos COM bloqueio (2): '))
    while opcao != 1 and opcao !=2:
        print("ERRO: Escolha uma opção válida")
        opcao = int(input('Escolha uma das opções:\n- Cruzamentos SEM bloqueio (1)\n- Cruzamentos COM bloqueio (2): '))
    if opcao == 1:
        N = int(input('Digite um valor para N: '))
        divisores = do.calculardivisores(N)
        n0 = (N/2)**(1/2)
        relaciona = {abs(divisor - n0): divisor for divisor in divisores}
        n = relaciona[min(relaciona)]
        k = (2*n)-1
        C = (k)*((2*N) + ((N/n)**2))
        print("O valor de n é: {} \nO valor de k é: {} \nO valor de cruzamento é: {}".format(n, k, C))
    if opcao == 2:
        N = int(input('Digite um valor para N: '))
        n = int(input('Digite um valor para n: '))
        p = float(input('Digite um valor para p: '))
        P = float(input('Digite um valor para P: '))
        k = int(input('Digite um valor para k: '))
        B = k/n
        C = (k)*((2*N) + ((N/n)**2))
        print("O valor de cruzamento é: {}\nO valor de B é: {}".format(C, B))

if __name__ == "__main__":
    lee()