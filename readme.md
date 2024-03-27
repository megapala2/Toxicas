Dashboard de Empresas Tóxicas do Brasil
Este projeto consiste em um dashboard simples que analisa uma planilha do Google Sheets para identificar as empresas mais mencionadas em relação a comportamentos tóxicos no ambiente de trabalho. Ele permite aos usuários visualizar a contagem de ocorrências de palavras-chave específicas em relação a cada empresa listada na planilha.

Funcionalidades
Análise de Planilha: O dashboard analisa uma planilha do Google Sheets para extrair dados sobre as empresas e as ocorrências de palavras-chave relacionadas a comportamentos tóxicos no ambiente de trabalho.

Tradução de Nomes de Empresas: Utiliza um dicionário para traduzir diferentes variações de nomes de empresas para um valor padrão, facilitando a análise e a comparação entre empresas.

Filtragem por Ocorrência de Palavras-chave: Permite aos usuários filtrar as ocorrências de palavras-chave, como "racismo", "machismo", "assédio", entre outras, para visualizar a contagem dessas ocorrências para cada empresa listada.

Requisitos
Python 3.x
Bibliotecas Python: pandas, plotly, streamlit, nltk
Conta no Google para acessar a planilha
Instalação e Uso
Clone o repositório para o seu ambiente local:
bash
Copy code
git clone https://github.com/megapala2/Toxicas
Instale as dependências do projeto:
Copy code
pip install pandas plotly streamlit nltk
Execute o aplicativo Streamlit:
arduino
Copy code
streamlit run app.py
O navegador padrão será aberto exibindo o dashboard. Explore as empresas e as ocorrências de palavras-chave usando os filtros fornecidos.
Observações
Certifique-se de ter permissão de acesso à planilha do Google Sheets. Caso contrário, o aplicativo não poderá extrair os dados corretamente.

O dicionário utilizado para traduzir os nomes das empresas pode ser atualizado conforme necessário para incluir mais variações ou empresas adicionais.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests com melhorias, correções de bugs ou novas funcionalidades.

Licença
Este projeto está licenciado sob a MIT License.