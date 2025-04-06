from flask import Flask, jsonify
from app.customer_agent import get_customer_profile_from_db
from app.product_agent import get_products_from_db
from app.recommendation_agent import generate_recommendations

app = Flask(__name__)

@app.route('/recommend/<int:customer_id>', methods=['GET'])
def recommend(customer_id):
    profile = get_customer_profile_from_db(customer_id)
    if not profile:
        return jsonify({"error": "Customer not found"}), 404

    products = get_products_from_db()
    recs = generate_recommendations(profile, products)
    return jsonify({"recommendations": recs})

if __name__ == '__main__':
    app.run(debug=True)
