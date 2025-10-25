import pandas as pd
import seaborn as sns
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
tips = sns.load_dataset("tips")
# Add tip percentage
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Tips Dashboard (Beginner)"),
    html.Div([
        html.Label('Filter by day'),
        dcc.Dropdown(
            id="day-filter",
            options=[{"label": d, "value": d} for d in sorted(tips["day"].unique())] + [{"label": "All", "value": "All"}],
            value="All",
            clearable=False,
            style={"width":"200px"}
        )
    ]),
    html.Div([
        html.Label('Max party size'),
        dcc.Slider(
            id="size-slider",
            min=int(tips["size"].min()),
            max=int(tips["size"].max()),
            value=int(tips["size"].max()),
            marks={i: str(i) for i in range(int(tips["size"].min()), int(tips["size"].max())+1)},
            step=1
        )
    ], style={"width":"50%","padding":"20px 0px"}),

    dcc.Graph(id="scatter-graph"),
    dcc.Graph(id="bar-graph")
])


@app.callback(
    Output("scatter-graph", "figure"),
    Output("bar-graph", "figure"),
    Input("day-filter", "value"),
    Input("size-slider", "value")
)
def update_charts(selected_day, max_size):
    df = tips.copy()
    if selected_day != "All":
        df = df[df["day"] == selected_day]
    df = df[df["size"] <= max_size]

    scatter = px.scatter(
        df, x="total_bill", y="tip", color="smoker", size="size",
        hover_data=["day", "time", "tip_pct"], title="Total Bill vs Tip"
    )

    bar = px.bar(
        df.groupby("day", as_index=False)["tip_pct"].mean(),
        x="day", y="tip_pct", title="Average Tip Percentage by Day"
    )

    return scatter, bar


if __name__ == "__main__":
    app.run_server(debug=True)
