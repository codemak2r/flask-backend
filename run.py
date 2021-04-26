from flask import Flask, jsonify
from app import create_app
from common.response import ResponseObject
from common.core import route
from datetime import datetime
from decimal import Decimal

app = create_app("dev")

@route(app,'/')
def home():
   res = ResponseObject(1,"success",{"name":"john.doe"})
   now = datetime.now()
   date = datetime.now().date()
   num = Decimal(11.11)
   test_dict = dict(now=now, date=date, num=num)
   res.update(data = test_dict)
   return res.body

if __name__ == "__main__":
    app.run(debug=True)