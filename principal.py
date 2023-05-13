from Classes.KeyGenerate import *
from Classes.Chiffrement import *
from Classes.Dechiffrement import *

# Algorithme de la Génération des clés

print("*****************************************")
print("______________Algorithme de génération de clé______________")
print("\n")

# Iniialisation
KEY = list()
#KEY = (0, 1, 1, 0, 1, 1, 0, 1)

print("Veillez entrer successivement les 8 bits de la clé K")
i = 1
while i <= 8:
    print("- Bit ", i)
    bit = input()
    if int(bit) not in (0, 1):
        print("Veillez entrer un chiffre binaire")
        break
    else:
        KEY.append(int(bit))
    i = i + 1

H_PERMUTE = list()
H_PERMUTE = (6, 5, 2, 7, 4, 1, 3, 0)

print("Etape 1 : Entrée")
print("* Soit la clé entrée au clavier: ", *KEY)
print("\n")
print("* La fonction de permutation : ", *H_PERMUTE)

feistelCipher = KeyGenerate(KEY, H_PERMUTE)

print("\n")
print("Etape 2 : Appliquer la fonction de permutation")
feistelCipher.applyPermutation()

print("Etape 3 : Diviser K en deux blocs de 4 bits k = k1' || k2'")
feistelCipher.splitKey()

print("Etape 4 : K1 = k1' + k2' et K2 = K2' ET K1")
feistelCipher.applyKey1Operator()
feistelCipher.applyKey2Operator()

print("Etape 5 : Décalage à gauche de K1")
feistelCipher.leftShift()
feistelCipher.leftRight()

print("\n")
print("Etape 6 : Sortie")
feistelCipher.outputKeys() 
print("*****************************************")
print("\n")


print("______________Algorithme de Chiffrement______________")
print("\n")

# Iniialisation
BLOC = list()
BLOC = (0, 1, 1, 0, 1, 1, 1, 0)
PI = list()
PI = (4, 6, 0, 2, 7, 3, 1, 5)
P = (2, 0, 1, 3)

print("Etape 1 : Entrée la clé K de longueur 8")
print("* ",BLOC)
print("* Fonction de permutation", PI)

encrypt = Chiffrement(BLOC, PI)

print("\n")
print("Etape 2 : Appliquer la fonction de permutation")
encrypt.applyBlocPermutation()
print("\n")

print("Etape 3 : Diviser N en deux blocs de 4 bits : N = Go || Do")
encrypt.splitBloc()
print("\n")

print("Etape 4 : #Premier Round, calculer : D1 = P(Do) XOR k1")
encrypt.calculateD1(P) # Calculer la permutation de Go
encrypt.calculateFirstRound(feistelCipher.getK1()) # Calculer la valeur de D1

print("\n")
print("Etape 5 : Deuxième Round Calculer la valeur de D2")
print("Deuxième Round")
encrypt.calculateSecondRound(P, feistelCipher.getK2()) 

print("\n")
print("Etape 6 Concatenation : C = G2 || D2")
encrypt.concatenate()

print("\n")
print("Etape 7 Inverse de PI")
encrypt.inverse_PI_permutation(PI)

print("*****************************************")
print("\n")


print("______________Algorithme de Déchiffrement______________")
print("\n")

print("Etape 1 : Enntrée = Bloc C de 8 bits")
BLOC_C = encrypt.get_encrypted_text()
PI = list()
PI = (4, 6, 0, 2, 7, 3, 1, 5)
P = list()
P = (2, 0, 1, 3)
decipher = Dechiffrement(BLOC_C, PI)

print("\n")
print("* Soit le bloc C suivant : ", BLOC_C)

print("\n")
print("Etape 2 : Appliquer la fonction de permutation PI sur le bloc C")
decipher.applyBlocPermutation()

print("\n")
print("Etape 3 : Diviser le bloc C en deux blocs de 4 bits telque C = G2 || D2")
decipher.splitBloc()

print("\n")
print("Etape 4 : PREMIER ROUND")
decipher.calculate_first_round(P, feistelCipher.getK2())

print("\n")
print("Etape 5 : DEUXIEME ROUND")
decipher.calculate_second_round(P, feistelCipher.getK1())

print("\n")
print("Etape 6 : CONCATENATION Go || Do")
decipher.calculate_N()

print("\n")
print("Etape 7 : APPLIQUER L'INVERSE DE LA PERMUTATION")
decipher.calculate_N()

print("\n")
print("Etape 8 : SORTIE TEXTE CLAIR")
decipher.calculate_PI_reverse_on_N()