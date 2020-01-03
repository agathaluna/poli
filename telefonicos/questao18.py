def main():
    a = 2
    M = 10
    h = a/M
    b = a
    bc = (h-b+b*h)/(b*h)
    print("A probabilidade de perdas é: {}".format(bc))
if __name__ == "__main__":
    main()