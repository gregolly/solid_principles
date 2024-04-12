from abc import ABC, abstractmethod

class Exame(ABC):
    @abstractmethod
    def verifica_condicoes(self):
        pass

class ExameSangue(Exame):
    def verifica_condicoes(self):
        # implemente as condições específicas do exame de sangue
        pass

class ExameRaioX(Exame):
    def verifica_condicoes(self):
        # implemente as condições específicas do exame de raio-x
        pass

class AprovaExame:
    def aprovar_solicitacao_exame(self, exame):
        if exame.verifica_condicoes():
            print(f"Exame {type(exame).__name__} aprovado!")

# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
print(aprovador.aprovar_solicitacao_exame(exame_sangue))
print(aprovador.aprovar_solicitacao_exame(exame_raio_x))