numero=input()
capicuia = list(numero)
if capicuia[0] == capicuia[-1] or capicuia[1] == capicuia[-2] and capicuia[0] == capicuia[-1] :
     print("sim")
else:
    print("não")