#coding: utf-8
import csv
import requests
from bs4 import BeautifulSoup

url1 = "https://www.ic.gc.ca/app/scr/ic/cr/contracts.html?id=921"

fichier="contrats-ic-JHR.csv"

entetes = {
	"User-Agent":"Gabryel Desaulniers - Requête envoyée dans le cadre d'un cours de journalisme informatique à l'UQAM (EDM5240)",
	"From":"legabryel95@gmail.com"
}

contenu = requests.get(url1, headers=entetes)
page = BeautifulSoup(contenu.text,"html.parser")
#print (page)

i=0 

for ligne in page.find_all("tr"):
    if i != 0:
        #print(ligne)
        # lien = ligne.a.get("href")
        lien = ligne.a.get("id")
        # print(lien)
        lien2 =lien[1:]
        # #print (lien2)
        hyperlien ="https://www.ic.gc.ca/app/scr/ic/cr/contract.html?id="+lien2+"&lang=fra"
        # print(hyperlien)
        contenu2 = requests.get(hyperlien, headers=entetes)
        page2 = BeautifulSoup(contenu2.text, "html.parser")
        contrat = []
        #premier item de la liste
        contrat.append(hyperlien)

        # for item in page2.find_all("div",class_="icRow","&nbsp"):
        for item in page2.find_all("div",class_="icRow"): # OK, je t'avais emmené jusque-là. Ici, je ne me souviens plus pourquoi, dans la ligne précédente, se trouve «&nbsp», mais c'est inutile.
            # print(item)
            # print("="*50)

# Ici, ce ne sont pas des éléments <td> qu'on cherchait, mais des éléments <div> de classe "ic2col2 formRightCol"
            # if item.td is not None:
            #     contrat.append(item.td.text) 
            # else:
            #          contrat.append(None)

# Pour extraire le contenu de ces éléments, il fallait s'inspirer du code que je t'avais donné dans la ligne 38:
            # print(item.find("div", class_="ic2col2 formRightCol").text.strip()) # Ici, la méthode «strip()» permet d'enlever tous les espaces inutiles
            if item.find("div", class_="ic2col2 formRightCol") is not None:
                contrat.append(item.find("div", class_="ic2col2 formRightCol").text.strip())
            else:
                contrat.append(None)

        print(contrat)

        hulk = open(fichier,"a")
        hogan = csv.writer(hulk)
        hogan.writerow(contrat)        

# Tu étais près du but!
# En consultant la documentation de BeautifulSoup, il aurait été possible pour toi de compléter ton script :)

# Dans un des scripts que je vous ai envoyés, j'ai fait une erreur.
# Quand on écrit « =+1 », on dit «la variable est égale à (plus) 1».
# C'est « +=1 » qu'il faut écrire pour augmenter de 1 la valeur d'une variable dans une boucle.
    # i =+ 1
    i += 1