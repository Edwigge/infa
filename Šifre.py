abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Seznama malih in velikih črk v abecebi. Uporablja se ju pri vseh šifrah

ri = ['j', 'g', 'd', 'q', 'o', 'x', 'u', 's', 'c', 'a', 'm', 'i', 'f', 'r', 'v', 't', 'p', 'n', 'e', 'w', 'k', 'b', 'l', 'z', 'y', 'h']
rii = ['n', 't', 'z', 'p', 's', 'f', 'b', 'o', 'k', 'm', 'w', 'r', 'c', 'j', 'd', 'i', 'v', 'l', 'a', 'e', 'y', 'u', 'x', 'h', 'g', 'q']
riii = ['j', 'v', 'i', 'u', 'b', 'h', 't', 'c', 'd', 'y', 'a', 'k', 'e', 'q', 'z', 'p', 'o', 's', 'g', 'x', 'n', 'r', 'm', 'w', 'f', 'l']
rI = ['J', 'G', 'D', 'Q', 'O', 'X', 'U', 'S', 'C', 'A', 'M', 'I', 'F', 'R', 'V', 'T', 'P', 'N', 'E', 'W', 'K', 'B', 'L', 'Z', 'Y', 'H']
rII = ['N', 'T', 'Z', 'P', 'S', 'F', 'B', 'O', 'K', 'M', 'W', 'R', 'C', 'J', 'D', 'I', 'V', 'L', 'A', 'E', 'Y', 'U', 'X', 'H', 'G', 'Q']
rIII = ['J', 'V', 'I', 'U', 'B', 'H', 'T', 'C', 'D', 'Y', 'A', 'K', 'E', 'Q', 'Z', 'P', 'O', 'S', 'G', 'X', 'N', 'R', 'M', 'W', 'F', 'L']
#Seznami malih in velikih črk v treh rotorjih v enigmi. Kombinacije črk so iz enigme, v uporabi pri nemški železnici in so bile predstavljene leta 1941.

ukw = ['q', 'y', 'h', 'o', 'g', 'n', 'e', 'c', 'v', 'p', 'u', 'z', 't', 'f', 'd', 'j', 'a', 'x', 'w', 'm', 'k', 'i', 's', 'r', 'b', 'l']
UKW = ['Q', 'Y', 'H', 'O', 'G', 'N', 'E', 'C', 'V', 'P', 'U', 'Z', 'T', 'F', 'D', 'J', 'A', 'X', 'W', 'M', 'K', 'I', 'S', 'R', 'B', 'L']
#Seznam malih in velikih črk v kolutu za obračanje v enigmi.

import time

#--------------------------
#Funkcije za vse šifre.

def cezar(geslo):
    #Funkcija izvede cezarjevo šifro z zamikom 3 črke.
    rez = ""
    geslo = str(geslo)
    for i in range(len(geslo)):
        if geslo[i] in abc:
            rez += abc[(abc.index(geslo[i])) - 3]
            #K rezultatu doda za tri mesta v abecedi zamaknjeno črko.
        elif str(geslo)[i] in ABC:
            rez += ABC[(ABC.index(geslo[i])) - 3]
            #Velike črke.
        else:
            rez += geslo[i]
            #Vsi ostali znaki.
    print(rez)
    
def cezar_zamik(geslo, zamik):
    #Cezarjeva šifra z poljubnim zamikom. (Deluje enako kot prejšnja funkcija, a namesto, da odšteje 3, odšteje spremenljivko 'zamik')
    rez = ""
    if zamik.isdigit() == False:
        print("V polje 'zamik' vnesite celo število.")
        #V primeru, da v spremenljivki 'zamik' ni števila, te bo program na to opozoril.
        return
    geslo = str(geslo)
    zamik = int(zamik)
    zamik %= 26
    for i in range(len(geslo)):
        if geslo[i] in abc:
            rez += abc[(abc.index(geslo[i])) - zamik]
        elif geslo[i] in ABC:
            rez += ABC[(ABC.index(geslo[i])) - zamik]
        else:
            rez += geslo[i]
    print(rez)

