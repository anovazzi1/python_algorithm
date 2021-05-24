def MDC(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto
    return MDC(a, b) 


def main():
    x = input()
    x = x.split(" ")
    x = list(map(int,x))
    a = x[0]
    b= x[1]
    mdc = MDC(a,b)
    mmc = int((a* b)// mdc)
    print(mmc)

main()