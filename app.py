from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def hello():
    version = os.environ.get("APP_VERSION", "v1")
    return f"Hello from Flask on Docker! Version: {version}\n"
if _name_=="_main_":
    app.run(host="0.0.0.0", port=5000)
