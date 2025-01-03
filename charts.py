import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from read_data import home, away, cols
from color import color_home, color_away

############################# chart 0 ####################################
home_team_name = home["team_long_name"].unique()[0]
away_team_name = away["team_long_name"].unique()[1]

cols = ['buildUpPlaySpeed', 'buildUpPlayDribbling', 'buildUpPlayPassing', 
        'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 
        'defencePressure', 'defenceAggression', 'defenceTeamWidth']

def fig_scatterone(df, team_name, color):
   
    tn_mk = ( df["team_long_name"] == team_name )
    
    trace0 = go.Scatterpolar(
        r=df[tn_mk][cols].values[0],
        theta=cols,
        mode="lines+text",
        name=f"home: {team_name}",
        connectgaps=True,
        fill="toself",
        line={"width": 0},
        fillcolor = color,
        opacity=0.5,
        # fillcolor="rgba(124,23,123,0.5)"
    )
    
    fig = go.Figure([trace0]).update_layout({
        "polar": {"radialaxis": {"range": [0, 80]}},
    })
    
    return fig

############################# chart 1 ####################################
# home_team_name = home["team_long_name"].unique()[0]
# away_team_name = away["team_long_name"].unique()[1]

cols = ['buildUpPlaySpeed', 'buildUpPlayDribbling', 'buildUpPlayPassing', 
        'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 
        'defencePressure', 'defenceAggression', 'defenceTeamWidth']


def fig_scatterboth(home_team_name, away_team_name):
    mask1 = ( home["team_long_name"] == home_team_name )
    mask2 = ( away["team_long_name"] == away_team_name )
    
    trace0 = go.Scatterpolar(
        r=home[mask1][cols].values[0],
        theta=cols,
        mode="lines",
        name=f"home: {home_team_name}",
        connectgaps=True,
        fill="toself",
        line={"width": 0},
        fillcolor=color_home,
        opacity=0.5
    )
    
    trace1 = go.Scatterpolar(
        r=away[mask2][cols].values[0],
        theta=cols,
        mode="lines",
        name=f"away: {away_team_name}",
        connectgaps=True,
        fill="toself",
        line={"width": 0},
        fillcolor=color_away,
        opacity=0.5
    )
    
    fig = go.Figure([trace0, trace1]).update_layout({
        "title": {"text": f"team stats", "x": 0.5},
        "margin": {"t": 30, "b": 45, "r": 75, "l": 75},
    }).update_layout({
        "polar": {"radialaxis": {"range": [0, 80]}},
    })
    
    return fig 

############################# chart 3 ####################################

import plotly.graph_objs as go

def score_output(df1, df2, value1, value2, title, shlg):

    mask_home = ( df1["team_long_name"]==value1 )
    mask_away = ( df2["team_long_name"]==value2 )
    x =["A"]

    y1 = df1[mask_home]["home_team_goal"].values
    y2 = df2[mask_away]["away_team_goal"].values
    
    name_home = str(df1[mask_home]["team_long_name"].values[0]) + " @home"
    name_away = str(df2[mask_away]["team_long_name"].values[0]) + " @away"

    customdata1 = np.array([[h*1] for h in [y1]])
    customdata2 = np.array([[h*1] for h in [y2]])

    trace1 = go.Bar(y=x, 
                    x=-1 * y1, 
                    orientation="h", 
                    name=name_home,
                    marker={"color": ["teal"]},
                    customdata=customdata1,
                    hovertemplate=
                    "Goals: %{customdata}"
                   )
    trace2 = go.Bar(y=x, 
                    x=y2, 
                    orientation="h", 
                    name=name_away,
                    marker={"color": ["darkblue"]},
                    customdata=customdata2,
                    hovertemplate=
                    "Goals: %{customdata}"
                   )
    
    traces = [trace1, 
              trace2
             ]
    
    fig = go.Figure(traces).update_layout({"barmode": "relative", 
                                     "xaxis": {"range": [-5, 5]},
                                     "title": {"text": title, "x": 0.5},
                                     "legend": {"title": "legend", "orientation": "h", "visible":shlg},
                                    }).update_xaxes({"zerolinewidth":5, "zerolinecolor": "lightgreen", "showticklabels": False
                                    }).update_yaxes({"showticklabels": False})
    return [fig]