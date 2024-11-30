from dash import dcc, html
import pandas as pd
import plotly.express as px
from utils.jira_client import get_jira_data

DATA = get_jira_data()


def task4_layout():
    issues = DATA['issues']

    user_data = []
    for issue in issues:
        assignee = issue['fields']['assignee']['displayName'] if issue['fields']['assignee'] else "Unassigned"
        reporter = issue['fields']['reporter']['displayName'] if issue['fields']['reporter'] else "Unknown Reporter"

        user_data.append({'User': assignee, 'Role': 'Assignee'})
        user_data.append({'User': reporter, 'Role': 'Reporter'})

    df = pd.DataFrame(user_data)

    user_counts = df.groupby(['User', 'Role']).size().reset_index(name='Count')

    total_counts = user_counts.groupby('User')['Count'].sum().sort_values(ascending=False).head(30).index
    top_users = user_counts[user_counts['User'].isin(total_counts)]

    fig = px.bar(
        top_users,
        x='Count',
        y='User',
        color='Role',
        orientation='h',
        title='Количество задач для пользователей (исполнитель и репортер)',
        labels={'Count': 'Количество задач', 'User': 'Пользователь'}
    )
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})

    return html.Div([
        html.H1("Task 4: Task Distribution by Users"),
        dcc.Graph(figure=fig),
    ])