def vigenere(geslo, ključ):
    #Šifra vigenere. Deluje enako kot cezarjeva šifra, a za zamik uporabimo pozicijo črke iz ključa v abecedi.
    rez = ""
    c = 0
    geslo = str(geslo)
    ključ = str(ključ)
    while len(ključ) < len(geslo):
        ključ += ključ
        #Če je ključ slučajno krajši od gesla, ga podvoji
    for i in range(len(geslo)):
        if not ključ[i] in abc:
            print('-------------------- \nV ključu so lahko le črke. \nNe sme vsebovati kateregakoli drugega znaka (števke 0-9, !, -, ?, ...) \n--------------------')
            #V primeru, da v spremenljivki 'ključ' niso le črke, te bo program na to opozoril.
            time.sleep(0.1)
            kodiranje()
        elif geslo[i] in abc:
            rez += abc[abc.index(geslo[i]) + abc.index(ključ[i - c]) - 26]
        elif geslo[i] in ABC:
            rez += ABC[ABC.index(geslo[i]) + abc.index(ključ[i - c]) - 26]
        else:
            rez += geslo[i]
            c += 1
    print(rez)

def autokey(geslo, ključ):
    #Šifra autokey. Deluje enako kot vigenere šifra, a v ključ doda tudi geslo.
    rez = ""
    gesklj = ""
    c = 0
    geslo = str(geslo)
    for e in range(len(geslo)):
        #V ključ dodaja le črke.
        if geslo[e] in abc:
            gesklj += geslo[e]
        elif geslo[e] in ABC:
            gesklj += abc[ABC.index(geslo[e])]
    ključ = str(ključ) + str(gesklj)
    while len(ključ) < len(geslo):
        ključ += ključ
        #Če je ključ slučajno krajši od gesla, ga podvoji
    for i in range(len(geslo)):
        if not ključ[i] in abc:
            print('-------------------- \nV ključu so lahko le črke. \nNe sme vsebovati kateregakoli drugega znaka (števke 0-9, !, -, ?, ...) \n--------------------')
            time.sleep(0.1)
            kodiranje()
        elif geslo[i] in abc:
            rez += abc[abc.index(geslo[i]) + abc.index(ključ[i - c]) - 26]
        elif geslo[i] in ABC:
            rez += ABC[ABC.index(geslo[i]) + abc.index(ključ[i - c]) - 26]
        else:
            rez += geslo[i]
            c += 1
    print(rez)

def enigma(geslo, r1, r2, r3):
    #Šifrirna naprava enigma. 
    začrka = ""
    rez = ""
    r1 = int(r1) % 26
    r2 = int(r2) % 26
    r3 = int(r3) % 26
    geslo = str(geslo)
    for i in range(len(geslo)):
        if geslo[i] in abc:
            #Črko 'premakne' skozi vse rotorje in nazaj.
            začrka = ri[abc.index(geslo[i]) - r1]
            začrka = rii[abc.index(geslo[i]) - r2]
            začrka = riii[abc.index(geslo[i]) - r3]
            začrka = ukw[abc.index(geslo[i])]
            začrka = riii[abc.index(geslo[i]) - r3]
            začrka = rii[abc.index(geslo[i]) - r2]
            začrka = ri[abc.index(geslo[i]) - r1]
            rez += začrka
            if r1 < 25:
                #Zamakne rotorje za eno pozicijo.
                r1 +=1
            else:
                r1 = 0
                if r2 < 25:
                    r2 += 1
                else:
                    r2 = 0
                    if r3 < 25:
                        r3 +=1
                    else:
                        r3 = 0
        elif geslo[i] in ABC:
            začrka = rI[ABC.index(geslo[i]) - r1]
            začrka = rII[ABC.index(geslo[i]) - r2]
            začrka = rIII[ABC.index(geslo[i]) - r3]
            začrka = UKW[ABC.index(geslo[i])]
            začrka = rIII[ABC.index(geslo[i]) - r3]
            začrka = rII[ABC.index(geslo[i]) - r2]
            začrka = rI[ABC.index(geslo[i]) - r1]
            rez += začrka
            if r1 < 25:
                r1 +=1
            else:
                r1 = 0
                if r2 < 25:
                    r2 += 1
                else:
                    r2 = 0
                    if r3 < 25:
                        r3 +=1
                    else:
                        r3 = 0
        else:
            rez += geslo[i]
    print(rez)



