# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:27:35 2021

@author: Harald Haualand
"""


class flervalgsporsmaal:
    
    def __init__(self, sporsmaal, alternativer, riktig_svar):
        self.sporsmaal = sporsmaal
        self.alternativer = alternativer
        self.riktig_svar = riktig_svar
        
    def __str__(self):
        tekst = self.sporsmaal + "\nalternativer:\n"
        index = 0
        for alternativ in self.alternativer:
            tekst += str(index)+ " " + alternativ + "\n"
            index += 1
        return tekst
    
    def __korrekt_svar_tekst__(self):
        return "Riktig svar er:" + " " + str(self.riktig_svar) + " " + self.alternativer[self.riktig_svar]
    
    def sjekk_svar(self, spiller_svar):
        if spiller_svar == self.riktig_svar:
            return 1
        else: 
            return 0
        
    
def les_sporsmaal():
    sporsmaal_liste = []
    with open ("sporsmaalsfil.txt", "r", encoding="UTF8") as f:
        for line in f:
            line.strip()
            kolonner = line.split(":")
            sporsmaal = kolonner[0]
            alternativer = kolonner[2].replace("[", "").replace("]", "").replace(" ", "").split(",")
            riktig_svar = int(kolonner[1])
            sporsmaal_liste.append(flervalgsporsmaal(sporsmaal, alternativer, riktig_svar))
    return sporsmaal_liste
        
        
if __name__ == "__main__":
    liste = les_sporsmaal()
    for sporsmaal in liste:
        print(sporsmaal)
        spiller_1_svar = int(input("Velg et alternativ for spiller 1: "))
        spiller_2_svar = int(input("Velg et alternativ for spiller 2: "))
        print("")
        print(sporsmaal.__korrekt_svar_tekst__())
        print("")
        if sporsmaal.sjekk_svar(spiller_1_svar):
            print("Spiller 1: Riktig.")
        else:
            print("Spiller 1: Feil.")
            
        if sporsmaal.sjekk_svar(spiller_2_svar):
            print("Spiller 2: Riktig.")
        else:
            print("Spiller 2: Feil.")
            
        print("")
        print("")
        
antall_riktige_spiller_1 = 0
antall_riktige_spiller_2 = 0
for sporsmaal in liste:
    antall_riktige_spiller_1 += sporsmaal.sjekk_svar(spiller_1_svar)
    antall_riktige_spiller_2 += sporsmaal.sjekk_svar(spiller_2_svar)
    
print("Spiller 1 har " + str(antall_riktige_spiller_1) + " av 8 riktige svar.")
print("Spiller 2 har " + str(antall_riktige_spiller_2) + "av 8 riktige svar.")
    


