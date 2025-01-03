import pandas as pd

# import os
# from google.cloud import storage

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dash-app-4-soccermatchups-6102ec5ed535.json"

# client = storage.Client()

# read in data

home_repo = "C:/Users/benno/OneDrive/Python/Dash/Deployment_ready/soccer_scores/deploy2/assets/data/home_all.csv"
away_repo = "C:/Users/benno/OneDrive/Python/Dash/Deployment_ready/soccer_scores/deploy2/assets/data/away_all.csv"

home = pd.read_csv(home_repo)
away = pd.read_csv(away_repo)

cols = ['buildUpPlaySpeed', 'buildUpPlayDribbling', 'buildUpPlayPassing', 
        'chanceCreationPassing', 'chanceCreationCrossing', 'chanceCreationShooting', 
        'defencePressure', 'defenceAggression', 'defenceTeamWidth']

home = home.sort_values(by=["home_team_goal"], ascending=False)
away = away.sort_values(by=["away_team_goal"], ascending=False)

label_dct = {
    'buildUpPlaySpeed': 'BuildSpeed',
    'buildUpPlayDribbling': 'BuildDribb',  
    'buildUpPlayPassing': 'BuildPass',
    'chanceCreationPassing': 'OppPass',
    'chanceCreationCrossing': 'OppCross',
    'chanceCreationShooting': 'OppShoot',
    'defencePressure': 'DefPress',
    'defenceAggression': 'DefAgg',
    'defenceTeamWidth': 'DefWidth'
}