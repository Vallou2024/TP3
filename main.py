import random as rd

class Jeu:
  def __init__(self, m, n):
    """
    Constructeur de la classe Jeu.

    Parameters:
        m (int): La limite supérieure pour le tirage.
        n (int): Le nombre d'essais maximal

    """
    self.k = rd.randint(0, m)
    self.n = n

  def test(self, k):
    """
    Compare le nombre deviné avec le nombre à deviner.

    Parameters:
        guess (int): Le nombre à deviner.

    Returns:
        bool: True si les nombres sont égaux, False sinon.
    """
    if k != self.k:
      if k < self.k:
        print("Trop Petit")
      if k > self.k:
        print("Trop Grand")
      return False
    else:
      print("Bravo tu as gagne")
    return True




if __name__ == '__main__':
  import doctest
  doctest.testmod()