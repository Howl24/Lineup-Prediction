import ipywidgets as widgets
import pickle
from IPython.display import display
import pandas as pd


team_df = pd.read_csv("team_df.csv").set_index("team")
ages = pd.Series.from_csv("ages.csv")
fifa = pd.Series.from_csv("fifa.csv")

team_list = list(team_df.index)

with open("modelo_wdl.p", "rb") as file:
    modelo = pickle.load(file)
    
def prediccion(btn):
    team1 = team1_dd.value
    team2 = team2_dd.value
    
    team1_attrs = team_df.loc[team1]
    team2_attrs = team_df.loc[team2]    
    
    match_row = {}
    #match_row['diff_partidos_jugados'] = team1_attrs['matches_played'] - team2_attrs['matches_played']
    match_row['diff_ratio_wins'] = team1_attrs['ratio_wins'] - team2_attrs['ratio_wins']
    match_row['diff_ratio_draws'] = team1_attrs['ratio_draws'] - team2_attrs['ratio_draws']
    match_row['diff_ratio_losses'] = team1_attrs['ratio_losses'] - team2_attrs['ratio_losses']
    match_row['diff_avg_goals_for'] = team1_attrs['avg_goals_for'] - team2_attrs['avg_goals_for']
    match_row['diff_avg_goals_against'] = team1_attrs['avg_goals_against'] - team2_attrs['avg_goals_against']
    match_row['diff_avg_age'] = ages[team1] - ages[team2]
    match_row['diff_ranking'] = float(fifa.loc[team1]) - float(fifa.loc[team2])
    
    X_test = pd.DataFrame([match_row]).values
    resultado = modelo.predict(X_test)
    
    if resultado == 1:
        print(team2)
    elif resultado == 2:
        print("Empate")
    else:
        print(team1)

team1_dd = widgets.Dropdown(options=team_list,
                 description="Equipo 1: ")

team2_dd = widgets.Dropdown(options=team_list,
                 description="Equipo 2: ")

btn = widgets.Button(description="Aceptar", 
                     button_style="")

btn.on_click(prediccion)

menu = widgets.HBox([team1_dd, team2_dd, btn])
resultado = widgets.

def render():
    display(menu)