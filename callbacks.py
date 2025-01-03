from dash import Input, Output, State, ctx
import dash_mantine_components as dmc
import random

from charts import fig_scatterone, fig_scatterboth
from read_data import home, away
from color import simple_layout, color_home, color_away

def callbacks_baby(app):
    @app.callback(
        Output(component_id="comp0_SELECTselect_home", component_property="value"),
        Output(component_id="comp1_SELECTselect_away", component_property="value"),
        Input(component_id="comp6_SELECTclick_randsquare", component_property="n_clicks"),
        State(component_id="comp0_SELECTselect_home", component_property="value"),
        State(component_id="comp1_SELECTselect_away", component_property="value")
    )
    def nowshuffle(clicked, homename, awayname):
        if clicked:
            homename = random.choice(home["team_long_name"].values)
            awayname = random.choice(away["team_long_name"].values)
            return homename, awayname
        else:
            return homename, awayname
    @app.callback(
        Output("comp4_FIGfig_mob", "figure"),
        Output("comp2_FIGfig_home", "figure"),
        Output("comp3_FIGfig_away", "figure"),
        
        Input("comp0_SELECTselect_home", "value"),
        Input("comp1_SELECTselect_away", "value")
    )
    def leftptowncitypopulationme(value0, value1):
        return simple_layout(fig_scatterboth(value0, value1)).update_layout({
            "margin": {"t": 30, "b": 15, "r": 45, "l": 45},
        }), simple_layout(fig_scatterone(home, value0, color_home)), simple_layout(fig_scatterone(away, value1, color_away))
    
    @app.callback(
        Output("PAP_ms10_0", "children"),
        Output("PAP_ms10_2", "children"),
        Output("PAP_s11", "children"),

        Input("comp7_SELECTclick_playbutton", "n_clicks"),
        Input("comp5p0_SELECTclick_homeoraway", "value"),

        State("comp0_SELECTselect_home", "value"),
        State("comp1_SELECTselect_away", "value")
    )
    def nice(nclicks, homeoraway_switch, home_team, away_team):

        if nclicks is None:
            return "0", "0", dmc.Text("Place your bet.", className="nv1 e")

        else:
            if ctx.triggered_id== "comp7_SELECTclick_playbutton":

                home_score = random.choice(home[home["team_long_name"]== home_team]["home_team_goal"].values)
                away_score = random.choice(home[home["team_long_name"]== away_team]["home_team_goal"].values)

                if home_score > away_score:
                    if homeoraway_switch == "HOME":
                        return dmc.Text(f"{home_score}", c=color_home, className="nv0 e"), dmc.Text(f"{away_score}", c=color_home, className="nv0 e"), dmc.Text("You win!", className="nv1 e")
                    elif homeoraway_switch == "AWAY":
                        return dmc.Text(f"{home_score}", c=color_home, className="nv0 e"), dmc.Text(f"{away_score}", c=color_home, className="nv0 e"), dmc.Text("You lose...", className="nv1 e")
                elif home_score < away_score: 
                    if homeoraway_switch == "HOME":
                        return dmc.Text(f"{home_score}", c=color_away, className="nv0 e"), dmc.Text(f"{away_score}", c=color_away, className="nv0 e"), dmc.Text("You lose...", className="nv1 e")
                    elif homeoraway_switch == "AWAY":
                        return dmc.Text(f"{home_score}", c=color_away, className="nv0 e"), dmc.Text(f"{away_score}", c=color_away, className="nv0 e"), dmc.Text("You win!", className="nv1 e")
                elif home_score == away_score:
                    return dmc.Text(f"{home_score}", c="gray", className="nv0 e"), dmc.Text(f"{away_score}", c="gray", className="nv0 e"), dmc.Text("One point.", className="nv1 e")
            
            elif ctx.triggered_id == "comp5p0_SELECTclick_homeoraway":
                return "0", "0", dmc.Text("Place your bet.", className="nv1 e")

    @app.callback(
        Output("PAP_ms10_3", "children"),
        Output("PAP_ms10_4", "children"),
        
        Input("comp0_SELECTselect_home", "value"),
        Input("comp1_SELECTselect_away", "value")
    )
    def leftptowncitypopulationme(value0, value1):
        print(dmc.Text(f"{value0}", className="nv2 e"))
        return dmc.Text(f"{value0}", className="nv2 e"), dmc.Text(f"{value1}", className="nv2 e")
            
    # @app.callback(
    #     Output(component_id="PAP_ms10_3", component_property="value"),
    #     Output(component_id="PAP_ms10_4", component_property="value"),
    #     State(component_id="comp0_SELECTselect_home", component_property="value"),
    #     State(component_id="comp1_SELECTselect_away", component_property="value")
    # )
    # def oooyaaaa(hometeam, awayteam):
    #     return hometeam, awayteam
