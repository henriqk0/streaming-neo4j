from neo4j import Transaction

def create_series(tx: Transaction, title: str, start_year: int, num_seasons: int):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons})",
        title=title, start_year=start_year, num_seasons=num_seasons
    )

def create_series_with_episode_info(tx: Transaction, title: str, start_year: int, num_seasons: int, episodes_per_season_avg: int, episode_duration_minutes: int):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, episodes_per_season_avg: $episodes_per_season_avg, episode_duration_minutes: $episode_duration_minutes})",
        title=title, start_year=start_year, num_seasons=num_seasons, episodes_per_season_avg=episodes_per_season_avg, episode_duration_minutes=episode_duration_minutes
    )

def create_series_with_status(tx: Transaction, title: str, start_year: int, num_seasons: int, status: str, end_year: int = None):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, status: $status, end_year: $end_year})",
        title=title, start_year=start_year, num_seasons=num_seasons, status=status, end_year=end_year
    )

def create_series_with_genres(tx: Transaction, title: str, start_year: int, num_seasons: int, genres: list, imdb_score: float):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, genres: $genres, imdb_score: $imdb_score})",
        title=title, start_year=start_year, num_seasons=num_seasons, genres=genres, imdb_score=imdb_score
    )

def create_series_with_network(tx: Transaction, title: str, start_year: int, num_seasons: int, network: str, available_4k: bool):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, network: $network, available_4k: $available_4k})",
        title=title, start_year=start_year, num_seasons=num_seasons, network=network, available_4k=available_4k
    )

def create_series_with_awards(tx: Transaction, title: str, start_year: int, num_seasons: int, num_emmy_awards: int, is_cancelled: bool):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, num_emmy_awards: $num_emmy_awards, is_cancelled: $is_cancelled})",
        title=title, start_year=start_year, num_seasons=num_seasons, num_emmy_awards=num_emmy_awards, is_cancelled=is_cancelled
    )

def create_series_with_tracking(tx: Transaction, title: str, start_year: int, num_seasons: int, total_view_count: int, popularity_score: float):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, total_view_count: $total_view_count, popularity_score: $popularity_score})",
        title=title, start_year=start_year, num_seasons=num_seasons, total_view_count=total_view_count, popularity_score=popularity_score
    )

def create_series_with_age_rating(tx: Transaction, title: str, start_year: int, num_seasons: int, age_rating: str, content_warning: str = None):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, age_rating: $age_rating, content_warning: $content_warning})",
        title=title, start_year=start_year, num_seasons=num_seasons, age_rating=age_rating, content_warning=content_warning
    )

def create_series_with_production(tx: Transaction, title: str, start_year: int, num_seasons: int, production_studio: str, filming_locations: list):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, production_studio: $production_studio, filming_locations: $filming_locations})",
        title=title, start_year=start_year, num_seasons=num_seasons, production_studio=production_studio, filming_locations=filming_locations
    )

def create_series_complete(tx: Transaction, title: str, start_year: int, num_seasons: int, network: str, status: str, genres: list, imdb_score: float):
    tx.run(
        "CREATE (s:Series {title: $title, start_year: $start_year, num_seasons: $num_seasons, network: $network, status: $status, genres: $genres, imdb_score: $imdb_score})",
        title=title, start_year=start_year, num_seasons=num_seasons, network=network, status=status, genres=genres, imdb_score=imdb_score
    )
