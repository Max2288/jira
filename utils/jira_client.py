import requests

def get_jira_data():
    jira_url = 'https://issues.apache.org/jira/rest/api/2/search'
    query = {
        'jql': 'project = Kafka AND status = Closed',
        'fields': 'key,summary,created,resolutiondate,assignee,reporter,timespent,priority',
        'expand': 'changelog',
        'maxResults': 1000
    }
    response = requests.get(jira_url, params=query)
    response.raise_for_status()  # Если ошибка, выбрасываем исключение
    return response.json()
