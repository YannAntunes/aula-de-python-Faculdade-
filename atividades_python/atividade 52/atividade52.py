# 52. Desenvolva um algoritmo que solicite ao usuario uma senha e continue
# pedindo ate que a senha correta "1234" seja digitada.

print("Sistema de acesso seguro")

while True:
    senha = input("Digite a senha: ")
    if senha == "1234":
        print("Senha correta! Acesso liberado.")
        break
    else:
        print("Senha incorreta. Tente novamente.")
