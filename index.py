import dash_mantine_components as dmc
from dash import html, dcc, _dash_renderer
from dash_iconify import DashIconify
_dash_renderer._set_react_version('18.2.0')

from read_data import home, away, cols
from color import color_home, color_away

comp0_select_home = dmc.Card(
    [
        dmc.Select(
            label="HOME",
            leftSection=DashIconify(icon="fa:soccer-ball-o", color=color_home),
            placeholder="select a team",
            data=home["team_long_name"].unique(),
            value=home["team_long_name"].unique()[0],
            searchable=True,
            clearable=False,
            id="comp0_SELECTselect_home"
        )
    ],
    withBorder=True,
    radius="md",
    shadow="sm",
    className="t s0"
)

comp1_select_away = dmc.Card(
    [
        dmc.Select(
            label="AWAY",
            leftSection=DashIconify(icon="fa:soccer-ball-o", color=color_away),
            placeholder="select a team",
            data=away["team_long_name"].unique(),
            value=away["team_long_name"].unique()[0],
            searchable=True,
            clearable=False,
            id="comp1_SELECTselect_away"
        )
    ],
    withBorder=True,
    radius="md",
    shadow="sm",
    className="t s1"
)

comp2_fig_home = dmc.Card(
    [
        dcc.Graph(
            figure={},
            id="comp2_FIGfig_home",
            # config={
            #     "responsive": True
            # }
        )
    ],
    className="t s2"    
)

comp3_fig_away = dmc.Card(
    [
        dcc.Graph(
            figure={},
            id="comp3_FIGfig_away",
            # config={
            #     "responsive": True
            # }
        )
    ],
    className="t s3"    
)

comp4_fig_both = dmc.Card(
    [
        dcc.Graph(
            figure={},
            id="comp4_FIGfig_mob",
            # config={
            #     "responsive": True
            # }            
        )
    ],
    className="t s4"
)

comp5_click_homeoraway = dmc.Card(
    [
        dmc.SegmentedControl(
            data=["HOME", "AWAY"],
            value="HOME",
            id="comp5p0_SELECTclick_homeoraway"
        ),
    ],
    className="t s5"
)

comp6_click_randsquare = dmc.Card(
    [
        dmc.Button(
            DashIconify(icon="mdi:dice-5", width=30, color="white"),
            color="rgb(8,81,156)",
            size="xs", 
            radius="xl",
            variant="gradient",
            gradient = { 'from': str(color_home), 'to': str(color_away), 'deg': 135},
            id="comp6_SELECTclick_randsquare",
            )
    ],
    className="t s6"
)

comp7_click_playbutton = dmc.Card(
    [
        dmc.Button(
            "PLAY",
            color="rgb(8,81,156)",
            size="xl", 
            radius="xl",
            variant="gradient",
            gradient = { 'from': str(color_home), 'to': str(color_away), 'deg': 135},
            id="comp7_SELECTclick_playbutton"
            )
    ],
    className="t s7",
)

