from Ejercicio_Nodos import NodoTernario


class Arbol:
    

    arbol1 = NodoTernario(20, NodoTernario(19, None, None, NodoTernario(67), None, None, NodoTernario(99)), NodoTernario(23, None, NodoTernario(57), None))

    print(arbol1.left.right.data)
