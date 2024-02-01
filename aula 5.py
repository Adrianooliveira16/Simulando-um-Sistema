# #crie um sistema onde o usuario precisa digitar uma senha para acessar uma informação

# input()
# print()
# 4 tipos primitivos

##indentação - organizar o seu codigo
#ordem de hierarquia
#{} () :
#if, else, elif

senha_usuario = input('Digite a senha: ')
senha_do_sistema = '123'

if senha_usuario == senha_do_sistema:
  print('Acesso autorizado')
else:
  print('Acesso negado')
  
# linha 22 a 27 guardando dados nas variaveis

nome_usuario = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
endereco = ('digite endereço: ')
curso = input('digite seu curso: ')
email_usuario = input('digite seu email: ')
senha_usuario = input('digite sua senha ')

# linha 31 a 34 simulando um sistema

print('...................................')
print('olá para acessar o sistema digite sua senha')
acesso_senha = input('para acessar digite sua senha')
email_acesso = input('para acessar digite seu email')

#atenticação com condicional

if senha_usuario == acesso_senha and email_usuario == email_acesso:
  print('olá',nome_usuario)
  print('seus dados são os seguintes:')
  print('..........................')
  print('sua idade é ',idade)
  print('seu endereço é',endereco)
  print('o curso escolhido foi:',curso)
else:
  print('voce digitou algo errado')
  