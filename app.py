import numpy as np
import pandas as pd
import dash
from dash.dependencies import Input, Output, State, MATCH
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import os
import sys
PATH = os.getcwd()

df = pd.read_csv(PATH+"//data//data_netflix.csv",  index_col=[0])

def generate_card(movie_id, movie, description, cast, genre):

    not_available = "Not Available"
    
    if isinstance(description,float):
        description = not_available
    if isinstance(cast,float):
        cast = not_available
    if isinstance(genre,float):
        genre = not_available
    
    card = html.Div(children=
        [
        
            html.Div(f"ID: {movie_id}", className="card-header"),
            html.Div(
                [
                    html.H4(f"{movie}", id=f'id-{movie_id}', className='card-title'),
                    html.Hr(className="my-4"),
                    html.P(f"{description}", className="card-text"),
                    html.Hr(className="my-4"),
                    html.H5("Cast", className='card-title'),
                    html.P(f"{cast}", className="card-text"),
                    html.Hr(className="my-4"),
                    html.H5("Genre", className='card-title'),
                    html.P(f"{genre}", className="card-text"),
                ], className="card-body",style={'overflow-y':'scroll'})
        ], id='id-card',className='card border-primary mb-3', style={'height':'16rem'}
    ),
    return card

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

server = app.server

app.layout = html.Div(children=[
    html.Div(children=[
        html.H1('Movie Recommender System', className="display-3"),
        html.P('An engine that recommends Movies or Tv Shows related to the search key.', className="lead"),
        html.Hr(className="my-4")
        ],
        className="jumbotron",
        style={'margin':'auto','width':'70%', 'height':'260px', 'position':'relative', 'top':'50px'}
    ),
    html.Div(children=[
        dcc.Dropdown(
            id='id-dropdown',
            options=[
                    {'label': df.title.iloc[i], 'value': df.title.iloc[i]} for i in range(df.shape[0])
                ],
            value='', 
            placeholder="Choose a Movie or Tv Show",
            style={'flex-grow':'2'}
            ),
        dbc.Button("Submit", id='id-button', color="primary", className="mr-1",style={'flex-grow':'1'}
            )
        ],
        style={'margin':'auto','width':'40%', 'display':'flex', 'padding-top':'60px'}
    ),
    html.Div(id='id-cards', style={'margin':'auto', 'padding-left':'15%'})  
]
)


@app.callback(
    Output(component_id='id-cards', component_property='children'),
    [Input(component_id='id-button', component_property='n_clicks')],
    [State(component_id='id-dropdown', component_property='value')]
)
def generate_recommendation(n_clicks,value):
    print(value)
    if value in df.title.values:
        movie_id = df[df.title == value].index[0]
        cs = np.load(PATH+'//data//cv_f2.npy')
        scores = sorted(list(enumerate(cs[movie_id])), key=lambda score: score[1])
        scores.reverse()

        movies = scores[1:11]
        
        cards = html.Div(children=[
            dbc.Row(
               [dbc.Col(generate_card(
                   movies[i][0], 
                   df.title.iloc[movies[i][0]], 
                   df.description.iloc[movies[i][0]],
                   df.cast.iloc[movies[i][0]],
                   df.listed_in.iloc[movies[i][0]]
                   ), width=2) for i in range(5)]
            ,align="start"),
            dbc.Row(  
               [dbc.Col(generate_card(
                   movies[i+5][0], 
                   df.title.iloc[movies[i+5][0]], 
                   df.description.iloc[movies[i+5][0]],
                   df.cast.iloc[movies[i+5][0]],
                   df.listed_in.iloc[movies[i+5][0]]
                   ), width=2) for i in range(5)]
            ,align="center")
        ], style={'margin':'auto','position':'relative','top':'20px'})
        
        return cards
    else:
        return html.Div()



if __name__=='__main__':
    app.run_server()