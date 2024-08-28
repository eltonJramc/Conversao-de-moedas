# Projeto: Conversão de Moedas

## Descrição
O projeto "Conversão de Moedas" é um programa desenvolvido em Python que permite a conversão de valores entre diferentes moedas utilizando uma API para obter as cotações mais recentes. Além disso, o projeto oferece a visualização das cotações através de gráficos, possibilitando uma análise comparativa entre as moedas selecionadas.

## Funcionalidades
- **Conversão de Moedas:** Converte valores de uma moeda de origem para uma moeda de destino utilizando as taxas de câmbio mais atualizadas.
- **Visualização Gráfica:** Gera gráficos de barras, pizza e dispersão para comparar visualmente as taxas de câmbio entre as moedas selecionadas.

## Tecnologias Utilizadas
- **Python 3.8+**
- **Bibliotecas:** 
  - `requests`: Utilizada para fazer requisições HTTP e obter os dados de cotação da API.
  - `matplotlib`: Utilizada para a criação dos gráficos de comparação das cotações.

## Como Funciona
1. **Obtenção das Cotações:** O programa utiliza a API [ExchangeRate-API](https://www.exchangerate-api.com/) para obter as cotações mais recentes das principais moedas em relação ao Real (BRL).
2. **Conversão:** O usuário pode converter valores de USD, EUR e GBP para BRL ou escolher outras moedas de origem e destino.
3. **Visualização:** O usuário pode optar por visualizar as cotações em diferentes tipos de gráficos: barra, pizza ou dispersão.

## Estrutura do Projeto
- **`moedas.py`**: Módulo responsável por obter as cotações das moedas através da API e realizar a conversão.
- **`conversao.py`**: Interface de linha de comando para a conversão de moedas.
- **`index_grafico.py`**: Interface de linha de comando para a geração dos gráficos.
- **`graficos.py`**: Módulo responsável por gerar os gráficos utilizando a biblioteca `matplotlib`.
