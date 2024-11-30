from dash import dcc, html
import pandas as pd
import plotly.express as px
from utils.jira_client import get_jira_data

DATA = get_jira_data()


def task6_layout():
    issues = DATA['issues']

    priorities = [issue['fields']['priority']['name'] if issue['fields']['priority'] else 'Undefined' for issue in issues]

    df = pd.DataFrame({'Priority': priorities})
    priority_counts = df['Priority'].value_counts().reset_index()
    priority_counts.columns = ['Priority', 'Count']

    priority_order = ['Critical', 'Blocker', 'Major', 'Minor', 'Trivial', 'Undefined']
    priority_counts['Priority'] = pd.Categorical(priority_counts['Priority'], categories=priority_order, ordered=True)
    priority_counts.sort_values('Priority', inplace=True)

    fig = px.bar(
        priority_counts,
        x='Priority',
        y='Count',
        title='Количество задач по степени серьезности',
        labels={'Priority': 'Степень серьезности', 'Count': 'Количество задач'},
        text='Count'
    )
    fig.update_traces(textposition='outside')

    return html.Div([
        html.H1("Task 6: Issues by Priority"),
        dcc.Graph(figure=fig),
    ])