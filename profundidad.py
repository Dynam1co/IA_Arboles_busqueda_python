from arbol import Nodo


def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()  # Extraer nodo a visitar
        nodos_visitados.append(nodo)  # Añadir a nodos visitados

        # Solo debemos comprobar que en la jarra grande hayan 4 litros
        if nodo.get_datos()[0] == solucion[0]:
            solucionado = True

            # Devuelvo el último nodo (meta) que tiene un padre, que a su vez tiene otro padre etc y ese sería el camino a la solución
            return nodo
        else:  # Expandir hijos
            dato_nodo = nodo.get_datos()

            # Llenar grande
            hijo = [5, dato_nodo[1]]

            hijo_1 = Nodo(hijo)

            if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_1)

            # Llenar pequeña
            hijo = [dato_nodo[0], 3]

            hijo_2 = Nodo(hijo)

            if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_2)

            # Vaciar grande
            hijo = [0, dato_nodo[1]]

            hijo_3 = Nodo(hijo)

            if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_3)

            # Vaciar pequeña
            hijo = [dato_nodo[0], 0]

            hijo_4 = Nodo(hijo)

            if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_4)

            # Traspasar grande-pequeña
            actual_grande = dato_nodo[0]
            actual_peque = dato_nodo[1]
            fin_grande = actual_grande
            fin_peque = actual_peque

            puedo_traspasar = 3 - actual_peque

            if puedo_traspasar > 0:
                if actual_grande <= puedo_traspasar:                    
                    fin_peque = actual_peque + fin_grande
                    fin_grande = 0

                    if fin_peque > 3:
                        fin_peque = 3
                else:
                    fin_peque = puedo_traspasar + actual_peque
                    fin_grande = actual_grande - puedo_traspasar

            hijo = [fin_grande, fin_peque]

            hijo_5 = Nodo(hijo)

            if not hijo_5.en_lista(nodos_visitados) and not hijo_5.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_5)

            # Traspasar pequeña-grande
            actual_grande = dato_nodo[0]
            actual_peque = dato_nodo[1]
            fin_grande = actual_grande
            fin_peque = actual_peque

            puedo_traspasar = 5 - actual_grande

            if puedo_traspasar > 0:
                if actual_peque <= puedo_traspasar:                    
                    fin_grande = actual_grande + fin_peque
                    fin_peque = 0

                    if fin_grande > 5:
                        fin_grande = 5
                else:
                    fin_grande = puedo_traspasar + actual_grande
                    fin_peque = actual_peque - puedo_traspasar

            hijo = [fin_grande, fin_peque]

            hijo_6 = Nodo(hijo)

            if not hijo_6.en_lista(nodos_visitados) and not hijo_6.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_6)

            nodo.set_hijos([hijo_1, hijo_2, hijo_3, hijo_4, hijo_5, hijo_6])


if __name__ == '__main__':
    estado_inicial = [0, 0]
    solucion = [4, 3]

    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    # Creo una lista de todos los padres del nodo solución
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    print(resultado)