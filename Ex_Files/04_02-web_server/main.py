from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, world!"

app.run(debug=True)