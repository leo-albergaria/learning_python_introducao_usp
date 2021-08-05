x = input("Digite um número inteiro: ")
xq = len(x)

xEn = "não"
for i in range(0,xq):
   if i+1 < len(range(0, xq)): 
      if x[i] == x [i+1]:
         xEn = "sim"
print (xEn)
