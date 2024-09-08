from flask import Blueprint, json, request
from datetime import datetime
from ..Helper.jsonData import jsonDataParser 
from ..extensions import insert_data


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.content_type == "application/json" :
        
        data = request.json
        webhook_event = request.headers.get('X-GitHub-Event')
        
        res = insert_data(data=data ,webhook_event = webhook_event)
        print(res)

        return {}, 200
