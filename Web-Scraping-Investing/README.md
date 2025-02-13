###  Web Scraping de Cotações das Ações Brasileiras  

Este código realiza **web scraping** para obter os valores de cotação das **cinco principais ações brasileiras** listadas no site **Investing**
### 🌐 Link para visualização no Streamlit: https://screping-ivesting-with-python.streamlit.app/

### 📌 Fluxo do Código
> [!TIP]
> ### Processo de Coleta e Exibição de Dados
> 1. **Automação do Navegador** → Utiliza a biblioteca **Selenium** para acessar o site e navegar até as páginas das ações.  
> 2. **Extração de Dados** → Captura tabelas de cotações usando **BeautifulSoup**.  
> 3. **Tratamento dos Dados** → Usa **Pandas** para limpar e formatar os dados, convertendo datas e valores numéricos.  
> 4. **Armazenamento** → Salva os dados em um arquivo **CSV**.  
> 5. **Dashboard** → Os dados serão exibidos posteriormente em um dashboard usando **Streamlit**.

> [!IMPORTANT]
> ### Desvantagens do web scraping
> 1. **Restrições Legais** – Muitos sites possuem termos de uso que proíbem a extração automatizada de dados, podendo levar a bloqueios de IP ou até ações legais.
> 2. **Mudanças na Estrutura do Site** – Pequenas alterações no HTML podem quebrar o scraper, exigindo manutenção constante.
> 3. **Desempenho e Carga no Servidor** – Scrapers mal projetados podem gerar altas requisições, causando lentidão ou bloqueio pelo site alvo.
> 4. **Qualidade e Confiabilidade dos Dados** – Os dados extraídos podem estar incompletos, desatualizados ou inconsistentes, comprometendo as análises.
> 5. **Dificuldade com Conteúdo Dinâmico** – Sites que usam JavaScript pesado (como React ou Vue.js) podem exigir selenium ou APIs, tornando o processo mais complexo e lento.

> [!NOTE]
> ### O arquivo 'DadosInvesting.csv' foi extraído no dia 13/02/2025, por tanto, as tabelas de ações contém apenas os dados dos fechamentos posteriores ao dia 01/01/2020 e anteriores ao dia 13/02/2025
