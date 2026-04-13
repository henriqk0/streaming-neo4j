from neo4j import GraphDatabase

from entities.user import (
    create_user,
    create_user_with_country,
    create_user_with_profile,
    create_premium_user,
    create_user_with_preferences,
    create_family_user,
    create_student_user,
    create_user_with_watch_history_limit,
    create_user_with_device_info,
    create_user_with_billing,
)
from entities.movie import (
    create_movie,
    create_movie_with_rating,
    create_movie_with_genres,
    create_movie_with_description,
    create_movie_with_budget,
    create_movie_with_streaming_info,
    create_movie_with_director_info,
    create_movie_with_awards,
    create_movie_with_cast_count,
    create_movie_with_tracking,
)
from entities.series import (
    create_series,
    create_series_with_episode_info,
    create_series_with_status,
    create_series_with_genres,
    create_series_with_network,
    create_series_with_awards,
    create_series_with_tracking,
    create_series_with_age_rating,
    create_series_with_production,
    create_series_complete,
)
from entities.actor import (
    create_actor,
    create_actor_with_nationality,
    create_actor_with_awards,
    create_actor_with_biography,
    create_actor_with_career_stats,
    create_actor_with_social,
    create_actor_with_height,
    create_actor_with_specialization,
    create_actor_with_family,
    create_actor_with_representation,
)
from entities.director import (
    create_director,
    create_director_with_nationality,
    create_director_with_awards,
    create_director_with_filmography,
    create_director_with_collaborators,
    create_director_with_biography,
    create_director_with_tracking,
    create_director_with_style,
    create_director_with_influence,
    create_director_with_representation,
)
from entities.genre import (
    create_genre,
    create_genre_with_stats,
    create_genre_with_target_demographic,
)
from entities.relationships import (
    watched_movie,
    watched_series,
    acted_in_movie,
    acted_in_series,
    directed_movie,
    directed_series,
    movie_in_genre,
    series_in_genre,
)

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "senha123"