#--------------------------
#Funkcije za dešifriranje vseh šifer.

def vigenere_res(geslo, ključ):
    #Reševanje šifre vigenere. 
    rez = ""
    c = 0
    geslo = str(geslo)
    ključ = str(ključ)
    while len(ključ) < len(geslo):
        ključ += ključ
    for i in range(len(geslo)):
        if not ključ[i] in abc:
            print('-------------------- \nV ključu so lahko le črke. \nNe sme vsebovati kateregakoli drugega znaka (števke 0-9, !, -, ?, ...) \n--------------------')
            time.sleep(0.1)
            dekodiranje()
        elif geslo[i] in abc:
            rez += abc[abc.index(geslo[i]) - abc.index(ključ[i - c])]
        elif geslo[i] in ABC:
            rez += ABC[ABC.index(geslo[i]) - abc.index(ključ[i - c])]
        else:
            rez += geslo[i]
            c += 1
    print(rez)

def autokey_res(geslo, ključ):
    #Reševanje šifre autokey
    rez = ""
    c = 0
    gesklj = ključ
    geslo = str(geslo)
    for i in range(len(geslo)):
        if not gesklj[i - c] in abc:
            print('-------------------- \nV ključu so lahko le črke. \nNe sme vsebovati kateregakoli drugega znaka (števke 0-9, !, -, ?, ...) \n--------------------')
            time.sleep(0.1)
            dekodiranje()
        elif geslo[i] in abc:
            rez += abc[abc.index(geslo[i]) - abc.index(gesklj[i - c])]
            gesklj += abc[abc.index(geslo[i]) - abc.index(gesklj[i - c])]
            #H geslu doda vsako dekodirano črko.
        elif geslo[i] in ABC:
            rez += ABC[ABC.index(geslo[i]) - abc.index(gesklj[i - c])]
            gesklj += abc[ABC.index(geslo[i]) - abc.index(gesklj[i - c])]
        else:
            rez += geslo[i]
            c += 1
    print(rez)



#--------------------------
#Funkciji za kodiranje in dekodiranje (interakcija z uporabnokom)
    
