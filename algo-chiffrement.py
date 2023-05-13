import operator

class Encrypt:

    _BLOC         =   list()            # Longueur de la clé
    _PERMUTED_KEY = dict()             # clé de permutation
    _PI_PERMUTE   =   list()            # Fonction de permutation
    _PI_PERMUTED_VALUES = list()        # Valeur de permutation
    _PI = list()
    _Go        =   list()
    _Go_PERMUTATION        =   list()
    _Do        =   list()
    _G1        =   list()
    _G2        =   list()
    _G1_PERMUTATION        =   list()
    _D1        =   list()
    _D2        =   list()
    _C         =   list()
    _C_indexes         =   list()
    _TEXT_CHIFFRE = list()

    def __init__(self, Bloc:int, PI:int) -> None:
        self._PI_PERMUTE       =    PI
        self._BLOC             =   Bloc
    
    def inverse_PI_permutation(self, P:list)-> None:
        PI_keys = dict()
        PI_keys = self.get_Concatenation_Indexes(P) # Une table de permutation 
        inversePI = list()

        print("* PI keys : ", *PI_keys.keys())
        print("* PI values : ", *PI_keys.values())
               
        for i in PI_keys.keys():
            idx = i
            for val in PI_keys.values():
                if(idx == PI_keys[val]):
                    inversePI.append(val)
                    continue
        print("\n")
        print("* L'inverse de PI est : ", *inversePI)
        print("\n")

        self._C_indexes = self.get_Concatenation_Indexes(self._C) # Une table des indexes de C
        
        for i in inversePI:
            idx = i
            for val in self._C_indexes.keys():
                if(idx == val):
                    self._TEXT_CHIFFRE.append(self._C_indexes[val])
                    continue
        print("__________________________________________")
        print("Le Texte chiffré est : ", *self._TEXT_CHIFFRE)
        print("__________________________________________")

    def get_encrypted_text(self) -> list:
        return self._TEXT_CHIFFRE

    def get_Concatenation_Indexes(self, list:list) -> dict:
        permutedC = dict() 
        permutedC = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(list):
            permutedC[i] = list[i]
            i = i + 1        
        return permutedC
    
    def getBlocIndexes(self) -> dict:
        permutedBloc = dict() 
        permutedBloc = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(self._BLOC):
            permutedBloc[i] = self._BLOC[i]
            i = i + 1        
        return permutedBloc

    def applyBlocPermutation(self) -> None:
        self._PERMUTED_KEY = self.getBlocIndexes() # Une table de permutation 
        
        for i in self._PI_PERMUTE:
            idx = i
            for j in self._PERMUTED_KEY.keys():
                if(idx == j):
                    self._PI_PERMUTED_VALUES.append(self._PERMUTED_KEY[j])
                    continue
        print("* La valeur du bloc N après permutation est : ", *self._PI_PERMUTED_VALUES)
        print("\n")

    def splitBloc(self) -> None:
        self._Go = self._PI_PERMUTED_VALUES[:4]
        self._Do = self._PI_PERMUTED_VALUES[4:]
        
        print("* La clé est maintenant divisé en 2 blocks :")
        print("Go' = ", *self._Go)
        print("Dà' = ", *self._Do)
        print("\n")
    
    def concatenate(self) -> None:
        self._C = self._G2 + self._D2
        print("* La concatenation C = ", *self._C)

    def calculateSecondRound(self, P:list, k2:list) -> None:
        self._G1_PERMUTATION =  self.applyRoundPermutation(P, 1)
        self.apply_D2_Operator(k2)
        self.apply_G2_Operator(k2)

    def apply_G2_Operator(self, k:list) -> None:
        G1_K2_value = list() # Resultat de G1 v K1
        i = 0
        j = 0
        while i < len(self._G1):
            while j < len(k):
                G1_K2_value.append(operator.or_(self._G1[j], k[j]))
                j = j + 1
            i = i + 1

        i = 0
        j = 0
        while i < len(self._D1):
            while j < len(G1_K2_value):
                self._G2.append(operator.xor(self._D1[j], G1_K2_value[j]))
                j = j + 1
            i = i + 1
        print("* G2 = D1 XOR (G1 v k2) = ", *self._G2)

    def apply_D2_Operator(self, k:list) -> None:
        i = 0
        j = 0
        while i < len(self._G1_PERMUTATION):
            while j < len(k):
                self._D2.append(operator.xor(self._G1_PERMUTATION[j], k[j]))
                j = j + 1
            i = i + 1
        print("* D2 = P(G1) XOR k2 = ", *self._D2)

    def calculateFirstRound(self, k1:list) -> None:
        self.apply_D1_Operator(k1)
        self.apply_G1_Operator(k1)
    
    def apply_G1_Operator(self, k:list) -> None:
        Go_K1_value = list() # Resultat de Go v K1
        i = 0
        j = 0
        while i < len(self._Go):
            while j < len(k):
                Go_K1_value.append(operator.or_(self._Go[j], k[j]))
                j = j + 1
            i = i + 1

        i = 0
        j = 0
        while i < len(self._Do):
            while j < len(Go_K1_value):
                self._G1.append(operator.xor(self._Do[j], Go_K1_value[j]))
                j = j + 1
            i = i + 1
        print("* G1 = Do XOR (Go v k1) = ", *self._G1)


    def apply_D1_Operator(self, k:list) -> None:
        i = 0
        j = 0
        while i < len(self._Go_PERMUTATION):
            while j < len(k):
                self._D1.append(operator.xor(self._Go_PERMUTATION[j], k[j]))
                j = j + 1
            i = i + 1
        print("* D1 = P(Go) XOR k1' = ", *self._D1)

    def calculateD1(self, P:list) -> None:
            self._Go_PERMUTATION = self.applyRoundPermutation(P, 0)
            print("* La Permutation de Go est : ", *self._Go_PERMUTATION)
            print("\n")
    
    def applyRoundPermutation(self, PERMUTE:list, G_index:int) -> list:
        roundedIndexes = dict()
        permutationTable = list()

        if G_index == 0:
            roundedIndexes = self.getRoundIndexes(self._Go) # Une table de permutation 
            for i in PERMUTE:
                idx = i
                for j in roundedIndexes.keys():
                    if(idx == j):
                        permutationTable.append(roundedIndexes[j])
                        continue
        elif G_index == 1:
            roundedIndexes = self.getRoundIndexes(self._G1) # Une table de permutation 
            for i in PERMUTE:
                idx = i
                for j in roundedIndexes.keys():
                    if(idx == j):
                        permutationTable.append(roundedIndexes[j])
                        continue
        return permutationTable
    
    def getRoundIndexes(self, Round:list) -> dict:
        permutedRound = dict() 
        permutedRound = { 0: 0, 1: 0, 2: 0, 3: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(Round):
            permutedRound[i] = Round[i]
            i = i + 1        
        return permutedRound