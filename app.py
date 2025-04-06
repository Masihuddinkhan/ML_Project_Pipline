from flask import Flask
from src.logger import logging
from src.exception import CustmeException
import os, sys

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def index():
    try:
        raise Exception("we are testing custme file")
    except Exception as e:
        abc = CustmeException(e, sys)
        logging.info(abc.error_message)
        return  "Welcome to the home page!"


if __name__ == "__main__":
    app.run(debug=True)