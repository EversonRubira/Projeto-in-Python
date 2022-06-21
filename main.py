class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        
    @classmethod
    def agenda(self):
        notificacao = NotificarCliente()
        return notificacao.notifica(self.nome)

class NotificarCliente:
    def notifica(self, cliente):
        return cliente + " Next meeting will be postponed"
        
# SRP - Single Responsability Principle
# S.O.L.I.D Orientacao a Objetos

cliente = Cliente('Everson', '123.456.789-00', 'desenvolvedor')
print(cliente.nome)
print(cliente.cpf)
print(cliente.profissao)
print(cliente.agenda())

