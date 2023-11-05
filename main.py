import agac
import gini
import ciz

Veri = gini.Veri
VeriS=gini.VeriS
Tablo1 = gini.Tablo1
basliklar = gini.basliklar
kategori = gini.kategori

total1 = []
for i in range(len(VeriS["SONUÇ"])):
    total1.append(i)
total = ["",total1]

root = agac.TreeNode("bas", 0)

agacim = agac.dugumle(total, root)

dot =agac.Digraph(comment="Tree")
agac.visualize_tree(root, dot)
dot.render('tree', view=True)

print(kategori)

