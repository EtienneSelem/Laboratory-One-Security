import operator

class Dechiffrement:

    # Longueur de la clé
    _PERMUTED_BLOC = dict()             # clé de permutation
    _PI_PERMUTED_BLOC_VALUES = list()        # Valeur de permutation
    _PI_PERMUTE   =   list()            # Fonction de permutation
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
    _TEXTE_DECHIFFRE = list()
    _P_REVERSE = list()
    _N = list()
    _N_PERMUTED = list()
    _PI_REVERSE = list()

    def __init__(self, Bloc:int, PI:int) -> None:
        self._PI = PI
        self._C = Bloc

    def applyBlocPermutation(self) -> None:
        self._PERMUTED_BLOC = self.get_8_bits_Indexes(self._C) # Presentation de la table de permutation
        for i in self._PI:
            idx = i
            for j in self._PERMUTED_BLOC.keys():
                if(idx == j):
                    self._PI_PERMUTED_BLOC_VALUES.append(self._PERMUTED_BLOC[j])
                    continue
            print("* La valeur du bloc N après permutation est : ", *self._PI_PERMUTED_BLOC_VALUES)
            print("\n")
        
    
    def get_8_bits_Indexes(self, list:list) -> dict:
        permutedC = dict() 
        permutedC = { 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(list):
            permutedC[i] = list[i]
            i = i + 1        
        return permutedC
    
    def get_4_bits_Indexes(self, list:list) -> dict:
        permutedC = dict() 
        permutedC = { 0: 0, 1: 0, 2: 0, 3: 0  } # Initialiser la table de permutation

        i = 0
        while i < len(list):
            permutedC[i] = list[i]
            i = i + 1
        return permutedC
    
    def splitBloc(self) -> None:
        self._G2 = self._PI_PERMUTED_BLOC_VALUES[:4]
        self._D2 = self._PI_PERMUTED_BLOC_VALUES[4:]
        
        print("Le bloc C est maintenant divisé en 2 blocks :")
        print("** G2' = ", *self._G2)
        print("** D2' = ", *self._D2)
        print("\n")
    
    def calculate_first_round(self, P, public_key) -> None:
        self.calculate_G1(P, public_key)
        self.calculate_D1(public_key)

    def calculate_G1(self, P, public_key) -> None:
        P_keys = dict()
        P_keys = self.get_4_bits_Indexes(P) # Une table de permutation 
        D2_K2_XOR = self.apply_xor_operator(self._D2, public_key)

        print("* P keys : ", *P_keys.keys())
        print("* P values : ", *P_keys.values())
        print("* D2 XOR K2 = ", D2_K2_XOR)

        for i in P_keys.keys():
            idx = i 
            for val in P_keys.values():
                if(idx == P_keys[val]):
                    self._P_REVERSE.append(val)
                    continue
        print("\n")

        print("* Et voici l'inverse de P: ", *self._P_REVERSE)
        print("\n")

        D2_K2_XOR_INDEXED = dict()
        D2_K2_XOR_INDEXED = self.get_8_bits_Indexes(D2_K2_XOR) # Une table des indexes de C
        
        for i in self._P_REVERSE:
            idx = i
            for val in D2_K2_XOR_INDEXED.keys():
                if(idx == val):
                    self._G1.append(D2_K2_XOR_INDEXED[val])
                    continue
        print("__________________________________________")
        print("* La valeur de G1 est : ", *self._G1)
        print("__________________________________________")

    def calculate_D1(self, public_key) -> None:
        G1_OR_K2 = self.apply_or_operator(self._G1, public_key)
        self._D1 = self.apply_xor_operator(self._G1, G1_OR_K2)
        print("\n")
        
        print("__________________________________________")
        print("* La valeur de D1 est : ", self._D1)
        print("__________________________________________")

    def apply_xor_operator(self, list1:list, list2:list) -> list:
        result = list()
        i = 0
        j = 0
        while i < len(list1):
            while j < len(list2):
                result.append(operator.xor(list1[j], list2[j]))
                j = j + 1
            i = i + 1
        return result

    def apply_or_operator(self, list1:list, list2:list) -> list:
        result = list()
        i = 0
        j = 0
        while i < len(list1):
            while j < len(list2):
                result.append(operator.or_(list1[j], list2[j]))
                j = j + 1
            i = i + 1
        return result

    def calculate_second_round(self, P, private_key) -> None:
        self.calculate_Go(P, private_key)
        self.calculate_Do(private_key)

    def calculate_Go(self, P, k1) -> None:
        D1_K1 = self.apply_xor_operator(self._D1, k1)
        D1_K1_INDEXED = dict()
        D1_K1_INDEXED = self.get_4_bits_Indexes(D1_K1)

        for i in self._P_REVERSE:
            idx = i
            for val in D1_K1_INDEXED.keys():
                if(idx == val):
                    self._Go.append(D1_K1_INDEXED[val])
                    continue
        print("\n")
        print("__________________________________________")
        print("* La valeur de Go est : ", *self._Go)
        print("__________________________________________")

    def calculate_Do(self, k1) -> None:
        Go_K1 = self.apply_or_operator(self._Go, k1)
        self._Do = self.apply_xor_operator(self._G1, Go_K1)
        print("\n")
        print("__________________________________________")
        print("* La valeur de Do est : ", *self._Do)
        print("__________________________________________")

    def calculate_N(self) -> None:
        self._N = self._Go + self._Do
        print("\n")
        print("__________________________________________")
        print("* Le bloc N vaut : ", *self._N)
        print("__________________________________________")

    def calculate_PI_reverse_on_N(self) -> None:
        PI_keys = dict()
        PI_keys = self.get_8_bits_Indexes(self._PI) # Une table de permutation 
        N_keys = list()
        N_keys = self.get_8_bits_Indexes(self._N)

        print("* PI keys : ", *PI_keys.keys())
        print("* PI values : ", *PI_keys.values())

        for i in PI_keys.keys():
            idx = i
            for val in PI_keys.values():
                if(idx == PI_keys[val]):
                    self._PI_REVERSE.append(val)
                    continue
        print("\n")
        
        print("* L'inverse de PI est : ", *self._PI_REVERSE)
        print("\n")
        
        for i in self._PI_REVERSE:
            idx = i
            for val in N_keys.keys():
                if(idx == val):
                    self._N_PERMUTED.append(N_keys[val])
                    continue
        print("__________________________________________")
        print("* Le Texte clair est : ", *self._N_PERMUTED)
        print("__________________________________________")