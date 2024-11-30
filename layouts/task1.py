from dash import dcc, html
import pandas as pd
import plotly.express as px
from utils.jira_client import get_jira_data
from datetime import datetime

DATA = get_jira_data()

def task1_layout():
    tasks = []
    for issue in DATA['issues']:
        created = datetime.strptime(issue['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
        resolutiondate = datetime.strptime(issue['fields']['resolutiondate'], '%Y-%m-%dT%H:%M:%S.%f%z')
        open_time = (resolutiondate - created).total_seconds() / 3600  # В часах
        tasks.append(open_time)

    df = pd.DataFrame({'Open Time (hours)': tasks})
    fig = px.histogram(df, x='Open Time (hours)', nbins=20, title='Гистограмма времени в открытом состоянии')

    return html.Div([
        html.H1("Task 1: Time in Open State"),
        dcc.Graph(figure=fig),
    ])