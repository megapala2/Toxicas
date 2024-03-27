import streamlit as st
import pandas as pd
import plotly.express as px
#from collections import Counter
#from nltk.tokenize import word_tokenize
#import nltk


#nltk.download('punkt')

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

MOTIVOS = ["racismo", "machismo", "burnout", "abuso", "ruim", "péssimo", "tóxica", "salário", "competitivo", "liderença", "rotatividade", 'homofóbica']

@st.cache_data
def save_df():
    df = pd.read_csv('https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/export?format=csv')
    return df
    

st.set_page_config(layout='wide')

df = save_df()


df = df.rename(columns={df.columns[0]: 'Data', df.columns[1]: 'Empresa'})

df['Empresa'] = df['Empresa'].str.lower().str.strip()
df['Motivos'] = df['Motivos'].str.lower().str.strip()
df['Empresa'] = df['Empresa'].replace(SUBS)
df['Contagem'] = df['Empresa'].map(df['Empresa'].value_counts())


empresas = df['Empresa'].unique()
contagem_nomes = df['Empresa'].value_counts()

novo_df = pd.DataFrame({'Empresa': contagem_nomes.index, 'Contagem': contagem_nomes.values})

for motivo in MOTIVOS:
    contagem_racismo = df.groupby('Empresa')['Motivos'].apply(lambda x: x.str.contains(motivo).sum()).reset_index()
    contagem_racismo = contagem_racismo.rename(columns={'Motivos': motivo})
    novo_df = novo_df.merge(contagem_racismo, on='Empresa', how='left')

opcoes = ['Contagem'] + MOTIVOS 

st.info("Planilha fonte: https://docs.google.com/spreadsheets/u/0/d/1u1_8ND_BY1DaGaQdu0ZRZPebrOaTJekE9hyw_7BAlzw/htmlview")
st.info('Formulário para preencher: https://docs.google.com/forms/d/e/1FAIpQLSdsmCP5YB4zgtfhR5xLFeqoCMDBVVcNLe2KIzAdJelwPs5-1A/viewform')


escolha = st.selectbox('Selecione o que você quer comparar!:', options=opcoes)



## PEGA AS PALAVRAS QUE MAIS APARECEM NA COLUNA MOTIVOS
#df = df.dropna(subset=['Motivos'])
#df['Motivos'] = df['Motivos'].astype(str)
#word_list = [word for line in df['Motivos'] for word in word_tokenize(line)]
#word_counts = Counter(word_list)
#most_common_words = [(word, count) for word, count in word_counts.items() if len(word) > 5]



with st.expander("Dataframe"):
    st.info(f"Linhas: {len(empresas)}")
    st.dataframe(novo_df, use_container_width=True)

if escolha:

    df_filtro = novo_df.groupby('Empresa')[escolha].sum().reset_index(name=escolha)
    top15 = df_filtro.nlargest(20, escolha)
    novo_df = novo_df[novo_df['Empresa'].isin(top15['Empresa'])]


    fig = px.bar(
            novo_df, 
            x=novo_df[escolha], 
            y=novo_df['Empresa'], 
            text=novo_df['Empresa'],
            template='presentation',
            
        )

    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    fig.update_layout(height=(800))

    fig.update_traces(
            textfont_size=19, 
            textposition="inside", 
            cliponaxis=False,
            insidetextanchor="middle",
            hovertemplate=None,
        

        )

    st.plotly_chart(fig, use_container_width=True)