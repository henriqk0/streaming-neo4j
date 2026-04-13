# streaming-neo4j

## Entities (nodes):

User, Movie, Series, Genre, Actor, Director

## Connections (relations):

WATCHED (w/ rating property), ACTED\_IN, DIRECTED, IN\_GENRE

-----

## Why use Neo4j?

For streaming platforms, data is inherently interconnected. Traditional relational databases (SQL) struggle with deep relationships because they rely on complex `JOIN` operations, which become computationally expensive as your dataset grows.

Neo4j is a **graph database** that treats relationships as first-class citizens. By storing data as nodes and edges, you gain several advantages:

  * **Relationship Performance:** Traversing relationships (e.g., "Find all movies in the Thriller genre that a user's friends have watched") is constant-time, regardless of the total database size.
  * **Intuitive Modeling:** The data model maps directly to your domain entities (Users, Actors, Genres), making the schema easier to understand and evolve.
  * **Real-time Recommendations:** Graph algorithms can easily power recommendation engines by analyzing patterns like "users who watched this also watched that" in real-time.

-----

## How to run (terminal):

*(Requirement: docker and docker compose installed. UV also, recommended)*

#### Resolve and install pyproject.toml dependencies

```bash
uv sync
```

#### Running docker to up db

```bash
docker compose up -d
```

#### Activating virtual environment

  - macOS / Linux: `source .venv/bin/activate`
  - Windows (PowerShell/Win Terminal): `.venv\Scripts\activate`

#### Running queries

```bash
python3 code/python/db_queries.py
```

-----

## How to visualize your graphs

Once your Docker container is running, Neo4j provides a powerful browser-based interface to explore your data visually.

1.  Open your web browser and navigate to: **[http://localhost:7474](https://www.google.com/search?q=http://localhost:7474)**
2.  Log in with the following credentials:
      * **Username:** `neo4j`
      * **Password:** `senha123`
3.  Once connected, you can run Cypher queries directly in the browser console (e.g., `MATCH (n) RETURN n LIMIT 25`) to see your nodes and relationships rendered as an interactive graph.