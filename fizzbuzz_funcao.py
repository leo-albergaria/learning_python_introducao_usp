def fizzbuzz (x):

   if (x % 3 == 0) and (x % 5 != 0):
      xreturn = "Fizz"                  
   else:
       if (x % 5 == 0) and (x % 3 != 0):
          xreturn = "Buzz"                  
       else:
          if (x % 3 == 0) and (x % 5 == 0):
            xreturn = "FizzBuzz"
          else:
            xreturn = x
   return xreturn
