def buscar_elemento(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1  # Retorna -1 se o elemento não for encontrado