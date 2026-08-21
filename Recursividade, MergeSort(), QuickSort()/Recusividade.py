# Recursividade
# Exemplo fatorial --> 5! = 5 x 4 x 3 x 2 x 1 = 120

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5))
print(fatorial(8))
print(fatorial(6))
print(fatorial(3))