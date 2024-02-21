# Imports:
from flask import Flask
from flask_cors import CORS
import datetime

this_time = datetime.datetime.now()

# Initializing flask app:
app = Flask(__name__)
CORS(app)

# Route for seeing a data
@app.route('/data')
def get_time():
	# Returning an example api for displaying in reactjs:
	return {
		'Name':"AB", 
		"Age":"32",
		"Date":this_time, 
		"programming":"python-flask"
		}

	
# Running app
if __name__ == '__main__':
	app.run(debug=True)
