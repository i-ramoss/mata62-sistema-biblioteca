from ..Usuario import Usuario
from ..Livro import Livro 

class Reserva():
    def __init__(self, usuario: Usuario, livro: Livro):
        self.__usuario = usuario
        self.__livro = livro 

