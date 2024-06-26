# Dashboard de Empresas Tóxicas do Brasil

Este projeto consiste em um dashboard simples que analisa uma planilha do Google Sheets para identificar as empresas mais mencionadas em relação a comportamentos tóxicos no ambiente de trabalho. Ele permite aos usuários visualizar a contagem de ocorrências de palavras-chave específicas em relação a cada empresa listada na planilha.

[EMPRESAS TÓXICAS BRASIL](https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/htmlview).

[EMPRESAS TÓXICAS BRASIL - FORMULÁRIO](https://docs.google.com/forms/d/e/1FAIpQLSdsmCP5YB4zgtfhR5xLFeqoCMDBVVcNLe2KIzAdJelwPs5-1A/viewform).

## Funcionalidades

- **Análise de Planilha:** O dashboard analisa uma planilha do Google Sheets para extrair dados sobre as empresas e as ocorrências de palavras-chave relacionadas a comportamentos tóxicos no ambiente de trabalho.

- **Tradução de Nomes de Empresas:** Utiliza um dicionário para traduzir diferentes variações de nomes de empresas para um valor padrão, facilitando a análise e a comparação entre empresas.

- **Filtragem por Ocorrência de Palavras-chave:** Permite aos usuários filtrar as ocorrências de palavras-chave, como "racismo", "machismo", "assédio", entre outras, para visualizar a contagem dessas ocorrências para cada empresa listada.

## Requisitos

- Python 3.x
- Bibliotecas Python: pandas, plotly, streamlit, fuzzywuzzy

## Instalação e Uso

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/megapala2/Toxicas.git
```

2. Instale as dependências do projeto:

```
pip install pandas plotly streamlit fuzzywuzzy
```

3. Execute o aplicativo Streamlit:

```
streamlit run app.py
```

4. O navegador padrão será aberto exibindo o dashboard. Explore as empresas e as ocorrências de palavras-chave usando os filtros fornecidos.

## Observações

- O dicionário utilizado para traduzir os nomes das empresas pode ser atualizado conforme necessário para incluir mais variações ou empresas adicionais.
  

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.
Principalmente para adicionar novas empresas na lista!

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).



