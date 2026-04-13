from neo4j import Transaction

def watched_movie(tx: Transaction, user_name: str, movie_title: str, rating: float = None, watch_date: str = None):
    params = {"user_name": user_name, "movie_title": movie_title, "rating": rating, "watch_date": watch_date}
    if rating and watch_date:
        tx.run(
            "MATCH (u:User {name: $user_name}), (m:Movie {title: $movie_title}) "
            "CREATE (u)-[r:WATCHED {rating: $rating, watch_date: $watch_date}]->(m)",
            **params
        )
    elif rating:
        tx.run(
            "MATCH (u:User {name: $user_name}), (m:Movie {title: $movie_title}) "
            "CREATE (u)-[r:WATCHED {rating: $rating}]->(m)",
            user_name=user_name, movie_title=movie_title, rating=rating
        )
    elif watch_date:
        tx.run(
            "MATCH (u:User {name: $user_name}), (m:Movie {title: $movie_title}) "
            "CREATE (u)-[r:WATCHED {watch_date: $watch_date}]->(m)",
            user_name=user_name, movie_title=movie_title, watch_date=watch_date
        )
    else:
        tx.run(
            "MATCH (u:User {name: $user_name}), (m:Movie {title: $movie_title}) "
            "CREATE (u)-[r:WATCHED]->(m)",
            user_name=user_name, movie_title=movie_title
        )

def watched_series(tx: Transaction, user_name: str, series_title: str, rating: float = None, watch_date: str = None):
    params = {"user_name": user_name, "series_title": series_title, "rating": rating, "watch_date": watch_date}
    if rating and watch_date:
        tx.run(
            "MATCH (u:User {name: $user_name}), (s:Series {title: $series_title}) "
            "CREATE (u)-[r:WATCHED {rating: $rating, watch_date: $watch_date}]->(s)",
            **params
        )
    elif rating:
        tx.run(
            "MATCH (u:User {name: $user_name}), (s:Series {title: $series_title}) "
            "CREATE (u)-[r:WATCHED {rating: $rating}]->(s)",
            user_name=user_name, series_title=series_title, rating=rating
        )
    elif watch_date:
        tx.run(
            "MATCH (u:User {name: $user_name}), (s:Series {title: $series_title}) "
            "CREATE (u)-[r:WATCHED {watch_date: $watch_date}]->(s)",
            user_name=user_name, series_title=series_title, watch_date=watch_date
        )
    else:
        tx.run(
            "MATCH (u:User {name: $user_name}), (s:Series {title: $series_title}) "
            "CREATE (u)-[r:WATCHED]->(s)",
            user_name=user_name, series_title=series_title
        )

def acted_in_movie(tx: Transaction, actor_name: str, movie_title: str, role: str = None):
    params = {"actor_name": actor_name, "movie_title": movie_title, "role": role}
    if role:
        tx.run(
            "MATCH (a:Actor {name: $actor_name}), (m:Movie {title: $movie_title}) "
            "CREATE (a)-[r:ACTED_IN {role: $role}]->(m)",
            **params
        )
    else:
        tx.run(
            "MATCH (a:Actor {name: $actor_name}), (m:Movie {title: $movie_title}) "
            "CREATE (a)-[r:ACTED_IN]->(m)",
            actor_name=actor_name, movie_title=movie_title
        )

def acted_in_series(tx: Transaction, actor_name: str, series_title: str, role: str = None, seasons: list = None):
    params = {"actor_name": actor_name, "series_title": series_title, "role": role, "seasons": seasons}
    if role and seasons:
        tx.run(
            "MATCH (a:Actor {name: $actor_name}), (s:Series {title: $series_title}) "
            "CREATE (a)-[r:ACTED_IN {role: $role, seasons: $seasons}]->(s)",
            **params
        )
    elif role:
        tx.run(
            "MATCH (a:Actor {name: $actor_name}), (s:Series {title: $series_title}) "
            "CREATE (a)-[r:ACTED_IN {role: $role}]->(s)",
            actor_name=actor_name, series_title=series_title, role=role
        )
    else:
        tx.run(
            "MATCH (a:Actor {name: $actor_name}), (s:Series {title: $series_title}) "
            "CREATE (a)-[r:ACTED_IN]->(s)",
            actor_name=actor_name, series_title=series_title
        )

def directed_movie(tx: Transaction, director_name: str, movie_title: str):
    tx.run(
        "MATCH (d:Director {name: $director_name}), (m:Movie {title: $movie_title}) "
        "CREATE (d)-[r:DIRECTED]->(m)",
        director_name=director_name, movie_title=movie_title
    )

def directed_series(tx: Transaction, director_name: str, series_title: str):
    tx.run(
        "MATCH (d:Director {name: $director_name}), (s:Series {title: $series_title}) "
        "CREATE (d)-[r:DIRECTED]->(s)",
        director_name=director_name, series_title=series_title
    )

def movie_in_genre(tx: Transaction, movie_title: str, genre_name: str):
    tx.run(
        "MATCH (m:Movie {title: $movie_title}), (g:Genre {name: $genre_name}) "
        "CREATE (m)-[r:IN_GENRE]->(g)",
        movie_title=movie_title, genre_name=genre_name
    )

def series_in_genre(tx: Transaction, series_title: str, genre_name: str):
    tx.run(
        "MATCH (s:Series {title: $series_title}), (g:Genre {name: $genre_name}) "
        "CREATE (s)-[r:IN_GENRE]->(g)",
        series_title=series_title, genre_name=genre_name
    )
