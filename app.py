import dash
import dash_core_components as dcc
import dash_html_components as html
import * from get_histogram


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Check Out These Beers!'),

    html.Div(children='''
        How are beers described?
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
