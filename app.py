from flask import Flask, request, jsonify 
import json
from uuid import uuid4
from datetime import datetime
from flask_cors import CORS, cross_origin

# remember to download flask_cors

app = Flask(__name__)
CORS(app)

def load_db():
	with open("database.JSON", "r") as f:
		database = json.load(f)
	return database
	# Look up and find databsase.JSON
	# Save is as something or return it

def save_db(database):
	with open("database.JSON", "w") as f:
		json.dump(database, f, indent=4) 

# All diary entry requests
@app.route("/diaryentry",methods=["GET"])
@cross_origin()
def get_all_diary_entries():
	db = load_db()
	n_entries = len(db)
	response = {
		'message': 'You have wasted 5 minutes of your life journalling!',
		'entries': db,
		'count': n_entries
}

	return jsonify(response), 200
		# Need function to load all entire database
		# Need to make my database to be JSON
		# Need to return JSON to the user
		# Do I need to do anything else?


# One diary entry request
@app.route("/diaryentry/<entryid>",methods=["GET"])
@cross_origin()
def get_one_diary_entry(entryid):
	# Need to load entire database
	# Need to search database for entryid
	# Need to return entry associated with entryid (title, description, created at)
	# Return entry to user with success message
	# If ID doesn't exist let user know entry ID wasn't available

	db = load_db()

# Hamza code
	# data = db.get(entryid)
	# success_response = {
	# 	'message': 'Sucessfully found your entry id',
	# 	'date': data,
	# 	'entryid': entryid
	# }

	# if data is None:
	# 	return jsonify({'message':'Couldnt find your entryid'}), 404

	# return jsonify(success_response), 200
			
# our code
	if entryid in db: 
		entry = db.get(entryid)

		response = {
			'message':'Here is your diary entry',
			'entries': entry
		}

		return jsonify(response), 200 

	else:
		return jsonify({'message': f'Could not find your entry with id {entryid}'}), 404



# post request 
@app.route("/diaryentry/",methods=["POST"])
@cross_origin()
def create_diary_entry(): 

#save the theme from request.data as a variable 
# response message should be if, and else statements
# each if statement should store the conditional Jsonify response 
# top bit is theme declaration into variables then below is response definition

	new_entry = json.loads(request.data)

	db  = load_db()
	unique_id = str(uuid4())
	db[unique_id] = new_entry

	gratitude_theme = new_entry["description"]
	
	db[unique_id]["createdat"] = str(datetime.now())
	
	save_db(db)
	# saving over the database with the new entry included


	if gratitude_theme == "Myself":
		response = {
		'message': 'What have you got to be grateful for?',
		'data': new_entry,
		'unique_id': unique_id
		}

	elif gratitude_theme =="Friends":
		response = {
		'message': 'Are you sure they are grateful for you with all the time you are spending on this app?',
		'data': new_entry,
		'unique_id': unique_id
		}

	elif gratitude_theme == "Family":
		response = {
		'message': 'You could have called your mum with the time you took to journal',
		'data': new_entry,
		'unique_id': unique_id
		}
	
	else:
		response = {
		'message': 'You are sacked. And your suspicions are right, we do have access to your whatsapps',
		'data': new_entry,
		'unique_id': unique_id
		}

	# response = {
	# 	'message': 'New entry created',
	# 	'data': new_entry,
	# 	'unique_id': unique_id
	# }

	return jsonify(response), 201

	# Get the data from the post request
	# Save the data into a variable
	# Load the database
	# Give the new entry an ID
	# Add new entry to database
	# Give the entry a new timestamp
	# Return the new entry + success message to the user






