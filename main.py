import dash
from dash import html, page_container

from layouts.task1 import *
from layouts.task2 import *
from layouts.task3 import *
from layouts.task4 import *
from layouts.task5 import *
from layouts.task6 import *

app = dash.Dash(__name__, use_pages=True, pages_folder='')

app.layout = html.Div([
    html.H1("Dash Application for JIRA Analytics"),
    html.Nav([
        html.A("Task 1: Open Time Histogram", href="/task1", style={'margin-right': '20px'}),
        html.A("Task 2: Time by State", href="/task2", style={'margin-right': '20px'}),
        html.A("Task 3: Created and Closed Issues", href="/task3", style={'margin-right': '20px'}),
        html.A("Task 4: User Task Distribution", href="/task4", style={'margin-right': '20px'}),
        html.A("Task 5: Logged Time Histogram", href="/task5", style={'margin-right': '20px'}),
        html.A("Task 6: Issues by Priority", href="/task6", style={'margin-right': '20px'}),
    ]),
    page_container
])

dash.register_page("task1", path="/task1", layout=task1_layout())
dash.register_page("task2", path="/task2", layout=task2_layout())
dash.register_page("task3", path="/task3", layout=task3_layout())
dash.register_page("task4", path="/task4", layout=task4_layout())
dash.register_page("task5", path="/task5", layout=task5_layout())
dash.register_page("task6", path="/task6", layout=task6_layout())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
