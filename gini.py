import pandas as pd

dataframe1 = pd.read_excel('Egitim_Test_Verileri/egitim1.xlsx')

def dataframe_to_dict(dataframe):
    
    columns = dataframe.columns

    data_dict = {column: list(dataframe[column]) for column in columns}

    data_sonuc = {"SONUÇ":data_dict["SONUÇ"]}
    data_dict.pop("SONUÇ")
    data_dict.pop("Record")
    
    return data_dict, data_sonuc

def kategori_yaz(veri):
    column_means = {}
    for attribute in basliklar:
        if attribute in veri:
            values = veri[attribute]
            try:
                mean = sum([float(value) for value in values]) / len(values)
            except:
                mean = 0
            column_means[attribute] = mean
        else:
            column_means[attribute] = None  # Sütun verileri eksikse, None olarak işaretle
    return column_means

Veri,VeriS =  dataframe_to_dict(dataframe1)

Tablo1 = {
    "evet" : [],
    "hayır": [],
    "giniSS":[]
}

basliklar = []
for i in Veri:
    basliklar.append(i)
kategori = kategori_yaz(Veri)



def kontrol(Veri,VeriS):
    Tablo = tablo_olustur()
    for indis in range(len(VeriS["SONUÇ"])):
        for baslik in Veri:
            if Veri[baslik][indis] <= kategori[baslik]:
                if VeriS["SONUÇ"][indis]=="yes":
                    Tablo[baslik][baslik+"_Sol"]["evet"] +=1
                else:
                    Tablo[baslik][baslik+"_Sol"]["hayır"] +=1
            else:
                if VeriS["SONUÇ"][indis]=="yes":
                    Tablo[baslik][baslik+"_Sag"]["evet"] +=1
                else:
                    Tablo[baslik][baslik+"_Sag"]["hayır"] +=1
                        
    return Tablo

def tablo_olustur():
    Tablo = {}
    for baslik in Veri:
        Tablo[baslik] = {f"{baslik}_Sol":{"evet":0,"hayır":0},
                         f"{baslik}_Sag":{"evet":0,"hayır":0}}
    return Tablo


def Gini_hesapla(Tablo):
    
    giniSSTablosu = {}
    giniTablosu = {}
    Sol_Sag = ["_Sol","_Sag"]
    for i in Tablo:
        giniss = {}
        for j in Sol_Sag:
            degerler = Tablo[i][i+j]
            evet= degerler["evet"]
            hayir= degerler["hayır"]
            try:

                gini = 1 - ( ((evet/(evet+hayir))**2) + ((hayir/(evet+hayir))**2))
            except:
                gini = 2
            giniss[str(j)] = gini
            giniSSTablosu[i] = giniss
    for i in giniSSTablosu:
        
        toplamSol = Tablo[i][i+"_Sol"]["evet"] + Tablo[i][i+"_Sol"]["hayır"]
        toplamSag = Tablo[i][i+"_Sag"]["evet"] + Tablo[i][i+"_Sag"]["hayır"]
        try:
            Gini = ( toplamSol * giniSSTablosu[i]["_Sol"] + toplamSag * giniSSTablosu[i]["_Sag"] ) / ( toplamSol + toplamSag )
        except:
            Gini = 2
        giniTablosu[i] = Gini
        
    kucuk = [10,""]
    for i in giniTablosu:
        if giniTablosu[i] < kucuk[0]:
            kucuk = [giniTablosu[i],i]

    return giniTablosu, kucuk

def ayir(veri,kucuk):
    secim=kucuk[1]
    say = 0
    sol= []
    sag = []
    
    for i in veri:

        
        if Veri[secim][i] <= kategori[secim]:
            sol.append(i)
        elif Veri[secim][i] > kategori[secim]:
            sag.append(i) 

    return sol,sag


def giniHesap(veri):
    ayirici = veri[0]
    veriler= veri[1]
    yeniVeri = {}
    yeniVeriS = {"SONUÇ":[]}
    
    for i in Veri:
        yeniVeri[i] = []

    for i in veriler:
        for j in Veri:
            yeniVeri[j].append(Veri[j][i])
        yeniVeriS["SONUÇ"].append(VeriS["SONUÇ"][i])
        
        
    kategori = kategori_yaz(yeniVeri)
    sol ,sag = ayir(veriler,ayirici)
    
    yeniVeriSL = {"SONUÇ":[]}
    yeniVeriSR = {"SONUÇ":[]}
    
    yeniVeriL = {}
    for i in Veri:
        yeniVeriL[i] = []

    for i in sol:
        for j in Veri:
            yeniVeriL[j].append(Veri[j][i])
        yeniVeriSL["SONUÇ"].append(VeriS["SONUÇ"][i])
    
    yeniVeriR = {}
    for i in Veri:
        yeniVeriR[i] = []

    for i in sag:
        for j in Veri:
            yeniVeriR[j].append(Veri[j][i])
        yeniVeriSR["SONUÇ"].append(VeriS["SONUÇ"][i])
       
    
    
    
    giniTablosu,kucukL = Gini_hesapla(kontrol(yeniVeriL,yeniVeriSL))
    giniTablosu,kucukR = Gini_hesapla(kontrol(yeniVeriR,yeniVeriSR))
    kucukL[0] = kategori_yaz(yeniVeriL)[kucukL[1]]
    kucukR[0] = kategori_yaz(yeniVeriR)[kucukR[1]]
    sol = [kucukL,sol]
    sag = [kucukR,sag]
    

    if veri[1] == sol[1] or veri[1]==sag[1]:
        sol = [VeriS["SONUÇ"][veri[1][0]],[]]
        sag = [VeriS["SONUÇ"][veri[1][0]],[]]
        
        #sol =[[],[]]
        #sag = [[],[]]
    return sol,sag , kategori
    
"""

def giniHesap(veri):
    veriler= veri[1]
    yeniVeri = {}
    yeniVeriS = {"SONUÇ":[]}
    
    for i in Veri:
        yeniVeri[i] = []

    for i in veriler:
        for j in Veri:
            yeniVeri[j].append(Veri[j][i])
        yeniVeriS["SONUÇ"].append(VeriS["SONUÇ"][i])
    #print(yeniVeri,yeniVeriS)
    giniTablosu,kucuk = Gini_hesapla(kontrol(yeniVeri,yeniVeriS))
    
    kategori = kategori_yaz(yeniVeri)
    sol ,sag = ayir(veriler,kucuk)
    sol = [kucuk,sol]
    sag = [kucuk,sag]

    if veri == sol or veri==sag:
        sol =[[],[]]
        sag = [[],[]]
    return sol,sag , kategori"""
    