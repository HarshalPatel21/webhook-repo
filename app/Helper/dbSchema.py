schema = {
  "$jsonSchema": {
    "bsonType": "object",
    "required": ["request_id", "author", "action", "from_branch", "to_branch", "timestamp"],
    "properties": {
      "request_id": {
        "bsonType": "int",
        "description": "must be a int and is required"
      },
      "author": {
        "bsonType": "string",
        "description": "must be a string and is required"
      },
      "action": {
        "bsonType": "string",
        "description": "must be a string and is required"
      },
      "from_branch": {
        "bsonType": "string",
        "description": "must be a string and is required"
      },
      "to_branch": {
        "bsonType": "string",
        "description": "must be a string and is required"
      },
      "timestamp": {
        "bsonType": "string",
        "description": "must be a string and is required"
      }
    }
  }
}
