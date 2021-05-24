'''formula da torre de hanoi = 2^n -1'''
def hanoi(n):
    if n ==0:
        return 1
    if n == 1:
        return 2
    else:
        x = 2* hanoi(n-1)
        return x

def main():
    n = input()
    n = int(n)
    movimentos = hanoi(n)
    movimentos = movimentos-1
    print(movimentos)

main()