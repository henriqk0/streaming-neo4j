from neo4j import Transaction

def create_director(tx: Transaction, name: str, birth_year: int):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year})",
        name=name, birth_year=birth_year
    )

def create_director_with_nationality(tx: Transaction, name: str, birth_year: int, nationality: str, residence: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, nationality: $nationality, residence: $residence})",
        name=name, birth_year=birth_year, nationality=nationality, residence=residence
    )

def create_director_with_awards(tx: Transaction, name: str, birth_year: int, num_oscar_wins: int, num_oscar_nominations: int):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, num_oscar_wins: $num_oscar_wins, num_oscar_nominations: $num_oscar_nominations})",
        name=name, birth_year=birth_year, num_oscar_wins=num_oscar_wins, num_oscar_nominations=num_oscar_nominations
    )

def create_director_with_filmography(tx: Transaction, name: str, birth_year: int, num_films_directed: int, primary_genre: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, num_films_directed: $num_films_directed, primary_genre: $primary_genre})",
        name=name, birth_year=birth_year, num_films_directed=num_films_directed, primary_genre=primary_genre
    )

def create_director_with_collaborators(tx: Transaction, name: str, birth_year: int, frequent_writer: str, frequent_composer: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, frequent_writer: $frequent_writer, frequent_composer: $frequent_composer})",
        name=name, birth_year=birth_year, frequent_writer=frequent_writer, frequent_composer=frequent_composer
    )

def create_director_with_biography(tx: Transaction, name: str, birth_year: int, birthplace: str, education: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, birthplace: $birthplace, education: $education})",
        name=name, birth_year=birth_year, birthplace=birthplace, education=education
    )

def create_director_with_tracking(tx: Transaction, name: str, birth_year: int, total_box_office: int, avg_critics_score: float):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, total_box_office: $total_box_office, avg_critics_score: $avg_critics_score})",
        name=name, birth_year=birth_year, total_box_office=total_box_office, avg_critics_score=avg_critics_score
    )

def create_director_with_style(tx: Transaction, name: str, birth_year: int, signature_themes: list, cinematographic_style: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, signature_themes: $signature_themes, cinematographic_style: $cinematographic_style})",
        name=name, birth_year=birth_year, signature_themes=signature_themes, cinematographic_style=cinematographic_style
    )

def create_director_with_influence(tx: Transaction, name: str, birth_year: int, influenced_by: str, awards: list):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, influenced_by: $influenced_by, awards: $awards})",
        name=name, birth_year=birth_year, influenced_by=influenced_by, awards=awards
    )

def create_director_with_representation(tx: Transaction, name: str, birth_year: int, agency: str, representation_status: str):
    tx.run(
        "CREATE (d:Director {name: $name, birth_year: $birth_year, agency: $agency, representation_status: $representation_status})",
        name=name, birth_year=birth_year, agency=agency, representation_status=representation_status
    )
