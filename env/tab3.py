import plotly.graph_objects as go
from dash import dcc, html


def render_tab(df):

    layout = html.Div(
        [
            html.H1("Kanały sprzedaży", style={"text-align": "center"}),
            html.Div(
                [
                    html.Div(
                        [
                            dcc.Dropdown(
                                id="store_type_dropdown",
                                options=[
                                    {"label": store, "value": store}
                                    for store in df["Store_type"].unique()
                                ],
                                value=df["Store_type"].unique()[0],
                            ),
                        ],
                        style={"width": "50%", "margin": "auto"},
                    ),
                    html.Div(
                        [
                            html.Div(
                                [dcc.Graph(id="bar-weekday-sales")],
                                style={"width": "50%"},
                            ),
                            html.Div(
                                [dcc.Graph(id="pie-customer-info")],
                                style={"width": "50%"},
                            ),
                        ],
                        style={"display": "flex", "justify-content": "space-around"},
                    ),
                ]
            ),
            html.Div(id="temp-out"),
        ]
    )

    return layout
