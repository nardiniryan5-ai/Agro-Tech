2° F-DS
Ryan Nardini Pereira
Isaque Rodrigues Da Silva
Rafael Henrique Trajano

Agronegócio: Controle de plantação e insumos para drones

# AgroTech Grupo G

Plataforma em Python para controle de plantações, quadrantes operacionais, drones agrícolas e estoque de insumos. O projeto funciona no terminal e utiliza um arquivo CSV para consolidar os dados de estoque.

## Funcionalidades

- Consulta dos dados institucionais da AgroTech.
- Listagem de plantações, drones e insumos.
- Matriz bidimensional com quatro quadrantes por talhão.
- Atualização validada dos estados `pendente`, `em aplicação` e `concluído`.
- Leitura e validação do arquivo `dados.csv`.
- Painel consolidado com totais de quadrantes, estados e estoque.
- Bateria automatizada de testes para o menu, a matriz e o CSV.

## Requisitos

- Python 3.10 ou superior.
- Terminal local ou GitHub Codespaces.

O projeto utiliza somente módulos da biblioteca padrão do Python e não exige instalação de pacotes.

## Como executar

No terminal, abra a pasta do projeto e execute:

```bash
python main.py
```

O caminho do CSV é resolvido a partir da localização do programa, portanto o comando também pode ser executado a partir de outro diretório:


## Menu

| Opção | Ação |
| --- | --- |
| 1 | Ver dados da empresa |
| 2 | Ver plantações |
| 3 | Ver drones |
| 4 | Ver insumos |
| 5 | Ver matriz de estado |
| 6 | Atualizar estado de quadrante |
| 7 | Exibir painel consolidado |
| 0 | Encerrar o sistema |

Entradas vazias, opções inexistentes e valores não numéricos são tratados sem interromper o programa.

## Dados do CSV

O arquivo `dados.csv` deve permanecer na raiz e conter as colunas abaixo:

```text
id,categoria,marca,nome,estoque,unidade,validade
```

O painel rejeita cabeçalhos incompletos, estoques não numéricos e valores negativos.

## Como testar

Execute a suíte completa:

```bash
python -m unittest discover -s tests -v
```

Valide também a sintaxe:

```bash
python -m py_compile main.py
```

O relatório da execução está disponível em `docs/relatorio-de-testes-agrotech.pdf`.

## Estrutura do projeto

```text
Agro-tech/
├── dados.csv
├── main.py
├── README.md
├── assets/
│   ├── brand/
│   │   └── agrotech-logo.png
│   └── images/
│       ├── campo-agrotech.jpg
│       ├── drones-agrotech.jpg
│       └── insumos-agrotech.jpg
├── docs/
│   ├── apresentacao/
│   │   ├── apresentacao-agrotech-grupo-g.pptx
│   │   └── video-institucional.mp4
│   ├── comercial/
│   │   └── proposta-comercial-agrotech.pdf
│   ├── identidade-visual.md
│   ├── requisitos/
│   │   └── levantamento-de-requisitos-agrotech.pdf
│   └── relatorio-de-testes-agrotech.pdf
└── tests/
    └── test_main.py
```

## Participação da equipe

As responsabilidades foram distribuídas conforme o planejamento acadêmico do grupo:

- Aluno 1: cadastro da empresa, entidades base e preparação dos dados operacionais em CSV.
- Aluno 2: matriz bidimensional dos quadrantes e leitura sequencial dos dados.
- Aluno 3: menu interativo, validações, painel consolidado e regras de negócio.
- Consolidação final: testes automatizados, relatório técnico e documentação de execução.

Os nomes dos integrantes devem ser acrescentados pela equipe quando forem disponibilizados.

## Limitações conhecidas

- Os estados dos quadrantes ficam em memória e são reiniciados ao encerrar o programa.
- Os custos não fazem parte do CSV atual.
- A versão entregue é uma aplicação de terminal; o vídeo institucional apresenta uma visão conceitual da solução.
