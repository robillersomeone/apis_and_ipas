import dash
from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_package.plots import *
import plotly.plotly as py
import plotly.graph_objs as go
import sqlalchemy


app.layout = html.Div([
    html.H1("Do you know your beer style?"),

    dcc.Dropdown(
        id = 'dropdown',
        options = dropdown(),
        value = 'Brown Porter',
        clearable = False
        ),
    dcc.Graph(id = 'beer-histogram',
              figure = {
              'data': [plot_words('American IPA')],
              'layout' : {
                'title': 'testing'
                      }
                        }
        )

])
@app.callback(
    dash.dependencies.Output('beer-histogram', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_figure(selected_style):
    return {
            'data': [plot_words(selected_style)],
            'layout' : {'title': 'Top Descriptor Words'}
        }

if __name__ == '__main__':
    app.run_server(debug=True)
