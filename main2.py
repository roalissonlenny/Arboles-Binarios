from lib2 import *


arraynum=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nodoraiz = nodo( arraynum[0] )

for i in range(1, len(arraynum), 1):
    agreganodos(nodoraiz, arraynum[i])

#Otras formas de hacerlo :
#for i in arraynum:
 #   agreganodos(nodoraiz, i)

#j=1
#while arraynum:
#    agreganodos(nodoraiz, arraynum[j])
#    j+=1

printArbol( nodoraiz )

inOrderArr=[]
LVR (nodoraiz, inOrderArr)
print("InOrder:", end="")
print(inOrderArr)

postOrderArr=[]
LRV (nodoraiz, postOrderArr)
print("PostOrder:", end="")
print(postOrderArr)

preOrderArr=[]
VLR (nodoraiz, preOrderArr)
print("PreOrder:", end="")
print(preOrderArr)

print("............................")

arrnodos=[16,5,7,12,9,20,18,3,10,14]
nodoraiz = None

for i in range(0,len(arrnodos),1):
    if i == 0:
        nodoraiz = nodo( arrnodos[i] )
    else:
        nodosOrdenados( nodoraiz, nodo( arrnodos[i] ) )
    
    pass



printArbol( nodoraiz )

