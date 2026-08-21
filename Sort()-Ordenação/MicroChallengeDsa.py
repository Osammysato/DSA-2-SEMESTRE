import random

# ----- Sorteia o vetor de 200 elementos -----
TAMANHO = 200
vetor_original = [random.randint(1, 1000) for _ in range(TAMANHO)]

def bubble_sort(lista):
    trocas = 0
    n = len(lista)
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
    return lista, trocas


def insertion_sort(lista):
    trocas = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            j -= 1
            trocas += 1

        lista[j + 1] = atual
    return lista, trocas


def selection_sort(lista):
    trocas = 0
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]  # troca só uma vez, no final
            trocas += 1
    return lista, trocas


vetor_bubble = vetor_original.copy()
vetor_insertion = vetor_original.copy()
vetor_selection = vetor_original.copy()

_, trocas_bubble = bubble_sort(vetor_bubble)
_, trocas_insertion = insertion_sort(vetor_insertion)
_, trocas_selection = selection_sort(vetor_selection)

print("Quantidade de trocas em cada método (vetor de 200 elementos):")
print(f"Bubble Sort:    {trocas_bubble} trocas")
print(f"Insertion Sort: {trocas_insertion} trocas")
print(f"Selection Sort: {trocas_selection} trocas")