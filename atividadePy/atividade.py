from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,Colaborador, NomeColaborador, Idade, Departamento, NomeProjeto, Projeto, Alocacoes, ParticipandeDe, DepartamentoColaborador, InfoGeral')

with open('colaboradores.txt') as file:
    for line in file:
        nomeColaborador, idade, departamento = line.strip().split(',')
        +Colaborador(nomeColaborador, idade, departamento)

with open('projetos.txt') as file:
    for line in file:
        nomeProjeto, departamento = line.strip().split(',')
        +Projeto(nomeProjeto, departamento)

with open('alocacoes.txt') as file:
    for line in file:
        nomeColaborador, projeto = line.strip().split(',')
        +Alocacoes(nomeColaborador, projeto)

ParticipanteDe = Alocacoes(NomeColaborador, Projeto)
print(ParticipanteDe)

print('\n///////////////\n')

DepartamentoColaborador(NomeColaborador, Departamento) <= Colaborador(NomeColaborador, Idade, Departamento)

print(DepartamentoColaborador(NomeColaborador,Departamento))

print('\n///////////////\n')

InfoGeral(NomeColaborador, Projeto, Departamento) <= Colaborador(NomeColaborador, Projeto, Departamento) 

print(InfoGeral(X,Y,Z))





'''
print("Colaboradores:\n")
for n, i, d in Colaborador(NomeColaborador, Idade, Departamento):
    print(n)

print('\n//////////////////////////////\n')

print('Projetos: \n')
for n, d in Projeto(NomeProjeto, Departamento):
    print(n)
'''