def main():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

    with driver.session() as session:
        # User functions
        session.execute_write(create_user, "John", "john@example.com", "basic")
        session.execute_write(create_user_with_country, "Jane", "jane@example.com", "USA", "premium")
        session.execute_write(create_user_with_profile, "Bob", "bob@example.com", 1990, "male", "Canada")
        session.execute_write(create_premium_user, "Alice", "alice@example.com", "UK", "2025-12-31")
        session.execute_write(create_user_with_preferences, "Charlie", "charlie@example.com", "en", True, False)
        session.execute_write(create_family_user, "David", "david@example.com", 4, True)
        session.execute_write(create_student_user, "Eve", "eve@example.com", "MIT", "S12345")
        session.execute_write(create_user_with_watch_history_limit, "Frank", "frank@example.com", 500)
        session.execute_write(create_user_with_device_info, "Grace", "grace@example.com", "Smart TV", 4)
        session.execute_write(create_user_with_billing, "Henry", "henry@example.com", "monthly", "credit_card")

        # Movie functions
        session.execute_write(create_movie, "The Matrix", 1999, 136)
        session.execute_write(create_movie_with_rating, "Inception", 2010, 148, "PG-13", "PG-13")
        session.execute_write(create_movie_with_genres, "Interstellar", 2014, 169, ["Sci-Fi", "Drama"], 8.7)
        session.execute_write(create_movie_with_description, "Titanic", 1997, 194, "A romance on the RMS Titanic.", "English")
        session.execute_write(create_movie_with_budget, "Avatar", 2009, 162, 237000000, 2847000000)
        session.execute_write(create_movie_with_streaming_info, "The Avengers", 2012, 143, True, True)
        session.execute_write(create_movie_with_director_info, "Pulp Fiction", 1994, 154, "Quentin Tarantino", "Quentin Tarantino")
        session.execute_write(create_movie_with_awards, "Parasite", 2019, 132, 4, 6)
        session.execute_write(create_movie_with_cast_count, "Avengers: Endgame", 2019, 181, 32, "Marvel Studios")
        session.execute_write(create_movie_with_tracking, "The Lion King", 2019, 118, 1500000, 9.2)

        # Series functions
        session.execute_write(create_series, "Breaking Bad", 2008, 5)
        session.execute_write(create_series_with_episode_info, "Game of Thrones", 2011, 8, 10, 60)
        session.execute_write(create_series_with_status, "Friends", 1994, 10, "ended", 2004)
        session.execute_write(create_series_with_genres, "Stranger Things", 2016, 4, ["Horror", "Sci-Fi", "Drama"], 8.7)
        session.execute_write(create_series_with_network, "The Office", 2005, 9, "NBC", True)
        session.execute_write(create_series_with_awards, "The Crown", 2016, 6, 21, False)
        session.execute_write(create_series_with_tracking, "Squid Game", 2021, 2, 5000000, 9.8)
        session.execute_write(create_series_with_age_rating, "Hannibal", 2013, 3, "TV-MA", "Graphic violence")
        session.execute_write(create_series_with_production, "Lost", 2004, 6, "Bad Robot Studios", ["Hawaii", "Los Angeles"])
        session.execute_write(create_series_complete, "The Mandalorian", 2019, 3, "Disney+", "ongoing", ["Sci-Fi", "Action"], 8.7)

        # Actor functions
        session.execute_write(create_actor, "Morgan Freeman", 1937)
        session.execute_write(create_actor_with_nationality, "Scarlett Johansson", 1984, "American", "White")
        session.execute_write(create_actor_with_awards, "Leonardo DiCaprio", 1974, 1, 6)
        session.execute_write(create_actor_with_biography, "Meryl Streep", 1949, "New Jersey", "Award-winning actress")
        session.execute_write(create_actor_with_career_stats, "Samuel L. Jackson", 1948, 150, 5000000000)
        session.execute_write(create_actor_with_social, "Dwayne Johnson", 1972, 350000000, "@TheRock")
        session.execute_write(create_actor_with_height, "Tom Cruise", 1962, 170.0, "Blue")
        session.execute_write(create_actor_with_specialization, "Mark Hamill", 1951, "Sci-Fi", False)
        session.execute_write(create_actor_with_family, "Jennifer Lawrence", 1990, "Cook", 0)
        session.execute_write(create_actor_with_representation, "Chris Hemsworth", 1983, "CAA", "Agent Smith")

        # Director functions
        session.execute_write(create_director, "Christopher Nolan", 1970)
        session.execute_write(create_director_with_nationality, "Quentin Tarantino", 1963, "American", "Los Angeles")
        session.execute_write(create_director_with_awards, "Steven Spielberg", 1946, 2, 19)
        session.execute_write(create_director_with_filmography, "Martin Scorsese", 1942, 50, "Crime")
        session.execute_write(create_director_with_collaborators, "Wes Anderson", 1969, "Wes Anderson", "Alexandre Desplat")
        session.execute_write(create_director_with_biography, "Alfred Hitchcock", 1899, "London", "London Film School")
        session.execute_write(create_director_with_tracking, "James Cameron", 1954, 5000000000, 8.5)
        session.execute_write(create_director_with_style, "Guillermo del Toro", 1964, ["Fantasy", "Horror"], "Visual")
        session.execute_write(create_director_with_influence, "Ridley Scott", 1937, "David Lean", ["BAFTA", "Golden Globe"])
        session.execute_write(create_director_with_representation, "Denis Villeneuve", 1967, "WME", "Active")

        # Genre functions
        session.execute_write(create_genre, "Action", "High-octane fight sequences and stunts")
        session.execute_write(create_genre_with_stats, "Drama", "Character-driven emotional stories", 1, 8.2)
        session.execute_write(create_genre_with_target_demographic, "Animation", "Animated content for all ages", 5, "All")

        # Relationship: WATCHED (User -> Movie/Series with rating)
        session.execute_write(watched_movie, "John", "The Matrix", 4.5, "2024-01-15")
        session.execute_write(watched_movie, "Jane", "Inception", 5.0, "2024-02-20")
        session.execute_write(watched_movie, "Bob", "Interstellar", 4.8, "2024-03-10")
        session.execute_write(watched_movie, "Alice", "Avatar", 4.2, "2024-01-25")
        session.execute_write(watched_movie, "Charlie", "The Avengers", 3.9, "2024-04-05")
        session.execute_write(watched_movie, "David", "Parasite", 4.7, "2024-02-14")
        session.execute_write(watched_movie, "Eve", "Pulp Fiction", 4.6, "2024-03-22")
        session.execute_write(watched_movie, "Frank", "Titanic", 4.3, "2024-01-30")
        session.execute_write(watched_movie, "Grace", "Avengers: Endgame", 4.9, "2024-05-01")
        session.execute_write(watched_movie, "Henry", "The Lion King", 4.4, "2024-02-28")

        # Relationship: WATCHED (User -> Series)
        session.execute_write(watched_series, "John", "Breaking Bad", 5.0, "2024-01-20")
        session.execute_write(watched_series, "Jane", "Game of Thrones", 4.8, "2024-02-15")
        session.execute_write(watched_series, "Bob", "Stranger Things", 4.7, "2024-03-05")
        session.execute_write(watched_series, "Alice", "The Office", 4.2, "2024-01-10")
        session.execute_write(watched_series, "Charlie", "The Crown", 4.6, "2024-04-12")
        session.execute_write(watched_series, "David", "Squid Game", 4.9, "2024-02-25")
        session.execute_write(watched_series, "Eve", "The Mandalorian", 4.5, "2024-03-15")
        session.execute_write(watched_series, "Frank", "Friends", 4.1, "2024-01-05")
        session.execute_write(watched_series, "Grace", "Hannibal", 4.4, "2024-04-20")
        session.execute_write(watched_series, "Henry", "Lost", 4.3, "2024-02-10")

        # Relationship: ACTED_IN (Actor -> Movie)
        session.execute_write(acted_in_movie, "Morgan Freeman", "The Matrix", "Morpheus")
        session.execute_write(acted_in_movie, "Leonardo DiCaprio", "Inception", "Dom Cobb")
        session.execute_write(acted_in_movie, "Leonardo DiCaprio", "Titanic", "Jack Dawson")
        session.execute_write(acted_in_movie, "Samuel L. Jackson", "Pulp Fiction", "Jules Winnfield")
        session.execute_write(acted_in_movie, "Scarlett Johansson", "The Avengers", "Black Widow")
        session.execute_write(acted_in_movie, "Chris Hemsworth", "Avengers: Endgame", "Thor")
        session.execute_write(acted_in_movie, "Tom Cruise", "The Matrix", "Neo")
        session.execute_write(acted_in_movie, "Jennifer Lawrence", "The Hunger Games", "Katniss Everdeen")
        session.execute_write(acted_in_movie, "Dwayne Johnson", "The Avengers", "Mjolnir")
        session.execute_write(acted_in_movie, "Meryl Streep", "The Iron Lady", "Margaret Thatcher")

        # Relationship: ACTED_IN (Actor -> Series)
        session.execute_write(acted_in_series, "Mark Hamill", "The Mandalorian", "Luke Skywalker", [3])
        session.execute_write(acted_in_series, "Samuel L. Jackson", "The Crown", "Narrator", [1])
        session.execute_write(acted_in_series, "Meryl Streep", "The Office", "Guest Star", [7])
        session.execute_write(acted_in_series, "Dwayne Johnson", "Friends", "Himself", [8])
        session.execute_write(acted_in_series, "Morgan Freeman", "Breaking Bad", "Uncredited", [5])
        session.execute_write(acted_in_series, "Chris Hemsworth", "The Office", "Guest Speaker", [9])
        session.execute_write(acted_in_series, "Tom Cruise", "Lost", "Kevin", [6])
        session.execute_write(acted_in_series, "Leonardo DiCaprio", "The Crown", "Historical Figure", [2])
        session.execute_write(acted_in_series, "Scarlett Johansson", "Game of Thrones", "Lady", [1])
        session.execute_write(acted_in_series, "Jennifer Lawrence", "Squid Game", "Player 456", [1])

        # Relationship: DIRECTED (Director -> Movie)
        session.execute_write(directed_movie, "Christopher Nolan", "Inception")
        session.execute_write(directed_movie, "Christopher Nolan", "Interstellar")
        session.execute_write(directed_movie, "James Cameron", "Avatar")
        session.execute_write(directed_movie, "James Cameron", "Titanic")
        session.execute_write(directed_movie, "Quentin Tarantino", "Pulp Fiction")
        session.execute_write(directed_movie, "Bong Joon-ho", "Parasite")
        session.execute_write(directed_movie, "Anthony Russo", "Avengers: Endgame")
        session.execute_write(directed_movie, "Jon Favreau", "The Lion King")
        session.execute_write(directed_movie, "The Wachowskis", "The Matrix")
        session.execute_write(directed_movie, "Joss Whedon", "The Avengers")

        # Relationship: DIRECTED (Director -> Series)
        session.execute_write(directed_series, "Vince Gilligan", "Breaking Bad")
        session.execute_write(directed_series, "David Benioff", "Game of Thrones")
        session.execute_write(directed_series, "Kevin Bright", "Friends")
        session.execute_write(directed_series, "The Duffer Brothers", "Stranger Things")
        session.execute_write(directed_series, "Greg Daniels", "The Office")
        session.execute_write(directed_series, "Peter Morgan", "The Crown")
        session.execute_write(directed_series, "Hwang Dong-hyuk", "Squid Game")
        session.execute_write(directed_series, "Bryan Fuller", "Hannibal")
        session.execute_write(directed_series, "Jon Favreau", "The Mandalorian")
        session.execute_write(directed_series, "J.J. Abrams", "Lost")

        # Relationship: IN_GENRE (Movie -> Genre)
        session.execute_write(movie_in_genre, "The Matrix", "Action")
        session.execute_write(movie_in_genre, "Inception", "Sci-Fi")
        session.execute_write(movie_in_genre, "Interstellar", "Sci-Fi")
        session.execute_write(movie_in_genre, "Titanic", "Drama")
        session.execute_write(movie_in_genre, "Avatar", "Sci-Fi")
        session.execute_write(movie_in_genre, "The Avengers", "Action")
        session.execute_write(movie_in_genre, "Pulp Fiction", "Drama")
        session.execute_write(movie_in_genre, "Parasite", "Drama")
        session.execute_write(movie_in_genre, "The Lion King", "Animation")
        session.execute_write(movie_in_genre, "Avatar", "Action")

        # Relationship: IN_GENRE (Series -> Genre)
        session.execute_write(series_in_genre, "Breaking Bad", "Drama")
        session.execute_write(series_in_genre, "Game of Thrones", "Drama")
        session.execute_write(series_in_genre, "Friends", "Comedy")
        session.execute_write(series_in_genre, "Stranger Things", "Horror")
        session.execute_write(series_in_genre, "The Office", "Comedy")
        session.execute_write(series_in_genre, "The Crown", "Drama")
        session.execute_write(series_in_genre, "Squid Game", "Drama")
        session.execute_write(series_in_genre, "Hannibal", "Horror")
        session.execute_write(series_in_genre, "The Mandalorian", "Sci-Fi")
        session.execute_write(series_in_genre, "Lost", "Drama")

    driver.close()

if __name__ == "__main__":
    main()
