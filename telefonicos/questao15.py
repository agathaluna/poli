import do
def main():
    a = 15.2
    c = 20

    a = 15.2
    repeticoes = c + 1

    x = a**c 
    y = do.fatorial(c) 

    for i in range(1,repeticoes):
        z = (a**i)/(do.fatorial(i))
        E = (x/y)/z
        print("O tráfego rejeitado no {} é {}".format(i, E))
        if i == 11:
            ml = a*(1-E)
            print("O tráfego carregado pelo décimo tronco é {}".format(ml))

if __name__ == "__main__":
    main()
