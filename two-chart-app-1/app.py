from flask import Flask
from routes import simple_page
print(simple_page)
app = Flask(__name__)
app.register_blueprint(simple_page)
