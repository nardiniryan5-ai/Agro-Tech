quadrantes_por_plantacao = 4
estados_validos = {"pendente", "em aplicação", "concluído"}

# Cada linha representa um talhão; cada coluna representa um quadrante.
matriz_estado = [
	["pendente" for _ in range(quadrantes_por_plantacao)]
	for _ in plantacoes
]


def atualizar_estado(talhao, quadrante, novo_estado):
	if talhao < 1 or talhao > len(plantacoes):
		raise ValueError("Talhão inválido.")
	if quadrante < 1 or quadrante > quadrantes_por_plantacao:
		raise ValueError("Quadrante inválido.")
	if novo_estado not in estados_validos:
		raise ValueError(
			f"Estado inválido. Escolha entre: {', '.join(sorted(estados_validos))}."
		)

	matriz_estado[talhao - 1][quadrante - 1] = novo_estado


def exibir_matriz_estado():
	print("Estado dos quadrantes das plantações")
	print(f"{'Talhão':<16}" + "".join(
		f"{'Quadrante ' + str(indice):<16}"
		for indice in range(1, quadrantes_por_plantacao + 1)
	))

	for plantacao, estados in zip(plantacoes, matriz_estado):
		print(f"{plantacao['nome']:<16}" + "".join(
			f"{estado:<16}" for estado in estados
		))


exibir_matriz_estado()