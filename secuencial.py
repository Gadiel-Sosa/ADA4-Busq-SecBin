def busqueda_secuencial(arreglo, elemento):
    posiciones = []
    for i in range(len(arreglo)):
        if arreglo[i] == elemento:
            posiciones.append(i)
    if posiciones:
        return f"Elemento '{elemento}' encontrado en las posiciones: {', '.join(map(str, posiciones))}."
    else:
        return f"Elemento '{elemento}' no encontrado."
arreglo = []
print("Ingresa los elementos del arreglo (palabras o números). Escribe 'fin' para terminar.")
while True:
    entrada = input("Elemento: ")
    if entrada.lower() == "fin":
        break
    arreglo.append(entrada)

if not arreglo:
    print("El arreglo está vacío. No se pueden realizar búsquedas.")
else:
    print("\nLista de elementos ingresados:")
    print(f"[{', '.join(arreglo)}]")  
    print("\nPuedes buscar elementos en el arreglo. Escribe 'fin' para terminar las búsquedas.")
    while True:
        entrada = input("Elemento a buscar: ")
        if entrada.lower() == "fin":
            print("Búsqueda finalizada. ¡Hasta luego!")
            break
        resultado = busqueda_secuencial(arreglo, entrada)
        print(resultado)
