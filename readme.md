
# Dashboard de Empresas Tóxicas do Brasil

Este projeto consiste em um dashboard simples que analisa uma planilha do Google Sheets para identificar as empresas mais mencionadas em relação a comportamentos tóxicos no ambiente de trabalho. Ele permite aos usuários visualizar a contagem de ocorrências de palavras-chave específicas em relação a cada empresa listada na planilha.

[EMPRESAS TÓXICAS BRASIL](https://opensource.org/licenses/MIT](https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/htmlview).
[EMPRESAS TÓXICAS BRASIL - FORMULÁRIO](https://docs.google.com/forms/d/e/1FAIpQLSdsmCP5YB4zgtfhR5xLFeqoCMDBVVcNLe2KIzAdJelwPs5-1A/viewform).

## Funcionalidades

- **Análise de Planilha:** O dashboard analisa uma planilha do Google Sheets para extrair dados sobre as empresas e as ocorrências de palavras-chave relacionadas a comportamentos tóxicos no ambiente de trabalho.

- **Tradução de Nomes de Empresas:** Utiliza um dicionário para traduzir diferentes variações de nomes de empresas para um valor padrão, facilitando a análise e a comparação entre empresas.

- **Filtragem por Ocorrência de Palavras-chave:** Permite aos usuários filtrar as ocorrências de palavras-chave, como "racismo", "machismo", "assédio", entre outras, para visualizar a contagem dessas ocorrências para cada empresa listada.

## Requisitos

- Python 3.x
- Bibliotecas Python: pandas, plotly, streamlit, nltk
- Conta no Google para acessar a planilha

## Instalação e Uso

1. Clone o repositório para o seu ambiente local:

```
git clone https://github.com/megapala2/Toxicas.git
```

2. Instale as dependências do projeto:

```
pip install pandas plotly streamlit nltk
```

3. Execute o aplicativo Streamlit:

```
streamlit run app.py
```

4. O navegador padrão será aberto exibindo o dashboard. Explore as empresas e as ocorrências de palavras-chave usando os filtros fornecidos.

## Observações

- Certifique-se de ter permissão de acesso à planilha do Google Sheets. Caso contrário, o aplicativo não poderá extrair os dados corretamente.

- O dicionário utilizado para traduzir os nomes das empresas pode ser atualizado conforme necessário para incluir mais variações ou empresas adicionais.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

Lembre-se de substituir `seu-usuario` e `nome-do-repositorio` com seu nome de usuário do GitHub e o nome do repositório, respectivamente. Adapte as instruções de instalação e uso conforme necessário para refletir a estrutura do seu projeto.
