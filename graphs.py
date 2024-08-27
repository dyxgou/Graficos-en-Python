from dash import Dash, Input, Output, callback, dcc, html
import plotly.express as px
import pandas as pd

poblacion_url = (
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)
datos = pd.read_csv(poblacion_url)


app = Dash()

app.layout = [
    html.H1(
        "Este es mi grafiquito",
        style={"textAlign": "center", "fontFamily": "system-ui"},
    ),
    dcc.Dropdown(datos.country.unique(), "Colombia", id="dropdown-section"),
    dcc.Graph(id="graph-content"),
]


@callback(Output("graph-content", "figure"), Input("dropdown-section", "value"))
def actualizar_grafico(value):
    pais = datos[datos.country == value]
    return px.line(pais, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True)
