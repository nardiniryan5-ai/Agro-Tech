# Entrega Final AgroTech Grupo G

Data de consolidação: 19 de novembro de 2026.

## Integrantes

- Ryan Nardini Pereira
- Rafael Henrique Trajano
- Isaque Rodrigues

## Conteúdo entregue

- Aplicação Python de terminal em `main.py`.
- Base de insumos em `dados.csv`.
- Testes automatizados em `tests/test_main.py`.
- README com instalação, execução e testes.
- Levantamento de requisitos em PDF.
- Relatório de testes em PDF.
- Proposta comercial em PDF.
- Apresentação em PowerPoint com seis slides.
- Vídeo institucional de aproximadamente um minuto.
- Logotipo, paleta e imagens institucionais.

## Validação final

```bash
python -m unittest discover -s tests -v
python -m py_compile main.py
```

Resultado registrado: 7 testes executados e 7 aprovados.

## Execução

```bash
python main.py
```

## Limitações conhecidas

- Os estados dos quadrantes permanecem somente durante a execução atual.
- A versão entregue funciona no terminal e não possui autenticação ou interface web.
- O PowerPoint e `video-institucional.mp4` devem permanecer juntos na pasta `docs/apresentacao` para preservar o link do terceiro slide.
- Não foram criados commits, conforme orientação do responsável pelo projeto.
