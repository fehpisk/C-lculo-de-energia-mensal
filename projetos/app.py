aparelho = input("Informe qual o seu aparelho: ")
potencia = float(input ("Informe a potencia do seu aparelho em watts (W): "))
tempo_uso = float(input ("Informe o tempo medio de uso diario do aparelho (em horas): "))


consumoMensal = potencia * tempo_uso * 30 / 1000
custoEstimado = consumoMensal * 0.75

print(f"\n --- Calculo de consumo mensal: --- ")
print(f"Aparelho: {aparelho}.")
print(f"Consumo estimado: {consumoMensal:.2f} KWh/mes.")
print(f"Custo estimado: R${custoEstimado:.2f}.")