from flask import Flask, render_template
import json
import urllib.request

app = Flask(__name__)

APP_API_KEY = "HAzNETw6VUoq4BIZ0KikSObCBP0xe0gMSbbYaubP"
API_URL = "https://api.nasa.gov/planetary/apod?api_key=" + APP_API_KEY

with urllib.request.urlopen(API_URL) as response:
    responseData = response.read()

datastore = json.loads(responseData)


@app.route('/')
def mainRoute():
    return render_template('apod.jinja', datastore=datastore)

print("name:" + __name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
