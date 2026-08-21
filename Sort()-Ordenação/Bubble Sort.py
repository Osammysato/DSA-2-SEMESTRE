def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):      # j vai percorrer 1 número a frente do i
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [5, 3, 8, 2]
print(bubble_sort(numeros))