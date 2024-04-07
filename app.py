import streamlit as st
import pandas as pd
import plotly.express as px
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import time
from pathlib import Path
import os

EMPRESAS = [
    "Wise System",
    "Accenture",
    "vhsys",
    "CI&T",
    "Nestlé",
    "IBM",
    "Stefanini",
    "Mottu",
    "Itaú",
    "Ambev",
    "Stone",
    "Nubank",
    "L'Oréal",
    "Atos Brasil",
    "Banco Daycoval",
    "Kabum",
    "Teleperformance",
    "99",
    "B3",
    "F1rst",
    "TOTVS",
    "DASA",
    "Deloitte",
    "Mercado livre",
    "Mundiale",
    "Thomson Reuters",
    "Softplan",
    "Vivo",
    "C6 Bank",
    "Gupy",
    "iFood",
    "Santander",
    "Bradesco",
    "Btg Pactual",
    "Hotmart",
    "Grão de Gente",
    "Mecanizou",
    "Creditas",
    "Dataprev",
    "Itaú Unibanco",
    "Locaweb",
    "Weme",
    "PicPay",
    "TIVIT",
    "Vaticano Crematório e Cemitério Sedes Paraná e Santa Catarina",
    "BLiP",
    "Fisk",
    "Gft",
    "Instituto Proa",
    "Kanastra",
    "MadeiraMadeira",
    "Americanas",
    "Banco Pan",
    "CERC",
    "Globo",
    "KPMG",
    "Valtech",
    "Group Software",
    "Unimed",
    "Wise",
    "Carrefour",
    "XP",
    "BRQ",
    "Serasa",
    "Wiz",
    "WB",
    "Zup",
    "Acuda",
    "Gerdau",
    "Isaac",
    "Ish",
    "4p",
    "Zurich",
    "Zamp",
    "Zenvia",
    "Yazaki",
    "Fadel",
    "Will Bank",
    "Weme",
    "Way2",
    "Vtex",
    "Visagio",
    "Vero",
    "V4",
    "UP BR",
    "UOL",
    "Ultrafarma",
    "Uber",
    "Tools",
    "Tokstok",
    "Tivit",
    "TIM",
    "Teleperformance",
    "Suno",
    "Squadra",
    "Softplan",
    "Sinergy RH",
    "Sicredi",
    "Shopee",
    "Senac",
    "Renner",
    "Raízen",
    "QuintoAndar",
    "PwC",
    "Porto Seguro",
    "Pepsico",
    "Pearson",
    "Osten Moove",
    "Oi",
    "NTT",
    "NOMAD",
    "Nissan",
    "Neon",




    









            ]

MOTIVOS = [
    'DIVERSIDADE',
    'ASSÉDIO(MORAL/SEXUAL)',
    'SALÁRIO/BENEFÍCIOS',
    'MICROGERENCIAMENTO',
    'COMUNICAÇÃO/TRANSPARÊNCIA',
    'POSSIBILIDADE DE CRESCIMENTO',
    'SEGURANÇA/SAÚDE',
    'FERRAMENTAS DE TRABALHO',
    'LIDERANÇA TÓXICA',
    'CARGA DE TRABALHO EXCESSIVA',
    'Outros'
]

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

def st_init():

    st.set_page_config(layout='wide', page_title='Worst to Work', page_icon="📊")

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.title("EMPRESAS TÓXICAS BRASIL")
    st.sidebar.image('https://exposedworkplaces.com/wp-content/uploads/2024/03/empresa_mais_toxicas_brazil.png')
    
    
    with st.sidebar.popover('Créditos'):
        criador_planilha = st.info('Criador da planilha: https://www.linkedin.com/in/andersonweber/')
        criador_dashboard = st.info('Criador desse dashbord: https://www.linkedin.com/in/thales-rudolph-b7511a16a/')
   

    with st.sidebar.popover('Fonte'):
        fonte = st.info("Planilha fonte: https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/htmlview")
        form = st.info('Formulário para preencher: https://docs.google.com/forms/d/e/1FAIpQLSdsmCP5YB4zgtfhR5xLFeqoCMDBVVcNLe2KIzAdJelwPs5-1A/viewform')
    
   
        
@st.cache_data
def save_df():

    try:

        df = pd.read_csv('https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/export?format=csv')
        try:   

            df = df.dropna(axis=1, how='all')     
            df = df.drop(df.columns[[3,4,6]], axis=1)

            df = df.rename(columns={df.columns[0]: 'Data', df.columns[1]: 'Empresa', df.columns[3]: 'Motivos' })

            
            #df = df.drop_duplicates(subset=['Empresa', 'Motivos'])

            df['Empresa'] =  df['Empresa'].astype(str)
            df['Motivos'] = df['Motivos'].astype(str)
            df['Empresa'] = df['Empresa'].str.lower().str.strip()
            df['Motivos'] = df['Motivos'].str.lower().str.strip()

            df['Contagem'] = df['Empresa'].map(df['Empresa'].value_counts())
            df['Match'] = df['Empresa'].apply(fuzzzz.find_matching_company)
            
            df = df.drop(df[df['Match'] == 'NA'].index)
            df = fuzzzz.verificar_ocorrencias(df)

            return df

        except:

            return st.warning('A formatação das colunas da planilha original mudou! Logo o código daqui morreu! X.X Por favor comunicar o dono desse dashboard!')
    
    except:
        
        return st.warning('A planilha original está interditada no momento! Erro ao extrair os dados!')

   

    

