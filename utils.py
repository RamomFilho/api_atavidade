from models import Pessoas


#Insere dados na Table pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Filho', idade=25)
    print(pessoa)
    pessoa.save()


#Consulta dados na Table pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Cartillo').first()
    print(pessoa.idade)


#Altera dados na Table pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ramom').first()
    pessoa.nome = 'Cartillo'
    pessoa.save()


#Exlui dados na Table pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Cartillo').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
