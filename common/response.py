class ResponseObject():
    def __init__(self, status=None, message=None, data=None):
        self.status = status
        self.message = message
        self.data = data
    
    def update(self, code=None, data=None, msg=None):
        """
        更新默认响应文本
        :param code:响应状态码
        :param data: 响应数据
        :param msg: 响应消息
        :return:
        """
        if code is not None:
            self.status = code
        if data is not None:
            self.data = data
        if msg is not None:
            self.message = msg
    
    def add_field(self, name=None, value=None):
        """
        在响应文本中加入新的字段，方便使用
        :param name: 变量名
        :param value: 变量值
        :return:
        """
        if name is not None and value is not None:
            self.__dict__[name] = value

    @property
    def body(self):
        """
        输出响应文本内容
        :return:
        """
        body = self.__dict__
        # body["data"] = body.pop("_data")
        # body["message"] = body.pop("_message")
        # body["status_code"] = body.pop("_status")
        return body
