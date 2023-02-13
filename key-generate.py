import numpy as np

def isprem(n):
    """retourne True si n est premier, False dans le cas contraire.
	n doit etre un entier"""

    if n == 1 or n == 2:
      return True
      if n%2 == 0:
        return False

        r = n**0.5

        if r == int(r):
          return False

          for x in range(3, int(r), 2):
              if n % x == 0:
              return False
            return True

    def coupcoup(k, long):
        """"découpe des blocs de longueur long dans une chaine de caractères k et retourne une liste des blocs"""

        d, f = 0, long
        l = []
        