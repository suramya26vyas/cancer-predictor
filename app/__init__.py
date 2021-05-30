from .config.config import Config
from flask import Flask
from .controller import bp
from .utilities import LibraryUtilities

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(bp)


@app.route("/", methods=['GET'])
def ping():
    return "Application is up! Visit <a href='/api'>APIs</a> to see the list of APIs.\n " \
           "To see Web Scrapping, Visit <a href='/api_ws'>Web-Scrapping</a> \n"\
            "Facebook related operations, Visit <a href='/api_fb'>Facebook-Scrapping</a>"
