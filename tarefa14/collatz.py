count = 0
    
def conjectura(n):
    global count
    if n == 1:
        return count
    if n % 2==0:
        count += 1
        n = conjectura(n/2)
        return n
    if n %2 != 0:
        count += 1
        n = conjectura(((n*3)+1)/2)
        return n


def main():
    n = input()
    n = int(n)
    collatz = conjectura(n)
    print(collatz)

main()