from flask import Flask 
from app import create_app

app = create_app("dev")

@app.route('/')
def home():
   return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)