#[(deger),[sol],[sağ]]
import gini






from graphviz import Digraph

class TreeNode:
    def __init__(self, value,count):
        self.value = value
        self.count = count  
        self.left = None
        self.right = None

def visualize_tree(root, dot=None):
    if dot is None:
        dot = Digraph()

   
    dot.node(f"{root.value}-{root.count}", label=f"{root.value}")

    if root.left:
       
        dot.edge(f"{root.value}-{root.count}", f"{root.left.value}-{root.left.count}", label=f' ≤{root.count}')
        visualize_tree(root.left, dot)

    if root.right:
   
        dot.edge(f"{root.value}-{root.count}", f"{root.right.value}-{root.right.count}", label=f'>{root.count}')
        visualize_tree(root.right, dot)











def datum(tree):
    return tree[0][0][0]

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


def dugumOlustur(datum, sol_agac_root=None, sag_agac_root=None):
    return [datum, sol_agac_root if sol_agac_root else [], sag_agac_root if sag_agac_root else []]






def dugumle(veri,root):
    verisol, verisag =[[None,None],None],[[None,None],None]
    if veri[1]==[]:
        pass
    else:
        
        verisol, verisag,kategori = gini.giniHesap(veri)
        if verisol[0] == [] or verisag[0] == []:
            indis = veri[1][0]
            root.value = gini.VeriS["SONUÇ"][indis]
            root.left = None
            root.right =None
        else:
            root.value = verisol[0][1]
            
            try:
                root.count = f"{kategori[verisol[0][1]]:.2f}"
            except:
                root.count = 0
            try:
                root.left = TreeNode(verisol[0][1],f"{kategori[verisol[0][1]]:.2f}")
            except:
                root.left = TreeNode(verisol[0][1],0)
            try:
                root.right = TreeNode(verisag[0][1],f"{kategori[verisag[0][1]]:.2f}")
            except:
                root.right = TreeNode(verisag[0][1],0)
            
    if verisol[1] !=None or verisag[1] !=None:    
        tree = dugumOlustur( veri, dugumle(verisol,root.left),dugumle(verisag,root.right))

        return tree


def yeniDeger(veri,agac,veris):
    #katmanları ayırna değişkenler (0.23436, 'HBG') gibi ayrılan katmanın kendinde olmalı alt katmanda değil hepsini değiş
    if veri[agac[0][1]][0] <= agac[0][2]:#eşik değeri içi değişecek
        yeniDeger(veri,agac[1])
    elif veri[agac[0][1]][0] > agac[0][2]:
        yeniDeger(veri,agac[2])
    print(veris["SONUÇ"][agac[1][0]])