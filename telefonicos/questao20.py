def main():
    a = 6
    M = 50
    h = a/M
    b = a
    bc = (h-b+b*h)/(b*h)
    print("A probabilidade de perdas é: {}".format(bc))
if __name__ == "__main__":
    main()
