# Importação das bibliotecas necessárias
import streamlit as st  # Para criar a interface do Streamlit
import pandas as pd  # Para manipulação dos dados em DataFrame
import plotly.express as px  # Para criação de gráficos interativos com Plotly
import plotly.graph_objs as go  # Para personalizar gráficos mais detalhadamente

# Dicionário que mapeia as colunas originais do CSV para nomes mais amigáveis para representação em dashboard
headers = {
    'data':'Data', 
    'ultimo':'Fechamento', 
    'abertura':'Abertura', 
    'maxima':'Máxima', 
    'minima':'Miníma', 
    'variacao':'Variação Percetual', 
    'acao':'Ação', 
    'mes':'Mês', 
    "ano":"Ano"
}

# Configuração inicial da página do Streamlit
st.set_page_config(page_title='Análise dos principais ativos brasileiros', layout='wide')

# Leitura do arquivo CSV com os dados financeiros. O separador é ";" e a codificação é 'latin1'
data = pd.read_csv('DadosInvesting.csv', sep=';')

# Criação do DataFrame a partir dos dados lidos
df = pd.DataFrame(data)

# Renomeia as colunas do DataFrame de acordo com o dicionário 'headers'
df.rename(columns=headers, inplace=True)

# Criação de uma nova coluna 'Variação monetária' calculando a diferença entre 'Fechamento' e 'Abertura' e em seguida arredondando o resultado com 2 casas decimais
df['Variação monetária'] = round(df['Fechamento'] - df['Abertura'], 2)

# Converte a coluna 'Ano' para string, garantindo que a visualização no Streamlit funcionem corretamente (Caso contrário, a visualização do ano ficaria "2,025" e não "2025")
df['Ano'] = df['Ano'].astype(str)

# Seleção de ano através de um filtro no sidebar do Streamlit
yearSelect = st.sidebar.multiselect('Ano:', df['Ano'].unique(), placeholder='Selecione o ano na lista')

# Filtragem de meses disponíveis com base nos anos selecionados
monthsAvailable = df[df['Ano'].isin(yearSelect)]['Mês'].unique()

# Seleção de mês através de um filtro no sidebar do Streamlit
monthSelect = st.sidebar.multiselect('Mês:', monthsAvailable, placeholder='Selecione o mês na lista')

# Seleção de ações através de um filtro no sidebar do Streamlit
actionSelect = st.sidebar.multiselect('Ação:', df['Ação'].unique(), placeholder='Selecione uma ação na lista')

# Cria uma cópia do DataFrame original para aplicar os filtros
filteredDf = df.copy()

# Aplica o filtro de ano, se algum ano for selecionado
if yearSelect:
    filteredDf = filteredDf[filteredDf['Ano'].isin(yearSelect)]

# Aplica o filtro de mês, se algum mês for selecionado
if monthSelect:
    filteredDf = filteredDf[filteredDf['Mês'].isin(monthSelect)]
    
# Aplica o filtro de ação, se alguma ação for selecionada
if actionSelect:
    filteredDf = filteredDf[filteredDf['Ação'].isin(actionSelect)]

# Se o DataFrame filtrado não estiver vazio, prossegue para gerar os gráficos
if not filteredDf.empty:

    # Exibe o subtítulo na página do Streamlit
    st.subheader('Cotação dos ativos (R$)')
    
    # Cria uma tabela dinâmica (pivot table) para o gráfico de Fechamento, com 'Data' como índice e 'Ação' como coluna
    pivotClosure = filteredDf.pivot(index='Data', columns='Ação', values='Fechamento').reset_index()

    # Cria um gráfico de linha com Plotly para o Fechamento, onde as ações são representadas pelas linhas
    chartClosure = px.line(pivotClosure, x='Data', y=pivotClosure.columns[1:], labels={'value': 'Fechamento', 'variable': 'Ação'})

    # Ajusta o layout do gráfico, formatando o eixo Y para mostrar valores em R$
    chartClosure.update_layout(
        yaxis_tickprefix='R$',  # Prefixo 'R$' no eixo Y
        yaxis_tickformat='.2f'  # Formato de 2 casas decimais no eixo Y
    )

    # Exibe o gráfico de Fechamento na página do Streamlit
    st.plotly_chart(chartClosure, use_container_width=True)

    # Exibe o subtítulo para o gráfico de variação percentual
    st.subheader('Variação (%)')

    # Cria uma tabela dinâmica (pivot table) para o gráfico de Variação percentual, com 'Data' como índice e 'Ação' como coluna
    pivotVarPercen = filteredDf.pivot(index='Data', columns='Ação', values='Variação Percetual').reset_index()

    # Cria um gráfico de linha com Plotly para a Variação percentual
    chart_var_percent = px.line(
        pivotVarPercen,
        x='Data',
        y=pivotVarPercen.columns[1:],  # Exclui a coluna 'Data'
        labels={'value': 'Variação Percetual', 'variable': 'Ação'}  # Define os rótulos dos eixos
    )

    # Exibe o gráfico de Variação percentual na página do Streamlit
    st.plotly_chart(chart_var_percent, use_container_width=True)

    # Exibe o subtítulo para o gráfico de Variação monetária
    st.subheader('Variação (R$)')

    # Cria uma tabela dinâmica (pivot table) para o gráfico de Variação monetária, com 'Data' como índice e 'Ação' como coluna
    pivotVarMonetary = filteredDf.pivot(index='Data', columns='Ação', values='Variação monetária').reset_index()

    # Cria um gráfico de linha com Plotly para a Variação monetária
    chartMonetary = px.line(pivotVarMonetary, x='Data', y=pivotVarMonetary.columns[1:], labels={'value': 'Variação monetária', 'variable': 'Ação'})

    # Ajusta o layout do gráfico de Variação monetária
    chartMonetary.update_layout(
        yaxis_tickprefix='R$',  # Prefixo 'R$' no eixo Y
        yaxis_tickformat='.2f'  # Formato de 2 casas decimais no eixo Y
    )

    # Exibe o gráfico de Variação monetária na página do Streamlit
    st.plotly_chart(chartMonetary, use_container_width=True)

    # Lista de colunas que terão o prefixo 'R$' adicionado antes de seus valores
    columnsConcat = ['Fechamento', 'Abertura', 'Máxima', 'Miníma', 'Variação monetária']

    # Adiciona o prefixo 'R$' em cada valor das colunas selecionadas
    for column in columnsConcat:
        filteredDf[column] = 'R$ ' + filteredDf[column].astype(str)

    # Exibe o DataFrame na mesma largura dos gráficos
    st.dataframe(filteredDf.reset_index(drop=True), use_container_width=True)

