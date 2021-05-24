resp = {0:0,1:1,2:2,}

def obter_fibonacci(n):
    if n > 2 and n not in resp:
        x = obter_fibonacci(n-1) + obter_fibonacci(n-2) + obter_fibonacci(n-3)
        resp[n] = x
        return x
    return resp[n]


def main():
    n = input()
    n = int(n)
    fibonacci = obter_fibonacci(n)
    print(fibonacci)

main()
