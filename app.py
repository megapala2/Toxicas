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





            ]

SUBS = {"itaú unibanco": "itaú",
        "itau": "itaú",
        "ambev tech": "ambev",
        "stone pagamentos": "stone",
        "serasa experian": "serasa",
        "dti sistemas": "dti digital",
        "xp investimentos": "xp",
        "xp inc.": "xp",
        "ci&t software s/a": "ci&t",
        "carrefour - ms": "carrefour",
        "carrefour icatu brasil": "carrefour",
        "caixa econômica federal (cef)": "caixa federal",
        "cactus gaming corporation": "cactus corporation",
        "brq digital solution": "brq",
        "brave ag": "brave",
        "bees da ab inbev": "ambev",
        "bees brasil": "ambev",
        "bees bank ambev": "ambev",
        "bees bank - ambev": "ambev",
        "bees": "ambev",
        "ambevtech": "ambev",
        "ambev/bees": "ambev",
        "ambev e ambectech": "ambev",
        "ambev (bees bank)": "ambev",
        "99 tecnologia": "99jobs",
        "accenture (projeto oi)": "accenture",
        "acuda - associação cultural e de desenvolvimento do apenado e egresso": "acuda",
        "afya educacional": "afya",
        "agência 4pix": "agência 4p",
        "zurich seguros": "zurich",
        "zup innovation": "zup",
        "xp inc": "xp",
        "wiz co.": "wiz",
        "wyse system ltda": "wise system",
        "wipro do brasil": "wipro",
        "wb produções artísticas e culturais": "wb produções",
        "vortx dtvm": "vortx",
        "vivo telefônica": "vivo",
        "vivo (telefônica brasil)": "vivo",
        "avanade/accenture": "accenture",
        "wise system ltda": "wise system",
        "bees (ambev)": "ambev",
        "stone co": "stone",
        "pagar.me - stone co": "stone",
        "stone instituição de pagamentos sa": "stone",
        "proxxi tecnologia (ibm)": "ibm",
        "proxxi": "ibm",
        "stefanini brasil": "stefanini",
        "stefanini consultoria": "stefanini",
        "stefanini it": "stefanini",
        "banco itaú": "itaú",
        "itaú, modec do brasil, agência havas+, softdesign, copa studio": "itaú",
        "ish - tecnologia": "ish",
        "isaac (arco tech)": "isaac",
        "ifood /anota aí": "ifood",
        "santander / f1rst": "santander",
        "banco santander": "santander",
        "f1rst tecnologia (santander)": "santander",
        "first - grupo santander": "santander",
        "f1rst tecnologia - banco santander": "santander",
        "f1rst santander": "santander",
        "f1rst empresa do santander": "santander",
        "f1rst - santander": "santander",
        "autoglass e btg pactual": "btg pactual",
        "btg": "btg pactual",
        "vivo (telefonica brasil)": "vivo",

}

MOTIVOS = ["Racismo", "Machismo", "Burnout", "Assédio", "Tóxico", "Salário", "Liderença", 'Homofobia','Hostil', 'Sexismo', 'Xenofobia', 'Preconceito', 'Transfobia', 'Gestão']

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

def st_init():

    st.set_page_config(layout='wide', page_title='Worst to Work', page_icon="📊")

    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

    st.title("EMPRESAS TÓXICAS BRASIL")
   
    st.sidebar.image('https://worstplacetowork.com.br/wp-content/uploads/2024/03/worstplacetoworklogo.png')
    fonte = st.sidebar.info("Planilha fonte: https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/htmlview")
    form = st.sidebar.info('Formulário para preencher: https://docs.google.com/forms/d/e/1FAIpQLSdsmCP5YB4zgtfhR5xLFeqoCMDBVVcNLe2KIzAdJelwPs5-1A/viewform')
   
@st.cache_data
def save_df():

    try:
   
        df = pd.read_csv('https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/export?format=csv')
        

    except:
        with st.spinner('Erro ao carregar a planilha do Google Sheets, pegando arquivo backup!'):
            time.sleep(5)
            try:
            
                 df = save_df_two()
                 return df
            except:
                 st.warning("Erro ao carregar TUDO X.X")
        


    df = df.rename(columns={df.columns[0]: 'Data', df.columns[1]: 'Empresa'})
    
    df = df.drop_duplicates(subset=['Empresa', 'Motivos'])

    df['Empresa'] =  df['Empresa'].astype(str)
    df['Motivos'] = df['Motivos'].astype(str)
    df['Empresa'] = df['Empresa'].str.lower().str.strip()
    df['Motivos'] = df['Motivos'].str.lower().str.strip()

    df['Contagem'] = df['Empresa'].map(df['Empresa'].value_counts())
    df['Match'] = df['Empresa'].apply(fuzzzz.find_matching_company)
    
    df = df.drop(df[df['Match'] == 'NA'].index)
    df = fuzzzz.verificar_ocorrencias(df)

  
    return df


@st.cache_data
def save_df_two():

    st.sidebar.warning('A planilha está interditada! Logo estaremos usando um arquivo de backup de 29/03/2024!')
    df = df = pd.read_csv('assets/DADOS.csv')
        
    df = df.rename(columns={df.columns[0]: 'Data', df.columns[1]: 'Empresa'})
    df = df.drop_duplicates(subset=['Empresa', 'Motivos'])

    df['Empresa'] =  df['Empresa'].astype(str)
    df['Motivos'] = df['Motivos'].astype(str)
    df['Empresa'] = df['Empresa'].str.lower().str.strip()
    df['Motivos'] = df['Motivos'].str.lower().str.strip()

    
   
    df['Contagem'] = df['Empresa'].map(df['Empresa'].value_counts())
    df['Match'] = df['Empresa'].apply(fuzzzz.find_matching_company)
    
    
    df = df.drop(df[df['Match'] == 'NA'].index)
    df = fuzzzz.verificar_ocorrencias(df)


    return df

def motivos(df, novo_df):
    
    novo_df = novo_df.rename(columns={'Empresa': 'Match'})
    
    for motivo in MOTIVOS:

        contagem_motivo = df.groupby('Match')[motivo].sum().reset_index()
        novo_df = novo_df.merge(contagem_motivo, on='Match', how='left')
    
    return novo_df

def chart(novo_df, escolha, df):

    df['Empresa'] = df['Data']
    df['Data'] = df['Match']
    df = df.drop(columns='Match')
    df = df.rename(columns={'Data':'Match', 'Empresa':'Data'})
    df = df.drop(columns='Data')
    df = df.reset_index()


    with st.expander("Dataframe"):
        st.info(f"Linhas: {len(novo_df)}")
        st.dataframe(novo_df, use_container_width=True)
        
        st.info(f"Linhas: {len(df)}")
        st.dataframe(df, use_container_width=True)

    if escolha:

        df_filtro = novo_df.groupby('Match')[escolha].sum().reset_index(name=escolha)
        top15 = df_filtro.nlargest(20, escolha)
        novo_df = novo_df[novo_df['Match'].isin(top15['Match'])]


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
        
        container = st.container()

        container.plotly_chart(fig, use_container_width=True)

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

opcoes = ['Contagem'] + MOTIVOS 
escolha = st.selectbox('Selecione o que você quer comparar!:', options=opcoes)


chart(novo_df, escolha, df)