

x = int(input("Escreva um número: "))

def is_prime(x):
    if x != 0 & x != 1 :
        if x > 3 :
           for i in range(2, x):
              if x % i == 0 :
                 return False
        return True
    return False

print(is_prime(x))