from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
 return """
 <h1>Cloud Computing Laaaaaab - PaaS</h1>
 <p>This application is deployed using a Platform as a Service.</p>
 """
