from dash import dcc, html
import pandas as pd
from utils.jira_client import get_jira_data
import plotly.graph_objects as go
from datetime import datetime

DATA = get_jira_data()


def task3_layout():
    issues = DATA['issues']
    rows = []
    for issue in issues:
        created_date = datetime.strptime(issue['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z').date()
        resolution_date = datetime.strptime(issue['fields']['resolutiondate'], '%Y-%m-%dT%H:%M:%S.%f%z').date()
        rows.append({'Date': created_date, 'Type': 'Created'})
        rows.append({'Date': resolution_date, 'Type': 'Closed'})

    df = pd.DataFrame(rows)
    daily_counts = df.groupby(['Date', 'Type']).size().reset_index(name='Count')
    all_dates = pd.date_range(daily_counts['Date'].min(), daily_counts['Date'].max())
    created_counts = daily_counts[daily_counts['Type'] == 'Created'].set_index('Date').reindex(all_dates, fill_value=0)[
        'Count']
    closed_counts = daily_counts[daily_counts['Type'] == 'Closed'].set_index('Date').reindex(all_dates, fill_value=0)[
        'Count']
    cumulative_created = created_counts.cumsum()
    cumulative_closed = closed_counts.cumsum()

    fig = go.Figure()
    fig.add_trace(go.Bar(x=all_dates, y=created_counts, name="Created (Daily)", marker_color="blue"))
    fig.add_trace(go.Bar(x=all_dates, y=closed_counts, name="Closed (Daily)", marker_color="red"))
    fig.add_trace(go.Scatter(x=all_dates, y=cumulative_created, mode="lines", name="Created (Cumulative)",
                             line=dict(color="blue", width=2)))
    fig.add_trace(go.Scatter(x=all_dates, y=cumulative_closed, mode="lines", name="Closed (Cumulative)",
                             line=dict(color="red", width=2)))

    fig.update_layout(
        title="Количество заведенных и закрытых задач с накопительным итогом",
        xaxis_title="Дата",
        yaxis_title="Количество задач",
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return html.Div([
        html.H1("Task 3: Opened and Closed Issues Over Time"),
        dcc.Graph(figure=fig),
    ])
