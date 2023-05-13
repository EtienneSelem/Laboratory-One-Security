import operator

class KeyGenerate:
    _f_KEY         =   list()            # Longueur de la clé
    _f_PERMUTED_KEY = dict()             # clé de permutation
    _f_H_PERMUTE   =   list()            # Fonction de permutation
    _f_H_PERMUTED_VALUES = list()        # Valeur de permutation
    _f_PI = 0
    _f_key1        =   list()
    _f_key2        =   list()
    _f_key1_prime      =   list()
    _f_key2_prime       =   list()

    def __init__(self, Key:list, H:list) -> None:
        self._f_H_PERMUTE       =    H
        self._f_KEY             =   Key
    
    def getKeyIndexes(self) -> dict:
        permutedKey = dict() 
        permutedKey = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(self._f_KEY):
            permutedKey[i] = self._f_KEY[i]
            i = i + 1        
        return permutedKey

    def applyPermutation(self) -> None:
        self._f_PERMUTED_KEY = self.getKeyIndexes() # Une table de permutation 
        
        for i in self._f_H_PERMUTE:
            idx = i
            for j in self._f_PERMUTED_KEY.keys():
                if(idx == j):
                    self._f_H_PERMUTED_VALUES.append(self._f_PERMUTED_KEY[j])
                    continue
        print("* La valeur de la clé après permutation est : ",*self._f_H_PERMUTED_VALUES)
        print("\n")

    def splitKey(self) -> None:
        self._f_key1_prime = self._f_H_PERMUTED_VALUES[:4]
        self._f_key2_prime = self._f_H_PERMUTED_VALUES[4:]
        
        print("* La clé est maintenant divisé en 2 blocks :")
        print("k1' = ", *self._f_key1_prime)
        print("k2' = ", *self._f_key2_prime)
        print("\n")
    
    def applyKey1Operator(self) -> None:
        i = 0
        j = 0
        while i < len(self._f_key1_prime):
            while j < len(self._f_key2_prime):
                self._f_key1.append(operator.xor(self._f_key1_prime[j], self._f_key2_prime[j]))
                j = j + 1
            i = i + 1
        print("* K1 = k1' XOR k2' = ", *self._f_key1)
    
    def applyKey2Operator(self) -> None:
        i = 0
        j = 0
        while i < len(self._f_key2_prime):
            while j < len(self._f_key1_prime):
                self._f_key2.append(operator.and_(self._f_key2_prime[j], self._f_key1_prime[j]))
                j = j + 1
            i = i + 1
        print("* K2 = k2' AND k1' = ", *self._f_key2)
        print("\n")

    # Shift keys to left    
    def leftShift(self) -> None:
        fistTwoValues = self._f_key1[0:2]
        lastTwoValues = self._f_key1[2:4]

        self._f_key1 = lastTwoValues + fistTwoValues
        print("* Le décalage à gauche de K1 = ", *self._f_key1)

    # Shift keys to right
    def leftRight(self) -> None:
        fistThirdValues = self._f_key2[0:3]
        lastValue = self._f_key2[3:]

        self._f_key2 = lastValue + fistThirdValues
        print("* Le décalage à droite de K2 = ", *self._f_key2)
    
    #Output keys values
    def outputKeys(self) -> None:
        print("_______________________________________")
        print("({}, {})".format(self._f_key1, self._f_key2))
        print("_______________________________________")
    # Getting K1 value
    def getK1(self) -> list:
        return self._f_key1

    # Getting K2 value
    def getK2(self) -> list:
        return self._f_key2