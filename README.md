# Portfólio em Dados 🎲💻


<p align="left">
    <a href="https://www.linkedin.com/in/joaovictorcamposcosta" target="_blank">
        <img
            src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg"
            alt="LinkedIn"
            width="22"
            style="vertical-align:middle;"
        />
        <span style="vertical-align:middle; margin-left:6px;"><strong>João Victor Campos</strong></span>
    </a>
    <br>
    <span>Mestrando em Física | Transição para Dados/BI</span>
</p>

**Python • Pandas • Power BI**

<p align="center">
  <a href="#1-dashboard-pós-graduação-em-física-ufmg">Dashboard Pós-Graduação em Física</a> •
  <a href="#2-spotify---dados-pessoais">Spotify Wrapped "Home Made"</a>
</p>


<blockquote>
Este repositório reúne projetos do meu portfólio em <b>Análise de Dados</b> e <b>BI</b>, com foco em:  

- **pipeline reprodutível** (extração → limpeza → análise → entrega)  
- **perguntas claras** e respostas com métricas/visuais  
- organização e documentação para facilitar leitura e execução. 

</blockquote>

<hr color="#777777">

## 1. Dashboard Pós-Graduação em Física (UFMG)

<p align="center">
  <img
    src="https://www.fisica.ufmg.br/posgraduacao/wp-content/uploads/sites/2/2017/07/logo-fisica-posgrad.png#gh-light-mode-only"
    alt="Pós-Graduação em Física - UFMG"
    width="420"
  >
  <img
    src="https://workshopfisica.info/wp-content/uploads/2024/01/POS-GRADUACAO-DEPARTAMENTO-DE-FISICA-4.png#gh-dark-mode-only"
    alt="Pós-Graduação em Física - UFMG"
    width="420"
  >
</p>


### Contexto e objetivo
A transparência na composição do corpo discente é fundamental para um bom funcionamento de um
programa de Pós-Graduação. Nesse sentido, esta análise tem como objetivo responder às principais
dúvidas de alunos interessados em ingressar no Departamento de Física, bem como fornecer aos
docentes e discentes atuais uma visão mais clara do ambiente acadêmico em que estão inseridos.

A partir de dados públicos do programa, o projeto busca organizar e apresentar informações de forma
acessível, apoiando a compreensão do perfil discente e auxiliando a tomada de decisão institucional.
As principais perguntas abordadas são:

- Quantos alunos há por **modalidade** (Mestrado/Doutorado)?
  - **Resposta**: Dos 152 alunos matriculados, 83 são do Doutorado e 69 de Mestrado.

- Qual a distribuição de alunos por **área de concentração**?
  - A **Física** e a maior área de concentração com 118 alunos, seguida da Física Aplicada e Interdisciplinar com 19 alunos e Astrofísica com 15 alunos.  

- Quantos alunos são **bolsistas** e quais **agências** financiam?
  - Dos 152 alunos, 108 (71,05%) são bolsistas e 44 alunos (28.95%) estão sem bolsas de estudos. As agências financiadoras do programa são CAPES, CNPQ e FAPEMIG. Existem apenas 12 bolsas FAPEMIG em todo o programa e a maioria das bolsas CNPQ são advindas da PRPG.

- Como está a distribuição de orientandos por **orientador(a)**?
  - Os orientadores com mais alunos do programa são os professores Bruce Vega e Mário Sérgio Mazzoni com **7 alunos cada um**. Em segundo lugar o prof. Ângelo Malachias com **6 alunos** e os 4 últimos professores que compõe o top 7 possuem **5 alunos cada**.
  - 🚨 É válido lembrar que esses dados dizem respeito apenas ao programa de Pós-Graduação e, portanto, não é levado em conta orientação em *iniciação científica* da *Graduação em Física*.

- Quais tendências aparecem em **entradas/terminações**?
  - Há uma crescente evidente no número de alunos do programa, em especial no ano de 2025 com 50 alunos!

### Ferramentas e stack
- **Jupyter Notebook (Python)**: [ETL dos Dados](./Dashboard%20Fisica%20UFMG/Notebooks/ETL_posgrad_fisicaufmg.ipynb) e [Análise Exploratória Inicial](./Dashboard%20Fisica%20UFMG/Notebooks/EDA_posgrad_fisicaufmg.ipynb)
- **Power BI**: Dashboard Institucional.: [Confira o Dashboard no Link](https://app.powerbi.com/reportEmbed?reportId=280e166c-af3a-4da4-881a-7f6a93304ed3&autoAuth=true&ctid=64126139-4352-4cd7-b1fb-2a971c6f69a6)
- **Git**: versionamento do projeto.

### Entregável
Dashboard interativo com a identidade visual do [site do programa](https://www.fisica.ufmg.br/posgraduacao/corpo-discente/).  

<div align="center">

![Dashboard Showcase](./Dashboard%20Fisica%20UFMG/PBI/dashboard_showcase.gif)

</div>
<hr color="#777777">


<!-- ## 2. Spotify - Dados Pessoais -->


<div style="background-color:#0b0b0b; border:1px solid #1f1f1f; border-radius:10px; padding:14px 16px; margin:10px 0;">
  <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
    <img
      src="https://open.spotify.com/favicon.ico"
      alt="Spotify"
      width="24"
      height="24"
      style="border-radius:4px;"
    >
    <span style="color:#45d979; font-weight:700; font-size:18px;">
      <h2>2. Spotify — Análise de Dados Pessoais</h2>
    </span>
    <span style="color:#cfcfcf; font-size:14px;">
       <strong>user:@victorjvc</strong>
    </span>
  </div>
  <p style="color:#d7d7d7; margin:10px 0 0;">
    Um Spotify Wrapped <i>"Home made"</i> para aqueles que não se contentam com suas retrospectivas ao final do ano.
  </p>
</div>

### Perguntas a serem respondidas

- [Qual top10 artistas?](#conclusões)
- [Qual o tempo mensal ouvindo música?](#conclusões)
- [Qual dia da semana mais foi escutado música?](#conclusões)
- [Qual período do dia concentra mais tempo de escuta?](#conclusões)

### Dados
- **Fonte**: exportação oficial de dados do Spotify (histórico de streaming).
  

### Stack
- **Python**: Pandas (limpeza e agregações)
- **Visualização**:
  - **Plotly** + **Streamlit** em  **[📁Projeto-Spotify/dashboard.py](Projeto-Spotify/dashboard.py)**
  - **Matplotlib** em **[📁📁Projeto-Spotify/Notebooks/EDA-spotify.ipynb](Projeto-Spotify/Notebooks/EDA-spotify.ipynb)**


### Dashboard Streamlit
![](Projeto-Spotify/video/spotify-streamlit-shocase.gif)


<hr color="#45d979">


### Respostas
Visualizações estáticas com Matplotlib.
#### Q1 : Qual top10 artistas?

![](Projeto-Spotify/images/Q1.png)


#### Q2 : Qual o tempo mensal ouvindo música?
O **tempo médio mensal** foi de ***47 horas***!
![](Projeto-Spotify/images/Q2.png)

#### Q3: Qual dia da semana mais foi escutado música?
Quinta-Feira é o dia que mais escutou-se músicas no ano de 2025.
![](Projeto-Spotify/images/Q3.png)

#### Q4: Qual período do dia concentra mais tempo de escuta?
Não houve preferência entre tarde e noite, ambas com 45% da vezes!

![](Projeto-Spotify/images/Q4.png)


<hr color="#45d979">


