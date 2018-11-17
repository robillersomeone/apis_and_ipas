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
    html.H1("But do you rly know your beer style?"),

    dcc.Dropdown(
        id = 'dropdown',
        options = dropdown(),
        value = 'Brown Porter',
        clearable = False
        ),

    html.P(style_description("Brown Porter"), id = 'style-description'),

    html.H3(min_max_abv("Brown Porter"), id = 'abv_range'),

    # html.H4(avg_abv("Brown Porter")),

    dcc.Graph(id = 'beer-histogram',
              figure = {
              'data': [plot_words('Brown Porter')]
                        }
        )

])
@app.callback(
    dash.dependencies.Output('beer-histogram', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_figure(selected_style):
    return {
            'data': [plot_words(selected_style)],
            'layout' : {'title': f'Out of all the beers labeled "{selected_style}", here are the top words in their descriptions:'}
        }

@app.callback(
dash.dependencies.Output('style-description', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_description(selected_style):
    return style_description(selected_style)

@app.callback(
dash.dependencies.Output('abv_range', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_abvs(selected_style):
    return min_max_abv(selected_style)


if __name__ == '__main__':
    app.run_server(debug=True)
