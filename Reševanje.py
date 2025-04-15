abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def cezar_zamik(geslo, zamik):
    rez = ""
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
    return(rez)

a = input('geslo ')
c = 0

for i in range(26):
    neki = cezar_zamik(a, c)
    print(neki)
    print('')
    print('')
    print('')
    c += 1
