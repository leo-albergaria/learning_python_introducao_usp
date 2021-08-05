
def n_primos(xNum):
  xI1 = 2
  xQtde = 0
  while xI1 <= xNum:
    xRange = range(2,xI1+1)
    i = 0
    xPrimo = True
    while i <= len(xRange)-1:  
       xd = xRange[i]
       if xI1%xd == 0 and xI1 != xd:
          xPrimo = False 
       i +=1
    if xPrimo:   
       xQtde +=1
    xI1 +=1   
  print (xQtde)
       

