usuario = str (input('escolha um nome de usuario:'))
senha = int (input('escolha uma senha:'))
minhasenha= 2007
meuusuario= 'vitorzago'
print(senha == minhasenha)
if (usuario == meuusuario) and (senha == minhasenha):
    print('Seja bem vindo')
else:
    print('Usuario ou senha incorreta')

