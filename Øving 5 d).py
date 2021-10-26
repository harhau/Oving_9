# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:22:12 2021

@author: Harald
"""

filnavn_1 = input("Skriv inn navn på fila med eposter: ")
filnavn_2 = input("Skriv inn navn på fila som skal inneholde avsendernes epost: ")


try:
    with open(filnavn_1, "r") as f:
        with open(filnavn_2, "w") as g:
            for line in f:
                line.strip()
                if "From: " in line:
                    index1 = line.find("<") + 1
                    index2 = line.find(">")
                    epost = line[index1 : index2]
                    if "mailto:" in line:
                        index1 = line.find("mailto:") + 7
                        index2 = line.find("]")
                        epost = line[index1 : index2]
                        g.write(epost + "\n")
                    else:
                        g.write(epost + "\n")
                        
except FileNotFoundError:
    print("Finner ikke fila!")
