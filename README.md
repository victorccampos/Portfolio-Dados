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
  <a href="#1-dashboard-pós-graduação-em-física-ufmg">Projeto 1</a> •
  <a href="#2-spotify---dados-pessoais">Projeto 2</a>
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
    src="https://www.fisica.ufmg.br/posgraduacao/wp-content/uploads/sites/2/2017/07/logo-fisica-posgrad.png"
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
- Qual a distribuição de alunos por **área de concentração**?
- Quantos alunos são **bolsistas** e quais **agências** financiam?
- Como está a distribuição por **orientador(a)**?
- Quais tendências aparecem em **entradas/terminações** (quando disponível)?

### Ferramentas e stack
- **Jupyter Notebook (Python)**: [ETL dos Dados](./Dashboard%20Fisica%20UFMG/Notebooks/ETL_posgrad_fisicaufmg.ipynb) e [Análise Exploratória Inicial](./Dashboard%20Fisica%20UFMG/Notebooks/EDA_posgrad_fisicaufmg.ipynb)
- **Power BI**: Dashboard Institucional
- **Git**: versionamento do projeto.

### Entregáveis
Dashboard interativo com a identidade visual do site do programa.  


> **Status**: Em andamento

<hr color="#777777">


<!-- ## 2. Spotify - Dados Pessoais -->
<!-- 
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
      2. Spotify — Análise de Dados Pessoais
    </span>
    <span style="color:#cfcfcf; font-size:14px;">
       <strong>user:@victorjvc</strong>
    </span>
  </div>
  <p style="color:#d7d7d7; margin:10px 0 0;">
    Projeto de exploração de hábitos de escuta a partir dos dados pessoais exportados pelo Spotify.
  </p>
</div>

### Contexto e objetivo
Analisar padrões de consumo musical para responder perguntas como:
- Quais artistas/músicas aparecem com maior frequência?
- Como o hábito muda ao longo do tempo?
- Existe padrão por **dia da semana** ou **horário**?
- Quais períodos concentram mais tempo de escuta?

### Dados
- **Fonte**: exportação oficial de dados do Spotify (histórico de streaming).
- **Conteúdo típico**:
  - timestamp,
  - artista,
  - faixa,
  - duração/tempo de reprodução,
  - metadados adicionais (dependendo do pacote exportado).

### Ferramentas e stack
- **Python**: Pandas (limpeza e agregações)
- **Visualização**: Matplotlib/Plotly (dependendo do notebook)

### Entregáveis (ideias de páginas/saídas)
- Ranking de artistas e faixas
- Séries temporais (escuta por mês/semana)
- Heatmap por dia da semana × hora (se aplicável)
- Métricas de “tempo total de escuta” e “média diária”

<hr color="#777777">
 -->
