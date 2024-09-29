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
