from flask import Blueprint, render_template , jsonify
from ..extensions import getDb

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():

    return render_template('home.html')

@home_bp.route('/data')
def get_data():
    db = getDb()
    if db is None:
        return jsonify({"error": "Database not initialized."}), 500

    try:
        cursor = db.webhooks.find().sort("timestamp",-1)
        data = list(cursor)
        
        for item in data:
            item['_id'] = str(item['_id'])
            
        return jsonify(data)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return jsonify({"error": str(e)}), 500


@home_bp.route('/clear_db', methods=['DELETE'])
def clear_database():
    db = getDb()
    try:
        db['webhooks'].delete_many({})  
        return jsonify({"message": "Database cleared successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
