# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:04:36 2021

@author: Harald Haualand testertest
"""

class flervalgspørsmål:
    
    def __init__(self, spørsmål, alternativer, riktig_svar):
        self.spørsmål = spørsmål
        self.alternativer = alternativer
        self.riktig_svar = riktig_svar
    
    def __str__(self):
        return self.spørsmål + str(self.alternativer)
    
    def sjekk_svar(self):
        brukerens_svar = int(input("Hvilket av alternativene er riktig? "))
        if brukerens_svar == self.riktig_svar:
            return 1
        else:
            return 0
        
spm = flervalgspørsmål("Hva er hovedstaden i Danmark?", ("1: Oslo", "2: København"), 2)
spm2 = flervalgspørsmål("Hva er 5+5?", ("1: 10" , "2: 20"), 1)

print(spm)
if spm.sjekk_svar() == 1:
    print("Riktig svar.")
else:
    print("Feil svar.")
    
print("\n")
    
print(spm2)
if spm2.sjekk_svar() == 1:
    print("Riktig svar.")
else:
    print("Feil svar.")
    
