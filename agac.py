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



def dugumOlustur(datum, sol_agac_root=None, sag_agac_root=None):
    return [datum, sol_agac_root if sol_agac_root else [], sag_agac_root if sag_agac_root else []]

def dugumle(veri,root):
    verisol, verisag =[[None,None],None],[[None,None],None]
    if veri[1]==[]:
        pass
    else:
        
        verisol, verisag,kategori = gini.giniHesap(veri)
        
        if verisol[1] == [] or verisag[1] == []:
            indis = veri[1][0]
            root.value = gini.VeriS["SONUÇ"][indis]
            
            root.left = None
            root.right =None
        else:
            root.value = veri[0][1]
            
            try:
                root.count = f"{veri[0][0]:.2f}"
            except:
                root.count = 0
            try:
                root.left = TreeNode(verisol[0][1],f"{verisol[0][0]:.2f}")
            except:
                root.left = TreeNode(verisol[0][1],0)
            try:
                root.right = TreeNode(verisag[0][1],f"{verisag[0][0]:.2f}")
            except:
                root.right = TreeNode(verisag[0][1],0)
        
    if verisol[0] == 'yes' or verisol[0] == 'no':
            return [verisol[0]]
    
    if verisol[1] !=[] or verisag[1] !=[]:
            tree = dugumOlustur( veri, dugumle(verisol,root.left),dugumle(verisag,root.right))

            return tree

def yeniDeger(veri,agac,veris):
    #veriler sözlüğünde dolaş
    
    if agac == ['yes'] or agac == ['no']:
        sonuc = agac
    else:
        if veri[agac[0][0][1]] <= agac[0][0][0]:#eşik değeri içi değişecek
            
            sonuc = yeniDeger(veri,agac[1],veris)
        elif veri[agac[0][0][1]] > agac[0][0][0]:
    
            sonuc = yeniDeger(veri,agac[2],veris)
    return sonuc

def yenidegerTest(veri,agac,veris):
    cevaplar = []
    for i in range(len(veri["RBC"])):
        tekdeger = {}
        for j in veri:
            tekdeger[j] = veri[j][i]
        cevaplar.append(yeniDeger(tekdeger,agac,veris))
    return cevaplar

def karsilastir(Veris, sonuclar):
    dogru = 0
    yanlis = 0
    for i in range(len(Veris)):
        if Veris[i] == sonuclar[i][0]:
            dogru +=1
        else:
            yanlis +=1
    print("dogru : ",dogru)
    print("yanlis: ", yanlis)
    return dogru,yanlis