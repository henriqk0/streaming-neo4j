from neo4j import Transaction

def create_user(tx: Transaction, name: str, email: str, subscription_tier: str = "basic"):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: $subscription_tier, created_at: datetime()})",
        name=name, email=email, subscription_tier=subscription_tier
    )

def create_user_with_country(tx: Transaction, name: str, email: str, country: str, subscription_tier: str = "basic"):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, country: $country, subscription_tier: $subscription_tier, created_at: datetime()})",
        name=name, email=email, country=country, subscription_tier=subscription_tier
    )

def create_user_with_profile(tx: Transaction, name: str, email: str, birth_year: int, gender: str, country: str):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, birth_year: $birth_year, gender: $gender, country: $country, subscription_tier: 'basic', created_at: datetime()})",
        name=name, email=email, birth_year=birth_year, gender=gender, country=country
    )

def create_premium_user(tx: Transaction, name: str, email: str, country: str, renewal_date: str):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'premium', country: $country, renewal_date: $renewal_date, created_at: datetime()})",
        name=name, email=email, country=country, renewal_date=renewal_date
    )

def create_user_with_preferences(tx: Transaction, name: str, email: str, preferred_language: str, subtitle_enabled: bool, autoplay_enabled: bool):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'basic', preferred_language: $preferred_language, subtitle_enabled: $subtitle_enabled, autoplay_enabled: $autoplay_enabled, created_at: datetime()})",
        name=name, email=email, preferred_language=preferred_language, subtitle_enabled=subtitle_enabled, autoplay_enabled=autoplay_enabled
    )

def create_family_user(tx: Transaction, name: str, email: str, num_profiles: int, parental_controls_enabled: bool):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'family', num_profiles: $num_profiles, parental_controls_enabled: $parental_controls_enabled, created_at: datetime()})",
        name=name, email=email, num_profiles=num_profiles, parental_controls_enabled=parental_controls_enabled
    )

def create_student_user(tx: Transaction, name: str, email: str, university: str, student_id: str):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'student', university: $university, student_id: $student_id, created_at: datetime()})",
        name=name, email=email, university=university, student_id=student_id
    )

def create_user_with_watch_history_limit(tx: Transaction, name: str, email: str, max_watch_history: int):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'basic', max_watch_history: $max_watch_history, created_at: datetime()})",
        name=name, email=email, max_watch_history=max_watch_history
    )

def create_user_with_device_info(tx: Transaction, name: str, email: str, primary_device: str, simultaneous_streams: int):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'premium', primary_device: $primary_device, simultaneous_streams: $simultaneous_streams, created_at: datetime()})",
        name=name, email=email, primary_device=primary_device, simultaneous_streams=simultaneous_streams
    )

def create_user_with_billing(tx: Transaction, name: str, email: str, billing_cycle: str, payment_method: str):
    tx.run(
        "CREATE (u:User {name: $name, email: $email, subscription_tier: 'basic', billing_cycle: $billing_cycle, payment_method: $payment_method, created_at: datetime()})",
        name=name, email=email, billing_cycle=billing_cycle, payment_method=payment_method
    )
