from abc import ABC, abstractmethod

class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

class ExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Exame sanguíneo aprovado!")

    def verifica_condicoes_exame(self, exame):
        pass

class RaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Raio-x aprovado!")
            
    def verifica_condicoes_exame(self, exame):
        pass

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

sangue = Exame("sangue")
raio_x = Exame("raio-x")
print(sangue)
print(raio_x)

aprovador_sangue = ExameSangue()
aprovador_raio_x = RaioX()

print(aprovador_sangue.aprovar_solicitacao_exame(sangue))
print(aprovador_raio_x.aprovar_solicitacao_exame(raio_x))