from neo4j import Transaction

def create_movie(tx: Transaction, title: str, release_year: int, duration_minutes: int):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes})",
        title=title, release_year=release_year, duration_minutes=duration_minutes
    )

def create_movie_with_rating(tx: Transaction, title: str, release_year: int, duration_minutes: int, age_rating: str, mpaa_rating: str):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, age_rating: $age_rating, mpaa_rating: $mpaa_rating})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, age_rating=age_rating, mpaa_rating=mpaa_rating
    )

def create_movie_with_genres(tx: Transaction, title: str, release_year: int, duration_minutes: int, genres: list, imdb_score: float):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, genres: $genres, imdb_score: $imdb_score})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, genres=genres, imdb_score=imdb_score
    )

def create_movie_with_description(tx: Transaction, title: str, release_year: int, duration_minutes: int, synopsis: str, language: str):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, synopsis: $synopsis, language: $language})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, synopsis=synopsis, language=language
    )

def create_movie_with_budget(tx: Transaction, title: str, release_year: int, duration_minutes: int, budget_usd: int, box_office_usd: int):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, budget_usd: $budget_usd, box_office_usd: $box_office_usd})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, budget_usd=budget_usd, box_office_usd=box_office_usd
    )

def create_movie_with_streaming_info(tx: Transaction, title: str, release_year: int, duration_minutes: int, available_4k: bool, subtitled: bool):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, available_4k: $available_4k, subtitled: $subtitled})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, available_4k=available_4k, subtitled=subtitled
    )

def create_movie_with_director_info(tx: Transaction, title: str, release_year: int, duration_minutes: int, director_name: str, writer: str):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, director_name: $director_name, writer: $writer})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, director_name=director_name, writer=writer
    )

def create_movie_with_awards(tx: Transaction, title: str, release_year: int, duration_minutes: int, num_oscars: int, num_nominations: int):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, num_oscars: $num_oscars, num_nominations: $num_nominations})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, num_oscars=num_oscars, num_nominations=num_nominations
    )

def create_movie_with_cast_count(tx: Transaction, title: str, release_year: int, duration_minutes: int, num_cast_members: int, production_company: str):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, num_cast_members: $num_cast_members, production_company: $production_company})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, num_cast_members=num_cast_members, production_company=production_company
    )

def create_movie_with_tracking(tx: Transaction, title: str, release_year: int, duration_minutes: int, view_count: int, popularity_score: float):
    tx.run(
        "CREATE (m:Movie {title: $title, release_year: $release_year, duration_minutes: $duration_minutes, view_count: $view_count, popularity_score: $popularity_score})",
        title=title, release_year=release_year, duration_minutes=duration_minutes, view_count=view_count, popularity_score=popularity_score
    )
