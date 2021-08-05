def n_primos(xNum):
  xQtde = 0
  for xInput in range(2, xNum+1):
      xPrimo = True
      for xAchar in range(2, xInput+1):
          if xInput != xAchar:
             if xInput%xAchar == 0:
                xPrimo = False
      if xPrimo:
         xQtde += 1
  return (xQtde)
