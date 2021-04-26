
from common.core import route
from . import api_v1
from common.response import ResponseObject

@route(api_v1, "/test", methods=["GET"])
def hello():
   res = ResponseObject(1,"success",{"name":"john.doe"})
   print(res.body)
   return res.body