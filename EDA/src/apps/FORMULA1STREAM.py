import streamlit as st
import pandas as pd
#from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objs as go
from pathlib import Path
import pandas as pd
pd.set_option("display.max_rows", 500)
df_1 = pd.DataFrame()
fuente_1 = ""


BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR.parent / 'data' / 'data'

df_races = pd.read_csv(DATA_DIR / 'races.csv')
df_results = pd.read_csv(DATA_DIR / 'results.csv')
df_drivers = pd.read_csv(DATA_DIR / 'drivers.csv')
df_constructors = pd.read_csv(DATA_DIR / 'constructors.csv')



df_rrc = df_results.merge(df_races, on='raceId', how='left') \
                      .merge(df_constructors, on='constructorId', how='left')
df_rrc = df_rrc[[ 'raceId', 'number', 'grid',
       'position', 'positionText', 'positionOrder', 'points', 'year', 'round', 'circuitId', 'name_x',
       'date', 'time_y','constructorRef', 'name_y', 'nationality']]



df_15_24 = df_rrc[df_rrc.year >= 2015]

df_y_n = df_15_24.groupby(['year', 'name_y'])
df_points_per_year = df_y_n[['points']].sum()
df_points_per_year = df_points_per_year.reset_index()


df_rrd = df_results.merge(df_races, on='raceId', how='left') \
                      .merge(df_drivers, on='driverId', how='left')
df_rrd = df_rrd[[ 'grid','positionOrder', 'points', 'rank', 
       'year', 'round', 'name',
       'forename', 'surname', 'nationality']]

df_year = df_rrd[df_rrd['year'] >= 2015].copy()
df_max_ham_per_race = df_year[(df_year['forename'] == 'Max') | (df_year['forename'] == 'Lewis')].copy()



df_max_ham_per_race = df_max_ham_per_race.assign(wins=df_max_ham_per_race['positionOrder'] == 1)



df_max_ham_total = df_max_ham_per_race.groupby(['year', 'forename', 'surname']).agg({
    'points': 'sum',
    'wins': 'sum'
}).reset_index()


df_rrd['wins'] = df_rrd['positionOrder'] == 1
df_rrd['wins'].sum()

df_max = df_rrd[((df_rrd['forename']== 'Max') & ((df_rrd['year'] >= 2015) & (df_rrd['year'] < 2020 )))]

vers = df_max.groupby(['year', 'forename', 'surname']).agg({
    'points': 'sum',
    'wins': 'sum'
}).reset_index() 

df_ham = df_rrd[((df_rrd['forename']== 'Lewis') & ((df_rrd['year'] >= 2007) & (df_rrd['year'] < 2012 )))]

ham = df_ham.groupby(['year', 'forename', 'surname']).agg({
    'points': 'sum',
    'wins': 'sum'
}).reset_index() 


traces = []
unico = df_points_per_year['name_y'].unique()

cores = {
    'Mercedes': '#00D2BE',     
    'Red Bull': '#1E41FF',     
    'Ferrari': '#DC0000',      
    'McLaren': '#FF8700',      
    'Alpine F1 Team': '#0090FF', 'Renault': '#0090FF', 
    'Williams': '#005AFF',     
    'Aston Martin': '#006F62', 'Racing Point': '#006F62', 'Force India': '#006F62',
    'AlphaTauri': '#6699FF',  'RB F1 Team': '#6699FF', 'Toro Rosso': '#6699FF',
    'Haas F1 Team': '#B6BABD',        
    'Sauber': '#900000', 'Alfa Romeo': '#900000', 
    'Lotus F1': '#454545',   
    'Manor Marussia': '#454545',  
}

for team in unico:
    i = df_points_per_year[df_points_per_year['name_y'] == team]
    trace = go.Scatter(
                x = i['year'],
                y = i['points'],
                name = team,
              
                line = dict(color = cores.get(team, 'gray')),
                
    )
    traces.append(trace)


layout = dict(title = 'Constructors points per year',
             xaxis= dict(title= 'Year',ticklen= 5)
           )

fig = go.Figure(data = traces, layout=layout)
fig.update_layout(
    height=800,  
    title='Constructors points per year',
    xaxis=dict(title='Year', ticklen=5),
    yaxis=dict(title='Points')
)

fig.update_yaxes(rangemode="tozero")
st.plotly_chart(fig)



df_verstappen = df_max_ham_total[df_max_ham_total['forename'] == 'Max']
df_hamilton = df_max_ham_total[df_max_ham_total['forename'] == 'Lewis']

trace1 = go.Bar(x = df_verstappen['year'],
               y = df_verstappen['points'],
               name = 'MAX',
               marker = dict(color = '#1E41FF',
                            line = dict(color='rgb(0,0,0)', width = 1.5)),
               text = df_verstappen['wins'])

trace2 = go.Bar(x = df_hamilton['year'],
               y = df_hamilton['points'],
               name = 'LEWIS',
               marker = dict(color = '#00D2BE',
                            line = dict(color='rgb(0,0,0)', width = 1.5)),
               text = df_hamilton['wins'])


data = [trace1, trace2]

layout = go.Layout(barmode = "group")

fig = go.Figure(data = data, layout = layout)
fig.update_layout(
    height=800,  
    title='Max vs Lewis (2015 - 2024)',
    xaxis=dict(title='Year', ticklen=5),
    yaxis=dict(title='Points')
)

st.plotly_chart(fig)


trace_ham = go.Bar(
    x = ham['year'],
    y = ham['points'],
    text= ham['wins'],
    name = 'HAM',
    marker = dict(color = '#00D2BE',
                  line = dict(color='rgb(0,0,0)', width = 1.5)),
    xaxis= 'x1',
    yaxis= 'y1'

)
trace_vers = go.Bar(
    x = vers['year'],
    y = vers['points'],
    text= vers['wins'],
    name = 'MAX',
    marker = dict(color = '#1E41FF',
                line = dict(color='rgb(0,0,0)', width = 1.5)),
    xaxis= 'x2',
    yaxis= 'y2'
)



layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45],
        anchor='y1'
    ),
    yaxis=dict(
        domain=[0, 1],
        anchor='x1'
    ),
    xaxis2=dict(
        domain=[0.55, 1],
        anchor='y2'
    ),
     yaxis2=dict(
        domain=[0, 1],
        anchor='x2'
))

data = [trace_ham, trace_vers]

fig = go.Figure(data = data, layout = layout)
fig.update_layout(yaxis2=dict(matches='y1'))
fig.update_layout(
    height=800,  # aumenta a altura total do gráfico
    title='Lewis (2007 - 2011) vs Max (2015 - 2019). Firts 5 seasons.',
    xaxis=dict(title='Year', ticklen=5),
    yaxis=dict(title='Points')
)

st.plotly_chart(fig)




