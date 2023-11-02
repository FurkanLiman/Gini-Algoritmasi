Veri = {
    "hava" :    ["güneşli","güneşli","bulutlu","yağmurlu","yağmurlu","yağmurlu","bulutlu","güneşli","güneşli","yağmurlu","güneşli","bulutlu","bulutlu","yağmurlu"],
    "ısı" :     ["sıcak","sıcak","sıcak","ılık","soğuk","soğuk","soğuk","ılık","soğuk","ılık","ılık","ılık","sıcak","ılık"],
    "nem":      ["yüksek","yüksek","yüksek","yüksek","normal","normal","normal","yüksek","normal","normal","normal","yüksek","normal","yüksek"],
    "rüzgar":   ["hafif","kuvvetli","hafif","hafif","hafif","kuvvetli","kuvvetli","hafif","hafif","hafif","kuvvetli","kuvvetli","hafif","kuvvetli"],
}
VeriS={"oyun":     ["hayır","hayır","evet","evet","evet","hayır","evet","hayır","evet","evet","evet","evet","evet","hayır"]}


Tablo1 = {
    "evet" : [],
    "hayır": [],
    "giniSS":[]
}

#ikili ayırmalar= güneşli,bulutlu/yağmurlu  | sıcak,ılık/soğuk 
#kategorinin değişken adı 2 uzunluklu olamaz örn "hava":["as","selam"]
basliklar = []
kategori = {
    "hava":[["güneşli","bulutlu"],"yağmurlu"],
    "ısı" :[["sıcak","ılık"], "soğuk"],
    "nem" :["yüksek","normal"],
    "rüzgar":["hafif","kuvvetli"]
    
    }

for i in Veri:
    basliklar.append(i)


def kontrol(Veri,VeriS):
    Tablo = tablo_olustur()
    for indis in range(len(VeriS["oyun"])):
        for baslik in Veri:
            if len(kategori[baslik][0])==2:
                if Veri[baslik][indis] == kategori[baslik][0][0] or Veri[baslik][indis] == kategori[baslik][0][1]:
                    if VeriS["oyun"][indis]=="evet":
                        Tablo[baslik][f"{kategori[baslik][0]}"]["evet"] +=1
                    else:
                        Tablo[baslik][f"{kategori[baslik][0]}"]["hayır"] +=1
                elif Veri[baslik][indis] == kategori[baslik][1]:
                    if VeriS["oyun"][indis]=="evet":
                        Tablo[baslik][f"{kategori[baslik][1]}"]["evet"] +=1
                    else:
                        Tablo[baslik][f"{kategori[baslik][1]}"]["hayır"] +=1
            elif len(kategori[baslik][0])!=2:
                if Veri[baslik][indis] == kategori[baslik][0]:
                    if VeriS["oyun"][indis]=="evet":
                        Tablo[baslik][kategori[baslik][0]]["evet"] +=1
                    else:
                        Tablo[baslik][kategori[baslik][0]]["hayır"] +=1
                elif Veri[baslik][indis] == kategori[baslik][1]:
                    if VeriS["oyun"][indis]=="evet":
                        Tablo[baslik][kategori[baslik][1]]["evet"] +=1
                    else:
                        Tablo[baslik][kategori[baslik][1]]["hayır"] +=1
                        
    return Tablo

def tablo_olustur():
    Tablo = {}
    for baslik in Veri:
        Tablo[baslik] = {f"{kategori[baslik][0]}":{"evet":0,"hayır":0},kategori[baslik][1]:{"evet":0,"hayır":0}}
    return Tablo


def Gini_hesapla(Tablo):
    giniSSTablosu = {}
    giniTablosu = {}
    for i in Tablo:
        giniss = {}
        for j in range(2):
            degerler = Tablo[i][f"{kategori[i][j]}"]
            evet= degerler["evet"]
            hayir= degerler["hayır"]
            try:

                gini = 1 - ( ((evet/(evet+hayir))**2) + ((hayir/(evet+hayir))**2))
            except:
                gini = 2
            giniss[str(j)] = gini
            giniSSTablosu[i] = giniss

    for i in giniSSTablosu:
        
        toplamSol = Tablo[i][f"{kategori[i][0]}"]["evet"] + Tablo[i][f"{kategori[i][0]}"]["hayır"]
        toplamSag = Tablo[i][f"{kategori[i][1]}"]["evet"] + Tablo[i][f"{kategori[i][1]}"]["hayır"]
        try:
            Gini = ( toplamSol * giniSSTablosu[i]["0"] + toplamSag * giniSSTablosu[i]["1"] ) / ( toplamSol + toplamSag )
        except:
            Gini = 2
        giniTablosu[i] = Gini
        
    kucuk = 10,""
    for i in giniTablosu:
        if giniTablosu[i] < kucuk[0]:
            kucuk = giniTablosu[i],i

    return giniTablosu, kucuk

def ayir(veri,kucuk):
    secim=kucuk[1]
    say = 0
    sol= []
    sag = []
    if len(kategori[secim][0])==2:
        for i in veri:

            for j in Veri:
                if Veri[j][i] == kategori[secim][0][0] or Veri[j][i] == kategori[secim][0][1]:
                    sol.append(i)
                elif Veri[j][i] == kategori[secim][1]:
                    sag.append(i) 
    else:    
        for i in veri:

            for j in Veri:
                if Veri[j][i] == kategori[secim][0]:
                    sol.append(i)
                elif Veri[j][i] == kategori[secim][1]:
                    sag.append(i) 
        
    return sol,sag






def giniHesap(veri):
    yeniVeri = {}
    yeniVeriS = {"oyun":[]}
    
    for i in Veri:
        yeniVeri[i] = []

    for i in veri:
        for j in Veri:
            yeniVeri[j].append(Veri[j][i])
        yeniVeriS["oyun"].append(VeriS["oyun"][i])
    
    giniTablosu,kucuk = Gini_hesapla(kontrol(yeniVeri,yeniVeriS))

    sol ,sag = ayir(veri,kucuk)
    if veri == sol or veri==sag:
        sol =[]
        sag = []
    return sol,sag
    