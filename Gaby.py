#coding: utf-8
import csv
import requests
from bs4 import BeautifulSoup
url1 = "https://www.ic.gc.ca/app/scr/ic/cr/contracts.html?id=921"
# voici le nom de mon fichier
fichier="contrats-ic.csv"
# je m'identifie, car je suis poli
entetes = {
	"User-Agent":"Gabryel Desaulniers - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"legabryel95@gmail.com"
}
# on etablie une connexion avec le site grace a resquests
contenu = requests.get(url1, headers=entetes)
# on demande a beautiful soup d'analyser le texte HTML
page = BeautifulSoup(contenu.text,"html.parser")
#print (page)
# enlever les entetes, donc se focuser sur ce qu'on veut
i=0 
for ligne in page.find_all("tr"):
    if i != 0:
        #print(ligne)
        #lien = ligne.a.get("href")
        lien = ligne.a.get("id")
        #print(lien)
        lien2 =lien[1:]
        #print (lien2)
        hyperlien ="https://www.ic.gc.ca/app/scr/ic/cr/contract.html?id="+lien2+"&lang=fra"
        #print(hyperlien)
        contenu2 = requests.get(hyperlien, headers=entetes)
        page2 = BeautifulSoup(contenu2.text, "html.parser")
        contrat = []
        #premier item de la liste
        contrat.append(hyperlien)
       #j'ai essaye de trouver une maniere d'integrer les valeurs des contrats avec l'option inspection, mais en vain. Mon scripte ne sort que les url. Mes essaies ont ete reduis a neant. Toutes tentatives etaient pleines d'espoir, mais vaines de sense
        for item in page2.find_all("div",class_="icRow","&nbsp"):
            print(item)
            print("="*50)
            if item.td is not None:
                contrat.append(item.td.text) 
                
            else:
                     contrat.append(None)
                     
           
        
            print(contrat)
                
        hulk = open(fichier,"a")
        hogan = csv.writer(hulk)
        hogan.writerow(contrat)        
                
                
    i =+ 1
