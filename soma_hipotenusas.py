def soma_hipotenusas (z):
  xQtde = 0 
  for i in range(1, z+ 1):
     xSoma = é_hipotenusa(i)
     if xSoma:
         xQtde += i
  return (xQtde) 
               
def é_hipotenusa(x):
    y = x ** 2
    xReturn = False
    for x1 in range(1,x+1):
        for y1 in range(1,x+1):
            if y == x1**2 + y1**2:
                xReturn = True
                break
    return xReturn
        