def kodiranje():
    geslo = input('Kaj želiš zakodirati? ')
    if geslo == "":
        print('-------------------- \nVpišite geslo, ki bi ga radi zakodirali. \nČe želite končati, vpišite \'STOP\' \n--------------------')
        time.sleep(0.2)
        kodiranje()
    if geslo != 'STOP':
        geslo_1 = ""
        for i in range(len(geslo)):
            črka_g = geslo[i]
            if črka_g == 'č':
                črka_g = 'c'
            if črka_g == 'ć':
                črka_g = 'c'
            if črka_g == 'đ':
                črka_g = 'd'
            if črka_g == 'š':
                črka_g = 's'
            if črka_g == 'ž':
                črka_g = 'z'
            if črka_g == 'Č':
                črka_g = 'C'
            if črka_g == 'Ć':
                črka_g = 'C'
            if črka_g == 'Đ':
                črka_g = 'D'
            if črka_g == 'Š':
                črka_g = 'S'
            if črka_g == 'Ž':
                črka_g = 'Z'
            geslo_1 += črka_g
        odg = input('Katero šifro želiš? ')
        if odg == 'c':
            cezar(geslo_1)
        elif odg == 'cz':
            zamik = input('Količina zamika? ')
            cezar_zamik(geslo_1, zamik)
        elif odg == 'v' or odg == 'a':
            ključ = input('Kakšen ključ naj uporabim? ')
            ključ_1 = ""
            for i  in range(len(ključ)):
                črka_k = ključ[i]
                if črka_k == 'č' or črka_k == 'Č':
                    črka_k = 'c'
                if črka_k == 'č' or črka_k == 'Ć':
                    črka_k = 'c'
                if črka_k == 'đ' or črka_k == 'Đ':
                    črka_k = 'd'
                if črka_k == 'š' or črka_k == 'Š':
                    črka_k = 's'
                if črka_k == 'ž' or črka_k == 'Ž':
                    črka_k = 'z'
                črka_k = črka_k.lower()
                ključ_1 += črka_k
            if odg == 'v':
                vigenere(geslo_1, ključ_1)
            else:
                autokey(geslo_1, ključ_1)
        elif odg == 'e':
            r1 = input('Pozicija rotorja 1? ')
            if r1.isdigit() == False:
                print('-------------------- \nZa rotorje lahko vpišite le naravna števila. \n--------------------')
                kodiranje()
            r2 = input('Pozicija rotorja 2? ')
            if r2.isdigit() == False:
                print('-------------------- \nZa rotorje lahko vpišite le naravna števila. \n--------------------')
                kodiranje()
            r3 = input('Pozicija rotorja 3? ')
            if r3.isdigit() == False:
                print('-------------------- \nZa rotorje lahko vpišite le naravna števila. \n--------------------')
                kodiranje()
            if r1.isdigit() != False and r2.isdigit() != False and r3.isdigit() != False:
                enigma(geslo_1, r1, r2, r3)
        elif odg != 'STOP':
            print('-------------------- \nZa odgovor vpišite eno od naslednjih črk: \nc - cezarjeva šifra \ncz - cezarjeva šifra s poljubnim zamikom \nv - šifra vigenere \na - šifra autokey \ne - enigma \nČe želite končati, vpišite \'STOP\'. \n--------------------')
            time.sleep(0.2)
            kodiranje()
        kdaj = False
        while kdaj == False:
            še = input('Še eno? ')
            if še == 'd' or še == 'D' or še == 'j' or še == 'J':
                kodiranje()
                kdaj = True
            elif še == 'dek' or še == 'Dek' or še == 'DEK':
                dekodiranje()
                kdaj = True
            elif še == 'n' or še == 'N':
                kdaj = True
                return
            else:
                print('-------------------- \nProsim, vnesite veljaven odgovor. \nd - da, želim zakodirati še eno šifro \nn - ne, ne želim zakodirati še ene šifre \ndek - dekodiranje \n--------------------')
                kdaj = False
        
def dekodiranje():
    geslo = input('Kaj želiš dekodirati? ')
    if geslo == "":
        print('-------------------- \nVpišite geslo, ki bi ga radi dekodirali. \nČe želite končati, vpišite \'STOP\' \n--------------------')
        time.sleep(0.2)
        dekodiranje()
    if geslo != 'STOP':
        odg = input('S katero šifro je šifra zakodirana? ')
        if odg == 'c':
            cezar_zamik(geslo, '23')
        elif odg == 'cz':
            zamik = input('Količina zamika, ki je bila uporabljena? ')
            cezar_zamik(geslo, str(26 - int(zamik)))
        elif odg == 'v' or odg == 'a':
            ključ = input('Kakšen ključ je bil uporabljen za kodiranje? ')
            ključ_1 = ""
            for i  in range(len(ključ)):
                črka_k = ključ[i]
                if črka_k == 'č' or črka_k == 'Č':
                    črka_k = 'c'
                if črka_k == 'č' or črka_k == 'Ć':
                    črka_k = 'c'
                if črka_k == 'đ' or črka_k == 'Đ':
                    črka_k = 'd'
                if črka_k == 'š' or črka_k == 'Š':
                    črka_k = 's'
                if črka_k == 'ž' or črka_k == 'Ž':
                    črka_k = 'z'
                črka_k = črka_k.lower()
                ključ_1 += črka_k
            if odg == 'v':
                vigenere_res(geslo, ključ_1)
            else:
                autokey_res(geslo, ključ)
        elif odg == 'e':
            print('Žal dešifriranje enigme trenutno še ni mogoče. Prototip dešifrerja je pospravljen nekje na dnu kode. Hvala za razumevanje! :)')
        elif odg != 'STOP':
            print('-------------------- \nZa odgovor vpišite eno od naslednjih črk: \nc - cezarjeva šifra \ncz - cezarjeva šifra s poljubnim zamikom \nv - šifra vigenere \na - šifra autokey \ne - enigma \nČe želite končati, vpišite \'STOP\'. \n--------------------')
            time.sleep(0.2)
            dekodiranje()
        kdaj = False
        while kdaj == False:
            še = input('Še eno? ')
            if še == 'd' or še == 'D' or še == 'j' or še == 'J':
                dekodiranje()
                kdaj = True
            elif še == 'kod' or še == 'Kod' or še == 'KOD':
                kodiranje()
                kdaj = True
            elif še == 'n' or še == 'N':
                kdaj = True
                return
            else:
                print('-------------------- \nProsim, vnesite veljaven odgovor. \nd - da, želim dekodirati še eno šifro \nn - ne, ne želim dekodirati še ene šifre \nkod - kodiranje \n--------------------')
                kdaj = False                
                
