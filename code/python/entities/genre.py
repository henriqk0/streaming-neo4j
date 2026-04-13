from neo4j import Transaction

def create_genre(tx: Transaction, name: str, description: str):
    tx.run(
        "CREATE (g:Genre {name: $name, description: $description})",
        name=name, description=description
    )

def create_genre_with_stats(tx: Transaction, name: str, description: str, popularity_rank: int, avg_content_rating: float):
    tx.run(
        "CREATE (g:Genre {name: $name, description: $description, popularity_rank: $popularity_rank, avg_content_rating: $avg_content_rating})",
        name=name, description=description, popularity_rank=popularity_rank, avg_content_rating=avg_content_rating
    )

def create_genre_with_target_demographic(tx: Transaction, name: str, description: str, target_age_min: int, target_gender: str):
    tx.run(
        "CREATE (g:Genre {name: $name, description: $description, target_age_min: $target_age_min, target_gender: $target_gender})",
        name=name, description=description, target_age_min=target_age_min, target_gender=target_gender
    )
