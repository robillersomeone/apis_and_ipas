import dash
from dash_package import app
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_package.plots import *
import plotly.plotly as py
import plotly.graph_objs as go
import sqlalchemy


y0 = abv_box('Saison')
style = go.Box(
    y = y0,
    name = 'Saison',
     marker=dict(
        color='#3D9970'
))
data = [style]
layout = go.Layout(
    title= min_max_abv('Saison'),
    yaxis = dict(
        title='Alcohol Content by Volume',
    zeroline = False),
    boxmode = 'group'
)

app.layout = html.Div([

    html.H1("Learn more about your favorite beers!"),
    dcc.Dropdown(
        id = 'dropdown',
        options = dropdown(),
        value = 'Saison',
        clearable = False
        ),
    html.P(style_description("Saison"), id = 'style-description'),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Descriptive Words', children=[
            html.Div([
                html.H5(count_beers_in_style("Saison"), id = "beers_analyzed"),
                dcc.Graph(
                    id='beer-histogram',
                    figure={
                        'data': [plot_words('Saison')],
                        'marker':{'color':'rgb(101, 32, 31)'}
                    }
                )
            ])
        ]),
        dcc.Tab(label='Food Pairings', children=[
                html.H4(style_name("Saison"), id = "style"),
                html.H6(style_foodpairings('Saison'), id = "foodpairings")
        ]),
        dcc.Tab(label='ABV by style', children=[
                        html.Div([ dcc.Graph(
                            id='abv-box',
                            figure={'data':data,
                                    'layout':layout
                            }
                    )])])
        ]),

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
dash.dependencies.Output('beers_analyzed', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_description(selected_style):
    return count_beers_in_style(selected_style)

@app.callback(
dash.dependencies.Output('style-description', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_description(selected_style):
    return style_description(selected_style)

@app.callback(
dash.dependencies.Output('style', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_description(selected_style):
    return style_name(selected_style)

@app.callback(
dash.dependencies.Output('foodpairings', 'children'),
[dash.dependencies.Input('dropdown', 'value')])
def update_description(selected_style):
    return style_foodpairings(selected_style)

@app.callback(
dash.dependencies.Output('abv-box', 'figure'),
[dash.dependencies.Input('dropdown', 'value')])
def update_abvs(selected_style):
    y0 = abv_box(selected_style)#abv_box('Saison')
    style = go.Box(
        y = y0,
        name = selected_style,
         marker=dict(
        color='#3D9970'
    ))
    layout = go.Layout(
        title= min_max_abv(selected_style),
        yaxis = dict(
            title='Alcohol Content by Volume',
        zeroline = False),
        boxmode = 'group'
    )
    data = [style]
    return {'data': data,
            'layout':layout}

# @app.callback(
# dash.dependencies.Output('abv_range', 'children'),
# [dash.dependencies.Input('dropdown', 'value')])
# def update_abvs(selected_style):
#     return min_max_abv(selected_style)

if __name__ == '__main__':
    app.run_server(debug=True)
