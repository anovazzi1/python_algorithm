def achar_maximo (t, lista):
   if (t == 1): 
       x = lista[0]
   else:
      x = achar_maximo (t-1, lista)
      if (x < lista[t-1]): x = lista[t-1]
   return x

def main():
    valores = input()
    valores = valores.split(" ")
    valores = list(map(int,valores))
    t = len(valores)
    max = achar_maximo(t, valores)
    print(max)
main()