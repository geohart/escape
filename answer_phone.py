from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    response = VoiceResponse()

    # Read a message aloud to the caller
    # response.say("Thank you for calling! Have a great day.", voice='alice')
	
	# Play sound
	response.play('./sounds/scream.mp3', loop=10)


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)