def kvizek():
    #Vprašanje, ki ga program postavi čisto na začetku
    kviz = input('Ali želite nekaj zakodirati ali dekodirati? ')
    if kviz == 'kod' or kviz == 'Kod' or kviz == 'KOD' or kviz == 'zak' or kviz == 'Zak' or kviz == 'ZAK':
        kodiranje()
    elif kviz == 'dek' or kviz == 'Dek' or kviz == 'DEK':
        dekodiranje()
    elif kviz != 'STOP':
        print('-------------------- \nProsim, vnesite veljaven odgovor. \nkod - kodiranje \ndek - dekodiranje \nČe ste si premislili in ne želite narediti nič, vpišite \'STOP\' \n--------------------')
        kvizek()

kvizek()




































































































#-------------------------------------
#Prototip kode za dešifriranje enigme (ne vem zakaj ne dela)

'''
def enigma_res(geslo, r1, r2, r3):
    #Dešifriranje enigme.
    začrka = ""
    rez = ""
    poz = 0
    r1 %= 26
    r2 %= 26
    r3 %= 26
    geslo = str(geslo)
    for i in range(len(geslo)):
        if geslo[i] in abc:
            #Črko 'premakne' skozi vse rotorje in nazaj.
            začrka = ri[abc.index(geslo[i]) - r1]
            začrka = rii[abc.index(geslo[i]) - r2]
            začrka = riii[abc.index(geslo[i]) - r3]
            začrka = ukw[abc.index(geslo[i])]
            začrka = riii[abc.index(geslo[i]) - r3]
            začrka = rii[abc.index(geslo[i]) - r2]
            začrka = ri[abc.index(geslo[i]) - r1]
            rez += začrka
            if r1 < 25:
                r1 +=1
            else:
                r1 = 0
                if r2 < 25:
                    r2 += 1
                else:
                    r2 = 0
                    if r3 < 25:
                        r3 +=1
                    else:
                        r3 = 0
        elif geslo[i] in ABC:
            začrka = rI[ABC.index(geslo[i]) - r1]
            začrka = rII[ABC.index(geslo[i]) - r2]
            začrka = rIII[ABC.index(geslo[i]) - r3]
            začrka = UKW[ABC.index(geslo[i])]
            začrka = rIII[ABC.index(geslo[i]) - r3]
            začrka = rII[ABC.index(geslo[i]) - r2]
            začrka = rI[ABC.index(geslo[i]) - r1]
            rez += začrka
            if r1 < 25:
                r1 +=1
            else:
                r1 = 0
                if r2 < 25:
                    r2 += 1
                else:
                    r2 = 0
                    if r3 < 25:
                        r3 +=1
                    else:
                        r3 = 0
        else:
            rez += geslo[i]
    print(rez)
'''


#-----------------------------
#Dodatek k prototipu

'''
for e in range(len(geslo)):
        if geslo[e] in abc or geslo[e] in ABC:
            poz += 1
    for j in range(poz):
        if r1 < 25:
            #Zamakne vse rotorje na svojo končno pozicijo.
            r1 +=1
        else:
            r1 = 0
            if r2 < 25:
                r2 += 1
            else:
                r2 = 0
                if r3 < 25:
                    r3 +=1
                else:
                    r3 = 0
'''


