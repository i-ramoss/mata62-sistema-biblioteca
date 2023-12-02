from .Livro import Livro

class Exemplar():
    def __init__(self, codigo:int, status:str, livro: Livro):
        self.__codigo = codigo
        self.__status = status
        self.__livro = livro 
