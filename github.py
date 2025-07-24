# Biblioteca pra rodar comandos no terminal
import os

email = "rafael.zottesso@ifpr.edu.br"

print(f"Seu email é: {email}")

# Verifica com o usuário se o email está correto

msg_commit = input("\nMensagem do commit: ")
while( len(msg_commit) <= 10 ):
    print("Detalhe mais sua mensagem!")
    msg_commit = input("Mensagem do commit: ")

print("------------------------------")
print("Iniciando processos do Git...")
print("------------------------------")

# Executar os comandos do git no terminal
    
# Configurar o email
c = f"git config user.email \"{email}\"  "
os.system(c)

# Identificar as novidades e incluir no commit
c = f"git add *"
os.system(c)

# Registrar o commit com uma mensagem
c = f"git commit -m \"{msg_commit}\"  "
os.system(c)

# Enviar para os servidores do GitHub
c = "git push"
os.system(c)