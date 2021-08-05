import math

x1 = int(input("Digite um número x1: "))
y1 = int(input("Digite um número y1: "))
x2 = int(input("Digite um número x2: "))
y2 = int(input("Digite um número y2: "))

dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if dist >= 10:
    print ("longe")
else:
    print ("perto")

