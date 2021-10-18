horaAtual = int(input("Informe a hora atual: "))
minutoAtual = int(input("Informe o minuto atual: "))
segundoAtual = int(input("Informe o segundo atual: "))

duracaohrs = int(input("Informe a duração em horas: "))
duracaoMin = int(input("Informe a duração em minuto: "))
duracaoSeg = int(input("Informe a duração em segundo: "))

print(f"Horário atual: {horaAtual + duracaohrs} : {minutoAtual + duracaoMin} : {segundoAtual + duracaoSeg}")