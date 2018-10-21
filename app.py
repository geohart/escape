from flask import Flask, request, send_file
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import xml.etree.cElementTree as ET
import os

app = Flask(__name__)

@app.route('/')
def index():
	print(request.base_url)
	return 'Boo!'

@app.route("/answer", methods=['GET'])
def answer_call():
	"""Respond to incoming phone calls with a brief message."""
	# Start our TwiML response
	response = VoiceResponse()

	# Read a message aloud to the caller
	# response.say("Thank you for calling! Have a great day.", voice='alice')
	
	# Play sound
	#response.play('./sounds/scream.mp3', loop=10)
	
	resource_url = (request.base_url[0:-len(request.path)])
	
	return("<img src='" + resource_url + "/sounds/pumpkin.jpg'>")
	#return str(response)

@app.route("/call", methods=['GET'])
def place_call():
	"""Place a call to number passed in as parameter"""
	
	# get phone number from url
	target = request.args.get('number')
	
	# run basic check to see if a valid number was provided
	if target is None:
		# notify user of error
		return("Make sure you have appended a 10-digit phone number to the url (" + request.base_url + "?number=[YOUR 10 DIGIT NUMBER HERE]).")
	elif not (len(target) == 10 and str.isdigit(target)):
		# notify user of error
		return("Make sure you have appended a 10-digit phone number to the url (" + request.base_url + "?number=[YOUR 10 DIGIT NUMBER HERE]).")
	else:
		
		# get root url
		path = (request.base_url[0:-len(request.path)])
		print(path)
		
		"""# create xml file describing call
		root = ET.Element("Response")
		ET.SubElement(root, "Say", voice="Alice").text = "Be afraid!"
		ET.SubElement(root, "Play").text = path +"/static/scream.mp3"
		tree = ET.ElementTree(root)
		tree.write("static/call.xml")"""

		# proceed with call attempt
		account_sid = os.environ['twilio_sid']
		auth_token = os.environ['twilio_auth_token']
		client = Client(account_sid, auth_token)
		
		print(path + "/specification")
		
		call = client.calls.create(
			url=path + "/specification",
			to="+1" + target,
			from_="+16506956260"
		)
		
		return("success")
		
@app.route("/specification", methods=['GET','POST'])
def get_call_specification():

	return send_file("static/call.xml")
	

if __name__ == "__main__":
	app.run(debug=True)