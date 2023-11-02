import cv2
import numpy as np
import agac
from copy import deepcopy

space = np.zeros([1000,1000,3],dtype=np.uint8)

def ciz(tree):
    seviye = agac.height(tree)
    en = agac.width(tree)
    preorder_traversal(tree,space,0,0)
    sonc = breadth_first_traversal(tree)
    print(sonc)
    part = space.shape[1]//seviye
    for i in range(seviye):
        space[part*i-10] = 255

    cv2.imshow("space",space)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def preorder_traversal(tree,space,katman,yatay):
    if not bos_mu(tree):
        print(datum(tree))
        katman+=1
        cv2.putText(space,str(datum(tree)),(500-(yatay*150),katman*150),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
        cv2.circle(space,(500-(yatay*150),katman*150),100,(255,255,255),2)
        preorder_traversal(sol_agac(tree),space,katman,yatay-1)
        preorder_traversal(sag_agac(tree),space,katman,yatay+1)
        
def sol_agac(tree):
    if bos_mu(tree):
        return []
    return tree[1]

def sag_agac(tree):
    if bos_mu(tree):
        return []
    return tree[2]

def bos_mu(tree):
    return tree == []

def datum(tree):
    return tree[0]

def breadth_first_traversal(tree):
    queue = deepcopy(tree)
    sonuc = []
    derinlik = 0
    while len(queue) > 0:
        if type(queue[0]) != list:
            a = queue.pop(0)
            sonuc.append(a)
            print(a)
        else:
            queue.extend(queue.pop(0))
            print(sonuc)


    return sonuc