def motivos(df, novo_df):
    
    novo_df = novo_df.rename(columns={'Empresa': 'Match'})
    
    for motivo in MOTIVOS:

        contagem_motivo = df.groupby('Match')[motivo].sum().reset_index()
        novo_df = novo_df.merge(contagem_motivo, on='Match', how='left')
    
    return novo_df

@st.experimental_fragment
def chart(novo_df, df):

    container = st.container()
    colunas1, colunas2 = container.columns(2)

    empresas = colunas1.selectbox('Selecione a empresa!', options=EMPRESAS, index=None)

    opcoes = ['Contagem'] + MOTIVOS 
    escolha = colunas2.selectbox('Selecione a ocorrência!', options=opcoes)

  
    df['Empresa'] = df['Data']
    df['Data'] = df['Match']
    df = df.drop(columns='Match')
    df = df.rename(columns={'Data':'Match', 'Empresa':'Data'})
    df = df.drop(columns='Data')
    df = df.reset_index()

    if empresas:
        novo_df = novo_df[novo_df['Match'] == empresas]


    with container.expander("Dataframe"):
        st.info(f"Linhas: {len(novo_df)}")
        st.dataframe(novo_df, use_container_width=True)
        
        st.info(f"Linhas: {len(df)}")
        st.dataframe(df, use_container_width=True)

    if escolha:
       main_chart(novo_df, escolha, container)
       col1, col2 = container.columns(2)
       top3_chart(novo_df, escolha, col1)
       motivos_chart(novo_df, escolha, col2)


        

def main_chart(novo_df, escolha, container):

    df_filtro = novo_df.groupby('Match')[escolha].sum().reset_index(name=escolha)
    top20 = df_filtro.nlargest(20, escolha)
    novo_df = novo_df[novo_df['Match'].isin(top20['Match'])]


    fig = px.bar(
            novo_df, 
            x=novo_df[escolha], 
            y=novo_df['Match'], 
            text=novo_df['Match'],
            template='presentation',
            title=escolha,
            
        )

    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.update_layout(height=(800))
    
    fig.for_each_xaxis(lambda x: x.update(showgrid=True))
    
    fig.update_traces(
            marker_color = '#f75e5e', 
            marker_line_color = 'black',
            marker_line_width = 2, 
            opacity = 1
            )

    fig.update_traces(
            textfont_size=21, 
            textposition="inside",
            cliponaxis=False,
            insidetextanchor="middle",
            hovertemplate=None,
            textfont_color='#000000 '
        
        )
    
    fig.update_layout(
        
        title_font=dict(size=24),
        
    )
    
    container.plotly_chart(fig, use_container_width=True)

def top3_chart(novo_df, escolha, col1):

    df_filtro = novo_df.groupby('Match')[escolha].sum().reset_index(name=escolha)
    top3 = df_filtro.nlargest(3, escolha)
    novo_df = novo_df[novo_df['Match'].isin(top3['Match'])]


    fig = px.bar(
            novo_df, 
            x=novo_df['Match'], 
            y=novo_df[escolha], 
            text=novo_df['Match'],
            template='presentation',
            title='Top 3',
            orientation='v'
            
        )

    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.update_layout(height=(500))
    
    fig.for_each_xaxis(lambda x: x.update(showgrid=True))
    
    fig.update_traces(
            marker_color = '#f75e5e', 
            marker_line_color = 'black',
            marker_line_width = 2, 
            opacity = 1
            )

    fig.update_traces(
            textfont_size=21, 
            textposition="inside",
            cliponaxis=False,
            insidetextanchor="middle",
            hovertemplate=None,
            textfont_color='#000000 '
        
        )
    
    fig.update_layout(
        
        title_font=dict(size=24),
        
    )
    
    col1.plotly_chart(fig, use_container_width=True)

def motivos_chart(novo_df, escolha, col1):

    df = pd.DataFrame({'Ocorrência':[], 'Contagem':[]})

    for motivo in MOTIVOS:
        if motivo != 'Outros':
            Contagem = novo_df[motivo].sum()
            df = df.append({'Ocorrência': motivo, 'Contagem': Contagem}, ignore_index=True)
    
    

    fig = px.bar(
            df, 
            x=df['Contagem'], 
            y=df['Ocorrência'], 
            text=df['Contagem'],
            template='presentation',
            title='Principais Ocorrências',
            orientation='h'
            
        )

    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.update_layout(height=(500))
    
    fig.for_each_xaxis(lambda x: x.update(showgrid=True))
    
    fig.update_traces(
            marker_color = '#f75e5e', 
            marker_line_color = 'black',
            marker_line_width = 2, 
            opacity = 1
            )

    fig.update_traces(
            textfont_size=21, 
            textposition="inside",
            cliponaxis=False,
            insidetextanchor="middle",
            hovertemplate=None,
            textfont_color='#000000 '
        
        )
    
    fig.update_layout(
        
        title_font=dict(size=24),
        
    )
    
    col1.plotly_chart(fig, use_container_width=True)


class fuzzzz:

    def find_matching_company(name):

        for target in EMPRESAS:
           
            ratio = fuzz.ratio(name.lower(), target.lower()) 
            if ratio > 80:  
                return target
            
        return "NA"
    
    def verificar_ocorrencias(df):
        for categoria in MOTIVOS:
            # Para cada categoria, cria uma nova coluna no dataframe indicando se houve ocorrência
            df[categoria] = df['Motivos'].str.contains(categoria, case=False)
        return df

        
    

st_init()

df = save_df()

empresas = df['Match'].unique()
contagem_nomes = df['Match'].value_counts()

novo_df = pd.DataFrame({'Empresa': contagem_nomes.index, 'Contagem': contagem_nomes.values})
novo_df = motivos(df, novo_df)


chart(novo_df, df)