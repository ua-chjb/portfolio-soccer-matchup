import plotly.express as px

from read_data import label_dct

plot_color = "#efefef"
font_color = "black"

font_size = 10
title_size = 14

grid_color = "white"
grid_width = 2
axis_color = "white"
line_width = 2


def simple_layout(fig):

    return fig.update_layout({
        "plot_bgcolor": plot_color,
        "font": {"color": font_color, "size": font_size},
        "clickmode": "select",
        "title": {"x": 0.5, "font": {"size": title_size}},
        "legend": {"visible": False},
        "barcornerradius": 10,
        "coloraxis":{"showscale": False},
        "margin": {"t": 45, "b": 15, "r": 15, "l": 15},
        "scene": {
            "xaxis": {"backgroundcolor": plot_color},
            "yaxis": {"backgroundcolor": plot_color},
            "zaxis": {"backgroundcolor": plot_color}
        }
    }).update_xaxes({
        "showgrid": True,
        "zeroline": False,
        "showline": True,
        "mirror": False,
        "gridcolor": grid_color,
        "gridwidth": grid_width,
        "linecolor": axis_color,
        "linewidth": line_width,
        "ticks": ""
    }).update_yaxes({
        "showgrid": True,
        "zeroline": False,
        "showline": True,
        "mirror": False,
        "gridcolor": grid_color,
        "gridwidth": grid_width,
        "linecolor": axis_color,
        "linewidth": line_width,
        "ticks": ""
    }).update_polars({
        "bgcolor": plot_color,
        "angularaxis": {
            "direction": "clockwise",
            "gridwidth": grid_width,
            "labelalias": label_dct
        },
        "radialaxis": {
            "gridwidth": grid_width
        },
    })


color_home = "lightblue"
color_away = "lightgreen"

external_stylesheets = ["https://fonts.googleapis.com/css2?family=Nova+Square&display=swap"]