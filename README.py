# meus-exercicios-python-iniciante - 10
# São questões simples para minha pessoa ter uma ser noção do meu progresso. 

dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

print(f"Dias da semana em funcionamento: {', '.join(dias_da_semana)}")

dia_escolhido = input("Digite o dia da semana: ").lower()

if dia_escolhido in dias_da_semana:
    print(f"Está em funcionamento na {dia_escolhido}.")

elif dia_escolhido == "sábado" or dia_escolhido == "domingo":
    print("Não está em funcionamento neste dia.")


else:
    print("Dia inválido. Por favor, digite um dia da semana válido.")

# Mais completo logo abaixo...

dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

print(f"Dias da semana em funcionamento: {', '.join(dias_da_semana)}") # utilizando join para exibir os dias da semana em funcionamento. Ou podemos utilizar o for para exibir os dias da semana em funcionamento. Ex:

#for dia in dias_da_semana:
#    print(f"Está em funcionamento na {dia}.")

dia_escolhido = input("Digite o dia da semana: ").lower()

if dia_escolhido in dias_da_semana:
    print(f"Está em funcionamento na {dia_escolhido}.")

elif dia_escolhido == "sábado" or dia_escolhido == "domingo":
    print("Não está em funcionamento neste dia.")


else:
    print("Dia inválido. Por favor, digite um dia da semana válido.")

print(', '.join(dias_da_semana))

print()

dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

for dia in dias_da_semana:
    print(f"Está em funcionamento na {dia}.")
