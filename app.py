from dash import Dash
import dash_mantine_components as dmc

from color import external_stylesheets
from index import lyt
from callbacks import callbacks_baby

app = Dash(__name__, external_stylesheets=external_stylesheets+[dmc.styles.CHARTS])

app.layout = lyt

callbacks_baby(app)

server = app.server

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8050")