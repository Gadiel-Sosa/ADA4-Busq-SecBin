def busqueda_binaria(arreglo, objetivo):
    izquierda = 0
    derecha = len(arreglo) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arreglo[medio] == objetivo:
            return f"Elemento {objetivo} encontrado en la posición {medio}."
        elif arreglo[medio] > objetivo:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return f"Elemento {objetivo} no encontrado."

arreglo = []
print("Ingresa los elementos para el arreglo (números). Escribe 'fin' para terminar.")

while True:
    entrada = input("Elemento: ")
    if entrada.lower() == 'fin':
        break
    try:
        arreglo.append(int(entrada))  
    except ValueError:
        print("Por favor, ingresa un número válido.")

if arreglo:
    arreglo.sort()
    print(f"Arreglo ordenado: {arreglo}")
    while True:
        objetivo = input("Ingresa el número a buscar (o escribe 'fin' para salir): ")
        
        if objetivo.lower() == 'fin':
            print("Búsqueda finalizada. ¡Hasta luego!")
            break
        
        try:
            objetivo = int(objetivo) 
            resultado = busqueda_binaria(arreglo, objetivo)
            print(resultado)
        except ValueError:
            print("Por favor, ingresa un número válido para la búsqueda.")
else:
    print("No se han ingresado elementos al arreglo. No se puede realizar la búsqueda.")
