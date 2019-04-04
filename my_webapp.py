from flask import Flask, render_template, request
import logging
import requests
import json

flask_app = Flask(__name__)

#CONFIGURING LOGGING
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

fh = logging.FileHandler('application_logs.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)



@flask_app.route('/')
def homepage():
    return render_template("index.html")


@flask_app.route('/<dog_breed>')
def show_dog(dog_breed):
	response = requests.get("https://dog.ceo/api/breed/{}/images/random".format(dog_breed))
	image_url = response.json()["message"]
	return render_template("displaydog.html", image_url=image_url)




logger.info('STARTING APP, TRY IT OUT!!!')

if __name__ == '__main__':
    flask_app.run(debug=True, use_reloader=True)

