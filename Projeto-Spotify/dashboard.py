import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns   

def seaborn_to_plotly(sns_pallete) -> list[str]:
    """Transforma as paletas do seaborn pro RGB do plotly"""    
    plotly_pal = []
    for c in sns_pallete:
        R = int(c[0]*255)
        G = int(c[1]*255)
        B = int(c[2]*255)
        color_plotly = f"rgb({R}, {G}, {B})"
        plotly_pal.append(color_plotly)
    return plotly_pal

st.set_page_config(page_title="Spotify Dashboard", layout="wide")

SPOTIFY_GREEN = "rgb(30, 215, 96)"
LIGHT_GREEN = "rgb(234, 246, 229)"

src_image: str = "https://open.spotify.com/favicon.ico"
st.image(src_image, width=50)
st.write("# Spotify Wrapped 2025")
st.write("## **@victorjvc**")
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)



df = pd.read_csv("./spotify_data/spotify2025.csv")

# ---
#  Gráfico: Qual meu Top 10 artistas ?
greens10 = seaborn_to_plotly(sns_pallete=sns.color_palette("Greens", n_colors=10))
top10_artists = (
    df["artist_name"]
    .value_counts()
    .head(10)
    .sort_values()
    .reset_index()
)
top10_artists.columns = ["Nome Artista", "Contagem"]
graph1 = px.bar(top10_artists, x="Contagem", y="Nome Artista", orientation="h", color="Contagem",
    color_continuous_scale=greens10, title="Top 10 Artistas", hover_data={"Nome Artista": False})

graph1.update_xaxes(title_text="")
graph1.update_yaxes(title_text="")
graph1.update_traces(hovertemplate="Contagem = %{x}")

col1.plotly_chart(graph1, use_container_width=True)


# ---
# Gráfico: Quanto tempo de música eu escutei mensalmente?
df["minPlayed"] = (df["ms_played"] / 1_000 / 60).round(2)
meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
meses_map = {i+1:mes for i, mes in enumerate(meses)}
monthly_minutes = df[["minPlayed", "month"]].groupby("month").sum().reset_index()
monthly_minutes["month_str"] = monthly_minutes["month"].map(meses_map)
monthly_minutes["hours"] = (monthly_minutes["minPlayed"] / 60).round(2)

graph2 = px.line(
    monthly_minutes,
    x="month_str",
    y="minPlayed",
    markers=True,
    title="Minutos ouvidos por mês",
    color_discrete_sequence=[SPOTIFY_GREEN],
    hover_data=dict(minPlayed=False, hours=".1f", month_str=True)
)
graph2.update_yaxes(title_text="")
graph2.update_xaxes(title_text="")
graph2.update_traces(
    hovertemplate=(
        "<b>Mês:</b> %{x}<br>"
        "<b>Tempo:</b> %{customdata[0]:.1f} h<br>"
        "<extra></extra>"
    )
)

col2.plotly_chart(graph2, use_container_width=True)


# ---
# Gráfico: Em que dias da semana eu mais escuto música?
weekday_df = df["weekday"].value_counts().sort_index().reset_index()
weekday_df.columns = ["Dia da Semana", "Contagem"]

#  int -> str ; 0=segunda ... 6=domingo
weekday_map = {0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo"}
weekday_df["Dia da Semana"] = weekday_df["Dia da Semana"].map(weekday_map)

graph3 = px.bar(weekday_df, x="Dia da Semana", y="Contagem", title="Dia da Semana Preferido para ouvir música")

colors = [
    SPOTIFY_GREEN if (v == weekday_df["Contagem"].max()) else LIGHT_GREEN for v in weekday_df["Contagem"]
]
graph3.update_yaxes(title_text="Músicas Ouvidas", titlefont=dict(size=18))
graph3.update_xaxes(title_text="", titlefont=dict(size=18))
graph3.update_traces(marker_color=colors, marker_line_width=0)
col3.plotly_chart(graph3)


# ---
# Gráfico 4: Existe preferência de horário para ouvir música?
df["ts"] = pd.to_datetime(df["ts"])
df["hour"] = df["ts"].dt.hour # 0, ..., 24
turnos = ["manhã", "tarde", "noite"]
criterios = [
     df.hour < 12, 
    (df.hour >= 12) & (df.hour < 18),
    df.hour >= 18
]
df["turno"] = np.select(condlist=criterios, choicelist=turnos)
pct_turnos = df["turno"].value_counts(normalize=True).reset_index()
pct_turnos.columns = ["Turno", "Porcentagem"]   
greens_r3 = seaborn_to_plotly(sns.color_palette("Greens_r", n_colors=3))
graph4 = px.pie(pct_turnos, names="Turno", values="Porcentagem", title="Preferência por turno", color_discrete_sequence=greens_r3)

graph4.update_traces(hovertemplate="%{percent:.1%}<extra></extra>")
graph4.update_traces(textinfo="label+percent",textfont=dict(size=16),showlegend=False)
col4.plotly_chart(graph4)
  