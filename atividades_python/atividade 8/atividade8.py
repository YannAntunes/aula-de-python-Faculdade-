# 8. Desenvolva um algoritmo que pergunte ao usuario o estado civil
# (solteiro, casado, divorciado, viuvo) e exiba uma mensagem correspondente.

estado_civil = input("Digite seu estado civil (solteiro, casado, divorciado, viuvo): ").strip().lower()

if estado_civil == "solteiro":
    print("Voce e solteiro(a). Aproveite sua liberdade!")
elif estado_civil == "casado":
    print("Voce e casado(a). Que sua uniao seja duradoura!")
elif estado_civil == "divorciado":
    print("Voce e divorciado(a). Novos comecos podem ser emocionantes!")
elif estado_civil == "viuvo":
    print("Voce e viuvo(a). Nossas condolencias.")
else:
    print("Estado civil invalido.")
