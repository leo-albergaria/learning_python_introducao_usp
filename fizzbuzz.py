x = int(input("Digite um número: "))

if (x % 3 == 0) and ((x % 5 == 0) or (x % 5 == 5)):
    print("FizzBuzz")
else:
    print(x)
    
