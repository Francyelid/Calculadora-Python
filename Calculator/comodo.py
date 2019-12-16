Aprenda
Comunidade
Vagas
LiveChat
Buscar

ASSINE
4
Larissa
Larissa
Olá
Larissa
Nível: Iniciante
MINHA
CONTA
Assine
Perfil
Meus
Cursos
Favoritos
Logout
Indique
um
amigo
Voltar
Curso
de
Python
Download
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37


class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('o valor informado da largura é inválido')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('o valor informado da profundidade é inválido')
            exit()

