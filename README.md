# Dash App with Docker Compose

This project serves a multi-page Dash application using Docker Compose for easy deployment and orchestration.

## Project Structure

```
.
├── layouts/taskX       # Solution for task X
├── utils/jira_client   # Recieving jira data
├── main.py             # Main Dash application file
├── Dockerfile          # Dockerfile to build the application image
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation (this file)
```

## Installation and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Max2288/jira
```

### 2. Build the Docker Image and Run
```bash
docker-compose up --build
```

### 3. Access the Application

The following routes are available:
> [http://localhost:8050/task1](http://localhost:8050/task1): First task visualization.

> [http://localhost:8050/task2](http://localhost:8050/task2): Second task visualization.

>  [http://localhost:8050/task3](http://localhost:8050/task3): Third task visualization.

> [http://localhost:8050/task4](http://localhost:8050/task4): Fourth task visualization.

>  [http://localhost:8050/task5](http://localhost:8050/task5): Fifth task visualization.

> [http://localhost:8050/task6](http://localhost:8050/task6): Sixth task visualization.

