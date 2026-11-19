# Lista dos dias em que o estabelecimento está em funcionamento.
dias_em_funcionamento = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
]

# Exibe os dias da lista em uma única linha, separados por vírgulas.
print(
    "Dias da semana em funcionamento: "
    + ", ".join(dias_em_funcionamento)
)

# Pede ao usuário um dia da semana.
# lower() transforma as letras em minúsculas e strip() remove espaços extras.
dia_escolhido = input("Digite o dia da semana: ").lower().strip()

# Verifica se o dia digitado está na lista de dias de funcionamento.
if dia_escolhido in dias_em_funcionamento:
    print(f"Está em funcionamento na {dia_escolhido}.")

# Verifica se o dia digitado é sábado ou domingo.
elif dia_escolhido in ["sábado", "domingo"]:
    print("Não está em funcionamento neste dia.")

# Executa este bloco se o dia digitado não estiver entre os dias reconhecidos.
else:
    print("Dia inválido. Por favor, digite um dia da semana válido.")

# Pula uma linha para separar as mensagens.
print()

# Percorre cada dia da lista e exibe uma mensagem para ele.
for dia in dias_em_funcionamento:
    print(f"Está em funcionamento na {dia}.")
