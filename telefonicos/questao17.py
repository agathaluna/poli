def main():
    # -*- coding: latin-1 -*-
    n = 15
    h = 0.26
    a = n*h

    if a > 0 and a <= 0.9:
        print('O número de saídas é 4.')
    elif a > 0.9 and a <= 2.5:
        print('O número de saídas é 6.')
    elif a > 2.5 and a <= 4.1:
        print('O número de saídas é 8.')
    elif a > 4.1 and a <= 6:
        print('O número de saídas é 10.')
    elif a > 6 and a <= 11:
        print('O número de saídas é 15.')
    elif a > 11 and a <= 14:
        print('O número de saídas é 20.') 
    else:
        print('Valor não disponível no gráfico!')
if __name__ == "__main__":
    main()