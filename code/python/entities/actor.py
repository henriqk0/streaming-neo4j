from neo4j import Transaction

def create_actor(tx: Transaction, name: str, birth_year: int):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year})",
        name=name, birth_year=birth_year
    )

def create_actor_with_nationality(tx: Transaction, name: str, birth_year: int, nationality: str, ethnicity: str):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, nationality: $nationality, ethnicity: $ethnicity})",
        name=name, birth_year=birth_year, nationality=nationality, ethnicity=ethnicity
    )

def create_actor_with_awards(tx: Transaction, name: str, birth_year: int, num_oscar_wins: int, num_oscar_nominations: int):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, num_oscar_wins: $num_oscar_wins, num_oscar_nominations: $num_oscar_nominations})",
        name=name, birth_year=birth_year, num_oscar_wins=num_oscar_wins, num_oscar_nominations=num_oscar_nominations
    )

def create_actor_with_biography(tx: Transaction, name: str, birth_year: int, birthplace: str, biography: str):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, birthplace: $birthplace, biography: $biography})",
        name=name, birth_year=birth_year, birthplace=birthplace, biography=biography
    )

def create_actor_with_career_stats(tx: Transaction, name: str, birth_year: int, num_films: int, total_box_office: int):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, num_films: $num_films, total_box_office: $total_box_office})",
        name=name, birth_year=birth_year, num_films=num_films, total_box_office=total_box_office
    )

def create_actor_with_social(tx: Transaction, name: str, birth_year: int, instagram_followers: int, twitter_handle: str):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, instagram_followers: $instagram_followers, twitter_handle: $twitter_handle})",
        name=name, birth_year=birth_year, instagram_followers=instagram_followers, twitter_handle=twitter_handle
    )

def create_actor_with_height(tx: Transaction, name: str, birth_year: int, height_cm: float, eye_color: str):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, height_cm: $height_cm, eye_color: $eye_color})",
        name=name, birth_year=birth_year, height_cm=height_cm, eye_color=eye_color
    )

def create_actor_with_specialization(tx: Transaction, name: str, birth_year: int, primary_genre: str, is_voice_actor: bool):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, primary_genre: $primary_genre, is_voice_actor: $is_voice_actor})",
        name=name, birth_year=birth_year, primary_genre=primary_genre, is_voice_actor=is_voice_actor
    )

def create_actor_with_family(tx: Transaction, name: str, birth_year: int, spouse: str = None, num_children: int = 0):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, spouse: $spouse, num_children: $num_children})",
        name=name, birth_year=birth_year, spouse=spouse, num_children=num_children
    )

def create_actor_with_representation(tx: Transaction, name: str, birth_year: int, agency: str, agent_name: str):
    tx.run(
        "CREATE (a:Actor {name: $name, birth_year: $birth_year, agency: $agency, agent_name: $agent_name})",
        name=name, birth_year=birth_year, agency=agency, agent_name=agent_name
    )
