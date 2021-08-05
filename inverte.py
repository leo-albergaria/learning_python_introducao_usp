x = 1
xLista = []
while x !=0:
   x = int(input("Digite um número: "))
   if x !=0:
      xLista.append(x)
    
for i in range(len(xLista)-1, -1, -1):
    print (xLista[i])
