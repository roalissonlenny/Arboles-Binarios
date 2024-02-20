def LVR( nodo, inOrderArr ):
    if nodo is not None:
        nodopadre = nodo
        LVR ( nodopadre.Izq, inOrderArr )
        inOrderArr.append( nodopadre.valor )
        LVR ( nodopadre.Der, inOrderArr )
        
    return inOrderArr
    
def linkhijo( nodopadre, nodohijoIzq=None, nodohijoDer=None ):
    if nodohijoIzq is not None:
        nodopadre.Izq = nodohijoIzq

    if nodohijoDer is not None:    
        nodopadre.Der = nodohijoDer
    
    pass

#Proyecto-Se puede usar recursividad 