from dash import dcc, html
import pandas as pd
import plotly.express as px
from utils.jira_client import get_jira_data

DATA = get_jira_data()


def task5_layout():
    issues = DATA['issues']
    task_data = []
    for issue in issues:
        changelog = issue['changelog']['histories']
        closed_time = None
        started_time = None

        for change in changelog:
            for item in change['items']:
                if item['field'] == 'status':
                    if item['toString'] == 'Closed':
                        closed_time = change['created']
                    elif item['toString'] in ['In Progress', 'Open']:
                        started_time = change['created']

        if closed_time and started_time:
            closed_time = pd.to_datetime(closed_time)
            started_time = pd.to_datetime(started_time)
            duration = (closed_time - started_time).total_seconds() / 3600  # Часы
            task_data.append(duration)

    df = pd.DataFrame({'TimeSpentHours': task_data})

    bins = [0, 1, 2, 4, 8, 16, 32, 64, 128]
    labels = ['<1h', '1-2h', '2-4h', '4-8h', '8-16h', '16-32h', '32-64h', '64-128h']
    df['TimeCategory'] = pd.cut(df['TimeSpentHours'], bins=bins, labels=labels, right=False)

    grouped = df['TimeCategory'].value_counts().reset_index()
    grouped.columns = ['TimeCategory', 'TaskCount']
    grouped.sort_values('TimeCategory', inplace=True)

    fig = px.bar(
        grouped,
        x='TimeCategory',
        y='TaskCount',
        title='Время выполнения задач (часы)',
        labels={'TimeCategory': 'Категория времени', 'TaskCount': 'Количество задач'},
        text='TaskCount'
    )
    fig.update_traces(textposition='outside')

    return html.Div([
        html.H1("Task 5: Logged Time Histogram"),
        dcc.Graph(figure=fig),
    ])
