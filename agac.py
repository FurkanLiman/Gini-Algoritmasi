#[(deger),[sol],[sağ]]
import gini

def datum(tree):
    return tree[0]

def bos_mu(tree):
    return tree == []
# leaf node ornegi: [4, [], []]
def isleaf(tree):
    return sol_agac(tree) == [] and sag_agac(tree) == []

def height(tree):
    if bos_mu(tree):
        return 0
    return 1 + max(height(sol_agac(tree)), height(sag_agac(tree)))

def width_list(tree):
    her_bir_derinlikteki_dugum_sayilari = height(tree) * [0]
    def listeye_ekle(tree, derinlik=0):
        if not bos_mu(tree):
            her_bir_derinlikteki_dugum_sayilari[derinlik] += 1
            listeye_ekle(sol_agac(tree), derinlik+1)
            listeye_ekle(sag_agac(tree), derinlik+1)
    listeye_ekle(tree)
    return her_bir_derinlikteki_dugum_sayilari

def width(tree):
    return max(width_list(tree))


def preorder_traversal(tree):
    if not bos_mu(tree):
        print(datum(tree))
        preorder_traversal(sol_agac(tree))
        preorder_traversal(sag_agac(tree))


# ornek agac: [deger, sol_agac, sag_agac]
def sol_agac(tree):
    if bos_mu(tree):
        return []
    return tree[1]

def sag_agac(tree):
    if bos_mu(tree):
        return []
    return tree[2]


def dugumOlustur(datum, sol_agac=None, sag_agac=None):
    return [datum, sol_agac if sol_agac else [], sag_agac if sag_agac else []]


def dugumle(veri):
    verisol,verisag = None,None
    if veri==[]:
        pass
    else:
        verisol, verisag = gini.giniHesap(veri)
    if verisol !=None or verisag !=None:    
        tree = dugumOlustur(veri, dugumle(verisol),dugumle(verisag))
        return tree

