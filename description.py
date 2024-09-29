import streamlit as st
from PIL import Image

# Configurações iniciais
st.set_page_config(page_title="CS03 - Dashboard", page_icon=":bar_chart:", layout="wide")

# Função para mostrar o Propósito
def cabecalho():
    # Título principal
    st.markdown('<h1 style="text-align: center;">GOVERNANÇA EM IA E BUSINESS ANALYTICS - CHALLENGE SPRINT 03</h1>', unsafe_allow_html=True)
    
    # Subtítulo
    st.markdown('<h5 style="text-align: center; font-style: italic;">SHOPPING DO CIDADÃO - DASHBOARD DE ATTRITION</h5><br>', unsafe_allow_html=True)

    # Motivação
    st.markdown("""
    <div style="font-size: 12px; text-align: right; max-width: 490px; margin-left: auto; display: block;">
        Projeto desenvolvido para Challenge Sprint 03, disciplina de Governança em IA e Business Analytics do tecnólogo de Inteligência Artificial da FIAP. Com suporte do Orientador Leonardo Ruiz Orabona.<br><br>
    </div>
    """, unsafe_allow_html=True)

    # Carregar e exibir a imagem
    imagem = "images/Team.png"
    try:
        img = Image.open(imagem)
        st.image(img, caption="", use_column_width=True)
    except FileNotFoundError:
        st.error("Imagem não encontrada. Verifique o caminho para a imagem.")

# Chame a função para mostrar o Propósito
cabecalho()

# Seções do conteúdo
st.header("Introdução")

st.markdown("""
A empresa Shopping do Cidadão é uma GovTech especializada na prestação de serviços públicos aos cidadãos por meio de múltiplos canais, como plataformas digitais e centros de atendimento presenciais disponíveis em várias regiões do Brasil, incluindo São Paulo, Minas Gerais, Rio de Janeiro e Ceará. A missão da empresa é desburocratizar processos e aproximar o Estado dos cidadãos, proporcionando agilidade, qualidade e facilidade no acesso a serviços públicos oferecendo serviços como emissão de documentos, certidões, e cursos profissionalizantes.

Assim como as demais empresas do mercado, o departamento de Recursos Humanos do Shopping do Cidadão enfrenta diversos desafios no seu dia a dia, principalmente relacionados ao desenvolvimento de talentos e à retenção de funcionários, este que é um desafio crítico para qualquer organização, especialmente em setores dinâmicos como a prestação de serviços públicos.

Manter funcionários satisfeitos e engajados exige uma abordagem multifacetada que abrange o bem-estar, reconhecimento, desenvolvimento de carreira e engajamento contínuo. Para isso, a aplicação de Inteligência Artificial pode ser um diferencial significativo ao identificar padrões nos dados de funcionários e prever comportamentos que são difíceis de detectar manualmente.

Um exemplo claro é o uso do indicador de Attrition (taxa de evasão de funcionários), que pode ser analisado com maior precisão por meio de algoritmos de Machine Learning para prever quais funcionários têm maior probabilidade de se desligarem voluntariamente da empresa, permitindo que o RH tome ações preventivas específicas para reter esses talentos.

""")

st.header("Dashboard")

st.markdown("""
Para o projeto, foi utilizada a base de dados IBM HR Analytics Employee Attrition & Performance, disponível no Kaggle. Esta base contém informações detalhadas sobre funcionários, incluindo idade, nível de educação, satisfação com o trabalho, rendimento, cargo, tempo de trabalho na empresa, entre outras variáveis.

A análise desses dados é crucial para entender fatores que influenciam a rotatividade de funcionários, identificar padrões de desempenho e melhorar a gestão de recursos humanos. Utilizar um dashboard para essa análise permite visualizar tendências, fazer comparações entre diferentes grupos e tomar decisões baseadas em dados de forma rápida e eficiente.
""")

# URL do relatório do Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZTE2MThkMTctY2FiYi00NTRkLWFhMDItMDkxMDNlZjU4MzE3IiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"

# Centralizando o iframe do Power BI
st.markdown(
    f"<div style='display: flex; justify-content: center;'><iframe src='{power_bi_url}' width='2000' height='1000' frameborder='0' allowFullScreen='true'></iframe></div>",
    unsafe_allow_html=True
)

st.write("") 

st.markdown("""

O dashboard apresentado acima oferece uma análise interativa dos dados, permitindo que os usuários explorem informações de forma dinâmica e visual. Com a complexidade dos desafios diários enfrentados pelo departamento de RH da empresa, especialmente relacionados a retenção de talentos, a necessidade de uma compreensão clara e acessível dos dados se torna crucial.

Através deste dashboard, é possível identificar tendências, padrões e anomalias nos dados, o que proporciona insights valiosos para a tomada de decisões informadas. Os gráficos e visualizações permitem uma interpretação mais intuitiva, facilitando a análise por diferentes segmentos e variáveis.

""")