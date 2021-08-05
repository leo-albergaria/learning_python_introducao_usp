def vogal (x):
   xVogais = "AEIOU" 
   xr = False
   for i in range(5):
      if xVogais[i] == x.upper():
         xr = True

   return (xr)
