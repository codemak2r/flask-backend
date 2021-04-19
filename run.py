from flask import Flask, jsonify
from app import create_app
from common.response import ResponseObject

app = create_app("dev")

@app.route('/')
def home():
   res = ResponseObject(1,"success")
   res.update(data = {"test":"object"})

   return jsonify(res.body)

if __name__ == "__main__":
    app.run(debug=True)