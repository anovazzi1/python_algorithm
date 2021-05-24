def obter_fatorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        x = n * obter_fatorial(n-1)
        return x


def main():
    n = input()
    n = int(n)
    fatorial = obter_fatorial(n)
    print(fatorial)

main()