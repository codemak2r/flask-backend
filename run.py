from flask import Flask, jsonify
from app import create_app
from common.response import ResponseObject
from common.route import route

app = create_app("dev")

@route(app,'/')
def home():
   res = ResponseObject(1,"success",{"name":"john.doe"})

   return res.body

if __name__ == "__main__":
    app.run(debug=True)