comp9_text_des = dmc.Card(
    [
        dmc.Text(
            "HOW ARE SCORES CALCULATED?",
            size="l",
            fw=500,
            className="text_header"
        ),
        dmc.Text(
            [
                """
                This data comes from the 
                """,
                dmc.Anchor(
                    "European Soccer Database", href="https://www.kaggle.com/datasets/hugomathien/soccer", target="_blank", size="sm"
                ),
                """, a SQLite database of +25,000 matches from seasons 2008-2016. The home and away scores are randomly selected from the designated team's matches at home or away, respectively. Randomization comes from random module.
                """
            ],
            size="sm",
            c="gray",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t s9"
)

comp10_paper_scores = dmc.Paper(
    [
        dmc.Text(
            [

            ],
            id="PAP_ms10_3",
            className="t ms10_3 e"
        ),
        dmc.Text(
            [
                
            ],
            id="PAP_ms10_0",
            className="t ms10_0 nv0 e"
        ),

        dmc.Text(
            [
                dmc.Text(
                    "-", 
                    size="xl", 
                    className=" nv_m"
                )
            ],
            className="t ms10_1 e"
        ),
        
        dmc.Text(
            [

            ],
            id="PAP_ms10_4",
            className="t ms10_4 e"
        ),
        dmc.Text(
            [

            ],
            id="PAP_ms10_2",      
            className="t ms10_2 nv0 e"
        ),
    ],
    withBorder=True,
    radius="md",
    # shadow="sm",
    className="t ms10",
)
    
comp11_text_result = dmc.Card(
    [
        dmc.Text(
            [

            ],
            id="PAP_s11",
            className="nv1 e"
        )
    ],
    className="t s11"
)

block0_mob  = html.Div(
    [
        comp0_select_home,
        comp1_select_away,
        comp6_click_randsquare,
        comp4_fig_both,
        comp2_fig_home,
        comp3_fig_away,
        comp5_click_homeoraway,
        comp10_paper_scores,
        comp11_text_result,
        comp7_click_playbutton,
        comp9_text_des
    ],
    className="d"
)

# # # # # # # # # # # # # # footer # # # # # # # # # # # # # #

icon_github = DashIconify(icon="simple-icons:github", width=30, color="white", className="bb")
link_github = "https://www.github.com/ua-chjb"
icon_linkedin = DashIconify(icon="devicon-plain:linkedin", width=30, color="white", className="bb")
link_linkedin = "https://linkedin.com/in/benjaminbnoyes"
icon_email = DashIconify(icon="mdi:email", width=30, color="white", className="bb")
link_email = "mailto:noyesbenjamin7@gmail.com"
icon_spotify = DashIconify(icon="cib:spotify", width=30, color="white", className="bb")
link_spotify = "https://open.spotify.com/playlist/50WTakgz8xAQlCpO8bzUF9?si=Hv5E5JpVQZiBdTsnljBZrg"
icon_soundcloud = DashIconify(icon="cib:soundcloud", width=40, color="white", className="bb")
link_soundcloud = "https://soundcloud.com/bennoyes-onb"  


comp20_footer0_github = dmc.Anchor(
    icon_github, href=link_github, target="_blank", 
    size="xl",
    className="footnt comp20_footer0_github"
)

comp21_footer1_linkedin = dmc.Anchor(
    icon_linkedin, href=link_linkedin, target="_blank", 
    size="xl",
    className="footnt comp21_footer1_linkedin"
)

comp22_footer2_email = dmc.Anchor(
    icon_email, href=link_email, target="_blank", 
    size="sm",
    className="footnt comp22_footer2_email"
)

comp23_footer3_spotify = dmc.Anchor(
    icon_spotify, href=link_spotify, target="_blank", 
    size="xl",
    className="footnt comp23_footer3_spotify"
)

comp24_footer4_soundcloud = dmc.Anchor(
    icon_soundcloud, href=link_soundcloud, target="_blank",
    size="xl",
    className="footnt comp24_footer4_soundcloud"
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2024 all rights reserved",
    className="footertinytext"
)

footer = html.Div(
    [
        comp20_footer0_github,
        comp21_footer1_linkedin,
        comp22_footer2_email,
        comp23_footer3_spotify,
        comp24_footer4_soundcloud,
        comp25_copyrightfooter
    ],
    className="f"
)
# # # # # # # # # # # # # # footer # # # # # # # # # # # # # #

title = html.Div(
    [
        dmc.Text(
            [
                "Soccer Simulator"
            ],
            size="xl",
            fw=500,
            className="tit_ex"
        )
    ],
    className="tit"
)

# # # # # # # # # # # # # # final composition # # # # # # # # # # # # # #

lyt = dmc.MantineProvider(
    [
        title,
        block0_mob,
        footer
    ]
)
