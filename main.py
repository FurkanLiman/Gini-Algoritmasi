import agac
import gini
import ciz
import pandas as pd

Veri = gini.Veri
VeriS=gini.VeriS
Tablo1 = gini.Tablo1
basliklar = gini.basliklar
kategori = gini.kategori

total1 = []
for i in range(len(VeriS["SONUÇ"])):
    total1.append(i)

giniTablosu,kucuk = gini.Gini_hesapla(gini.kontrol(Veri,VeriS))
root = agac.TreeNode(kucuk[1], 124)
kategori = gini.kategori_yaz(Veri)
kucuk[0] = kategori[kucuk[1]]
total = [kucuk,total1]
agacim = agac.dugumle(total, root)

dot =agac.Digraph(comment="Tree")
agac.visualize_tree(root, dot)
dot.render('Agac_Gorsel/tree6', view=True)


dataframe2 = pd.read_excel('Egitim_Test_Verileri/test1.xlsx')
veritest,verisonuc = gini.dataframe_to_dict(dataframe2)

sonuclar = agac.yenidegerTest(veritest,agacim,VeriS)

dogru , yanlis = agac.karsilastir(verisonuc["SONUÇ"],sonuclar)

print(f"dogruluk oranı:{(dogru/(dogru+yanlis)):.3f}")



