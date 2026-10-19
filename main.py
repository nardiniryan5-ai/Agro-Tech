empresa = {
	"nome": "AgroTech",
	"razao_social": "AgroTech Tecnologia Agricola Ltda.",
	"segmento": "Agronegócio e tecnologia de aplicação com drones",
	"descricao": "Controle de plantações e gestão de insumos para operações com drones.",
	"endereco": {
		"cidade": "Itapecerica da Serra",
        "estado": "São Paulo",
		"email": "contato@agrotech.com",
		"telefone": "55+ (11) 99999-9999",
	},
}

plantacoes = [
	{
		"id": 1,
		"nome": "Talhão Norte",
		"cultura": "Soja",
		"area_hectares": 42.5,
		"localizacao": "Fazenda Horizonte, São Paulo - SP",
		"status": "em operação",
		"data_plantio": "2026-09-15",
	},
	{
		"id": 2,
		"nome": "Talhão Sul",
        "cultura": "Soja",
		"localizacao": "Fazenda Horizonte, Itapecerica da Serra - SP",
		"status": "em operação",
		"data_plantio": "2026-08-20",
	},
]

drones = [
	{
		"id": "DR-001",
		"modelo": "DJI Agras T50",
		"capacidade_tanque_litros": 10,
		"status": "disponivel",
		"horas_voo": 125.5,
	},
	{
		"id": "DR-002",
		"modelo": "DJI Agras T100",
		"capacidade_tanque_litros": 20,
		"status": "em_manutencao",
		"horas_voo": 318.0,
	},
]

insumos = [
	{
		"id": "INS-001",
		"nome": "Fertilizante foliar",
		"categoria": "fertilizante",
		"unidade": "litro",
		"estoque_atual": 240,
		"estoque_minimo": 50,
		"compativel_com_aplicacao_por_drone": True,
	},
	{
		"id": "INS-002",
		"nome": "Biofungicida",
		"categoria": "defensivo_biologico",
		"unidade": "litro",
		"estoque_atual": 80,
		"estoque_minimo": 30,
		"compativel_com_aplicacao_por_drone": True,
	},
]

quadrantes_por_plantacao = 4
estados_validos = ["pendente", "em aplicação", "concluído"]

# Cada linha representa um talhão; cada coluna representa um quadrante.
matriz_estado = [
	["pendente" for _ in range(quadrantes_por_plantacao)]
	for _ in plantacoes
]


def atualizar_estado(talhao, quadrante, novo_estado):
	if talhao >= 1 and talhao <= len(plantacoes):
		if quadrante >= 1 and quadrante <= quadrantes_por_plantacao:
			if novo_estado in estados_validos:
				matriz_estado[talhao - 1][quadrante - 1] = novo_estado
			else:
				print("Estado inválido.")
		else:
			print("Quadrante inválido.")
	else:
		print("Talhão inválido.")


def exibir_matriz_estado():
	print("Estado dos quadrantes das plantações")
	print(f"{'Talhão':<16}", end="")
	for quadrante in range(1, quadrantes_por_plantacao + 1):
		print(f"{'Quadrante ' + str(quadrante):<16}", end="")
	print()

	for indice_talhao in range(len(plantacoes)):
		print(f"{plantacoes[indice_talhao]['nome']:<16}", end="")
		for estado in matriz_estado[indice_talhao]:
			print(f"{estado:<16}", end="")
		print()


exibir_matriz_estado()

def menu():
    while True:
        print("\n===== AgroTech =====")
        print("[1] Ver dados da empresa")
        print("[2] Ver plantações")
        print("[3] Ver drones")
        print("[4] Ver insumos")
        print("[5] Ver matriz de estado")
        print("[6] Atualizar estado de quadrante")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\nEmpresa:", empresa["nome"])
            print("Segmento:", empresa["segmento"])
            print("Cidade:", empresa["endereco"]["cidade"])

        elif opcao == "2":
            for plantacao in plantacoes:
                print("\nID:", plantacao["id"])
                print("Nome:", plantacao["nome"])
                print("Cultura:", plantacao["cultura"])
                print("Status:", plantacao["status"])

        elif opcao == "3":
            for drone in drones:
                print("\nID:", drone["id"])
                print("Modelo:", drone["modelo"])
                print("Status:", drone["status"])
                print("Horas de voo:", drone["horas_voo"])

        elif opcao == "4":
            for insumo in insumos:
                print("\nNome:", insumo["nome"])
                print("Estoque atual:", insumo["estoque_atual"], insumo["unidade"])
                print("Estoque mínimo:", insumo["estoque_minimo"])

        elif opcao == "5":
            exibir_matriz_estado()

        elif opcao == "6":
            talhao = input("Digite o número do talhão (1 ou 2): ")
            quadrante = input("Digite o quadrante (1 a 4): ")

            if talhao.isdigit() and quadrante.isdigit():
                talhao = int(talhao)
                quadrante = int(quadrante)

                print("\n[1] Pendente")
                print("[2] Em aplicação")
                print("[3] Concluído")

                estado = input("Escolha o novo estado: ")

                if estado == "1":
                    atualizar_estado(talhao, quadrante, "pendente")
                elif estado == "2":
                    atualizar_estado(talhao, quadrante, "em aplicação")
                elif estado == "3":
                    atualizar_estado(talhao, quadrante, "concluído")
                else:
                    print("Opção de estado inválida.")
            else:
                print("Digite apenas números no talhão e quadrante.")

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()