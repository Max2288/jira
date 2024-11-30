from dash import dcc, html
import pandas as pd
import plotly.express as px
from utils.jira_client import get_jira_data
from datetime import datetime

DATA = get_jira_data()

def task2_layout():
    state_times = []

    for issue in DATA['issues']:
        changelog = issue.get('changelog', {}).get('histories', [])
        created = datetime.strptime(issue['fields']['created'], '%Y-%m-%dT%H:%M:%S.%f%z')

        transitions = []
        for change in changelog:
            for item in change['items']:
                if item['field'] == 'status':
                    transition_time = datetime.strptime(change['created'], '%Y-%m-%dT%H:%M:%S.%f%z')
                    transitions.append((item['fromString'], item['toString'], transition_time))

        transitions.sort(key=lambda x: x[2])
        for i, (from_status, to_status, transition_time) in enumerate(transitions):
            if i == 0:
                duration = (transition_time - created).total_seconds() / 3600  # Время в часах
                state_times.append({'State': from_status, 'Time in State (hours)': duration})

            if i > 0:
                prev_time = transitions[i - 1][2]
                duration = (transition_time - prev_time).total_seconds() / 3600
                state_times.append({'State': from_status, 'Time in State (hours)': duration})

        if transitions:
            last_status, _, last_time = transitions[-1]
            resolution_time = datetime.strptime(issue['fields']['resolutiondate'], '%Y-%m-%dT%H:%M:%S.%f%z')
            duration = (resolution_time - last_time).total_seconds() / 3600
            state_times.append({'State': last_status, 'Time in State (hours)': duration})

    df = pd.DataFrame(state_times)
    unique_states = df['State'].unique()


    graphs = []
    for state in unique_states:
        fig = px.histogram(
            df[df['State'] == state],
            x='Time in State (hours)',
            nbins=20,
            title=f'Время задач в состоянии: {state}'
        ).update_layout(
                xaxis_title='Время в состоянии (часы)',
                yaxis_title='Количество задач',
                template='plotly_white'
        )
        graphs.append(html.Div([
            html.H3(f"State: {state}"),
            dcc.Graph(figure=fig)
        ]))

    return html.Div([
        html.H1("Task 2: Time Distribution by State"),
        *graphs,
    ])
