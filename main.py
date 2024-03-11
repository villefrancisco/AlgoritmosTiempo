import random
import time

def insertionSort(lista):
    for i in range (1, len(lista)):
        val = lista[i]
        j = i-1
        while j >= 0 and val < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = val
    return lista

def selectionSort(lista):
    for i in range(0, len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

def bubbleSort(lista):
    for i in range(1, len(lista)-1):
        for j in range(0, len(lista)-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

        return lista

    # Heap Sort in python


def heapify(lista, n, i):
    mayor = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lista[i] < lista[l]:
        mayor = l

    if r < n and lista[mayor] < lista[r]:
        mayor = r

    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


def heapSort(lista):
    n = len(lista)
    for i in range(n // 2, -1, -1):
        heapify(lista, n, i)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

    return lista


def particion(lista, menor, mayor):
    pivote = lista[mayor]
    i = menor - 1
    for j in range(menor, mayor):
        if lista[j] <= pivote:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[mayor] = lista[mayor], lista[i + 1]
    return i + 1


def quickSort(lista, indicemenor, indicemayor):
    if indicemenor < indicemayor:
        pivote = particion(lista, indicemenor, indicemayor)
        quickSort(lista, indicemenor, pivote - 1)
        quickSort(lista, pivote + 1, indicemayor)
    return lista

if __name__ == '__main__':
    size_of_n = [10, 100, 1000, 10000, 100000]
    for n in size_of_n:
        print("El valor de n: ", n)
        lista = random.sample(range(1, n+1), n)
        inicio = time.time()
        sorted_lista = insertionSort(lista)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Insertion Sort: ", tiempo_transcurrido)

        lista = random.sample(range(1, n + 1), n)
        inicio = time.time()
        sorted_lista = selectionSort(lista)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Selection Sort: ", tiempo_transcurrido)

        lista = random.sample(range(1, n + 1), n)
        inicio = time.time()
        sorted_lista = bubbleSort(lista)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Bubble Sort: ", tiempo_transcurrido)

        lista = random.sample(range(1, n + 1), n)
        inicio = time.time()
        sorted_lista = mergeSort(lista)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Merge Sort: ", tiempo_transcurrido)

        lista = random.sample(range(1, n + 1), n)
        inicio = time.time()
        sorted_lista = heapSort(lista)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Heap Sort: ", tiempo_transcurrido)

        lista = random.sample(range(1, n + 1), n)
        inicio = time.time()
        sorted_lista = quickSort(lista, 0, n-1)
        fin = time.time()
        tiempo_transcurrido = fin - inicio
        print("Tiempo Quick Sort: ", tiempo_transcurrido)