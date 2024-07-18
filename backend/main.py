from instagrapi import Client

def login_instagram(username, password):
    """
    Logs into Instagram and returns an authenticated Client instance.
    """
    cl = Client()
    cl.login(username, password)
    return cl

def fetch_business_profiles(cl, category, country):
    """
    Fetches business profiles based on a category and country.
    """
    # Search for the category hashtag
    hashtag = cl.hashtag_info(category)
    posts = cl.hashtag_medias_recent(hashtag.name, amount=50)  # Fetch recent 50 posts

    # Filter posts by country (this assumes location data is available in posts)
    profiles = []
    for post in posts:
        if post.location and country.lower() in post.location.name.lower():
            profiles.append(post.user.username)
    
    return profiles

if __name__ == "__main__":
    # Set your Instagram credentials
    username = ""
    password = ""
    category = "restaurant"  # Example category
    country = "USA"           # Example country

    # Step 1: Login to Instagram
    cl = login_instagram(username, password)
    print(f"Logged in as {username}")

    # Step 2: Fetch business profiles
    profiles = fetch_business_profiles(cl, category, country)
    print(f"Business profiles in {category} category from {country}:")
    for profile in profiles:
        print(profile)
