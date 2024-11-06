from pyDatalog import pyDatalog

pyDatalog.create_terms('X,Y,Z,Colaborador, NomeColaborador, Idade, Departamento, Projeto, NomeProjeto, Alocacoes, ParticipanteDe, DepartamentoColaborador, InfoGeral, Senior, Quantidade_seniores')

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

#ATIVIDADE1

# print("Colaborador")
# for n,i,d in Colaborador(NomeColaborador, Idade, Departamento):
#     print(n)

# print('\n/////////////////////////\n')
# print("Projeto")
# for n, d in Projeto(NomeProjeto, Departamento):
#     print(n)


#ATIVIDADE 2

#ParticipanteDe(NomeColaborador, NomeProjeto) <= Alocacoes(NomeColaborador, NomeProjeto)

#print(ParticipanteDe(X, Y))

# DepartamentoColaborador(NomeColaborador, Departamento) <= Colaborador(NomeColaborador, Idade, Departamento)
# # print(DepartamentoColaborador(X,Y))

# #InfoGeral(NomeColaborador, NomeProjeto, Departamento) <= ParticipanteDe(NomeColaborador, NomeProjeto) & DepartamentoColaborador(NomeColaborador, Departamento)
# #print(InfoGeral(X,Y,Z))


# #ATIVIDADE 3

# Senior(NomeColaborador) <= Colaborador(NomeColaborador, Idade, Departamento) & (Idade>"30")

# # for nomeColaborador, departamento in DepartamentoColaborador(X,Y) & Senior(X):
# #     print(f'{nomeColaborador} - {departamento}')

# for departamento in DepartamentoColaborador(X,Y) & Senior(X):
#     quantidade_seniores = len(Senior(X) & DepartamentoColaborador(X,Y))
#     print(f'{departamento} - {quantidade_seniores}')