def recommend_products(profile, products):
    preferences = profile.get("preferences", [])
    recommendations = [
        product for product in products
        if product["category"] in preferences
    ]
    return recommendations
