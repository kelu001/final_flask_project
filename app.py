# Import des bibliothèques nécessaires
from dash import dcc, html, Dash
import plotly.express as px
from pandas import read_csv

# Initialisation de l'application Dash
app = Dash(__name__)

# Préparation des données pour Plotly
data = read_csv('data/S_CLIENTS_JAN_MAR_2015.csv', sep=';')
# on ne conserve que les réservation "checked-out"
data = data[data['resv_status'] == 'CHECKED OUT']
# Suppression des colonnes non désirées
data = data.drop(['arrival', 'departure', 'nb_rsv', 'nights', 'sejour_id', 'sejour_we',
                  'day_use', 'room_type_id', 'company_id', 'agent_id', 'rate_code', 'first_stay',
                  'party_code', 'exclu_prestay', 'source_code', 'ca_act', 'ca_div', 'ca_div', 'ca_golf',
                  'ca_heb', 'ca_heb_paye', 'ca_heb_sys', 'ca_mus', 'ca_nr', 'ca_rest', 'ca_soins', 'ca_tot_sys',
                  'ca_tot_paye', 'resv_status', 'group_id', 'booked_room_type', 'group_id', 'source_prof_id',
                  'insert_date', 'adults', 'children', 'src_client_id'], axis=1)


# création de la première figure
fig1 = px.bar(data, x='channel', y='ca_tot', color='channel', width=500)
fig1.update_layout(bargap=0.1)

fig2 = px.pie(data, names='channel', values='ca_tot', color='channel')

# Définir le layout de l'application avec des composants Dash et un graphique Plotly
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for Python.'''),
    dcc.Graph(  # Affichage du premier graph
        id='bar-graph',
        figure=fig1),
    html.Br(),
    dcc.Graph(  # Affichage du second graph
        id='pie-graph',
        figure=fig2),
])


# Lancer le serveur
if __name__ == '__main__':
    app.run_server(debug=True)
