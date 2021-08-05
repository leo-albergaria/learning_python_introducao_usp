x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

for i in range (0, y):

     for ii in range (0, x):
        if (ii >= 1 and ii <= x-2) and (i == 1):
           print (" ", end="")
        else:
           print ("#", end="")
           
     print("")

        
