# streaming-neo4j
neo4j streaming data model 

## Entities (nodes):
User, Movie, Series, Genre, Actor, Director

## Connections (relations):
WATCHED (w/ rating property), ACTED_IN, DIRECTED, IN_GENRE

## How to run:
_(Requirement: docker and docker compose installed. UV also, recommended)_
#### Resolve and install pyproject.toml dependencies 

```bash
uv sync
```

#### Running docker to up db

```bash
docker compose up -d
```


#### Activating virtual environment 
- macOS / Linux: source .venv/bin/activate
- Windows (PowerShell/Win Terminal): .venv\Scripts\activate

#### Running queries

```bash
python3 code/python/db_queries.py
```
```

```
