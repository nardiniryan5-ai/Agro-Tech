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
		"localizacao": "Fazenda Horizonte, Itapecerica da Serra" - SP",
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

