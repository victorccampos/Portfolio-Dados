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
      <h1>2. Spotify — Análise de Dados Pessoais</h1>
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
  - **Plotly** + **Streamlit** em  **[📁/dashboard.py](./dashboard.py)**
  - **Matplotlib** em **[📁Notebooks/EDA-spotify.ipynb](./Notebooks/EDA-spotify.ipynb)**


### Dashboard Streamlit

![](./video/spotify-streamlit-shocase.gif)

<hr color="#45d979">


### Conclusões
#### Q1 : Qual top10 artistas?

![](./images/Q1.png)



#### Q2 : Qual o tempo mensal ouvindo música?
![](./images/Q2.png)

#### Q3: Qual dia da semana mais foi escutado música?
![](./images/Q3.png)

#### Q4: Qual período do dia concentra mais tempo de escuta?
![](./images/Q4.png)

<hr color="#45d979">
