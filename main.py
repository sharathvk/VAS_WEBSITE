import dash
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# ------------------ PAGES ------------------

# Index Page (Main Menu)
index_page = dbc.Container([
    html.H1("VAS Group", className="text-center my-4"),

    dbc.Row([
        dbc.Col(
            dbc.Button("Go to About", href="/about", color="primary", className="w-100"),
            md=4
        ),
        dbc.Col(
            dbc.Button("Go to Services", href="/services", color="success", className="w-100"),
            md=4
        ),
        dbc.Col(
            dbc.Button("Go to Contact", href="/contact", color="warning", className="w-100"),
            md=4
        ),
    ], className="g-3")
])

# Other Pages
about_page = dbc.Container([
    html.H2("About Page"),
    html.P("This is About Us"),
    dbc.Button("Back to Home", href="/", color="secondary")
])

services_page = dbc.Container([
    html.H2("Services Page"),
    html.P("Our services list"),
    dbc.Button("Back to Home", href="/", color="secondary")
])

contact_page = dbc.Container([
    html.H2("Contact Page"),
    html.P("Contact details here"),
    dbc.Button("Back to Home", href="/", color="secondary")
])

# ------------------ APP LAYOUT ------------------

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content")
])

# ------------------ ROUTING ------------------

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/about":
        return about_page
    elif pathname == "/services":
        return services_page
    elif pathname == "/contact":
        return contact_page
    else:
        return index_page

# ------------------ RUN ------------------



if __name__ == "__main__":
    app.run(debug=True)