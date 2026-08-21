def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = merge_sort(esquerda)
    direita = merge_sort(direita)

    return merge(esquerda, direita)


def merge(esquerda, direita):
    # 'esquerda' e 'direita' são as duas metades que vamos juntar.

    # Cria uma lista vazia, como se fosse uma caixa nova, para ir
    # guardando os números na ordem certa, um por um.
    resultado = []

    # 'i' é como se fosse o seu dedo apontando para a primeira carta do monte da 'esquerda'.
    # Começa no zero porque em programação, a primeira posição é a zero.
    i = 0

    # 'j' é o seu outro dedo apontando para a primeira carta do monte da 'direita'.
    j = 0

    # Enquanto o dedo 'i' não chegar no fim do monte da esquerda
    # E (and) o dedo 'j' não chegar no fim do monte da direita...
    # (ou seja, enquanto tiver carta nos dois montes pra comparar)
    while i < len(esquerda) and j < len(direita):

        # Você olha para as duas cartas que está apontando.
        # A carta do monte da esquerda é MENOR ou IGUAL a do monte da direita?
        if esquerda[i] <= direita[j]:

            # Se for, você pega essa carta da esquerda e coloca na sua caixa de 'resultado'.
            resultado.append(esquerda[i])

            # E avança o dedo da esquerda para apontar para a próxima carta daquele monte.
            i += 1

        else:
            # Se a carta da direita for a menor de todas...

            # Você pega a carta da direita e coloca na sua caixa de 'resultado'.
            resultado.append(direita[j])

            # E avança o dedo da direita para apontar para a próxima carta daquele monte.
            j += 1

    # Quando o bloco 'while' acima terminar, significa que as cartas de UM
    # dos montes acabaram. Mas o outro monte ainda tem cartas sobrando!

    # Se o monte da direita acabou primeiro, pega TUDO que sobrou no
    # monte da esquerda (do ponto onde o dedo 'i' parou até o final) e joga na caixa.
    resultado.extend(esquerda[i:])

    # Se foi o monte da esquerda que acabou primeiro, pega TUDO que
    # sobrou no da direita (do ponto onde o dedo 'j' parou até o final) e joga na caixa.
    # Nota: Apenas um desses dois 'extends' vai realmente adicionar algo,
    # porque um dos montes já estará vazio.
    resultado.extend(direita[j:])

    # Por fim, entrega a caixa com todos os números juntos e ordenados!
    return resultado


# --- Código para conferir o resultado ---

# 1. Crie uma lista de teste desordenada
numeros = [38, 27, 43, 3, 9, 82, 10]

# 2. Imprima a lista original
print("Lista original:", numeros)

# 3. Chame a função passando a lista e guarde o resultado
numeros_ordenados = merge_sort(numeros)

# 4. Imprima o resultado final
print("Lista ordenada:", numeros_ordenados)

