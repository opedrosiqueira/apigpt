import openai
import os
from dotenv import load_dotenv
import pprint
import json

# Load variables from the .env file into the environment
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt="draw a flowchart diagram from the following algorithm: 1. go to the first room; 2. While you haven't changed the light bulb in the four rooms, do 2.1. take a ladder; 2.2. position the ladder under the lamp in the current room; 2.3. fetch some spare bulbs; 2.4. climb the ladder; 2.5. remove the incandescent lamp; 2.6. put a led lamp; 2.7. while the lamp does not light, do 2.7.1. remove the burnt out bulb; 2.7.2. put in another spare lamp; 2.8. go to the next room;",
    n=1,
    size="512x512"
)
image_url = response['data'][0]['url']

pprint.pprint(response)
