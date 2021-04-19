# coding: utf-8 
from flask import jsonify
from functools import wraps

def route(bp,  *args, **kwargs):
    kwargs.setdefault("strict_slashes", False)

    def decorator(f):
        # 调用 blueprint 的 route
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*args, **kwargs):
            # 这里执行函数，根据函数返回，直接用 json 格式封装返回值
            rv = f(*args, **kwargs)
            # 如果是整数或者浮点数，放进 data
            if isinstance(rv, (int, float)):
                res = ResponseObject()
                res.update(data = rv)
                return jsonify(res.body)
            # 如果是 tuple
            elif isinstance(rv, tuple):
                if len(rv) >= 3:
                    return jsonify(rv[0], rv[1], rv[2])
                else:
                    return jsonify(rv[0]), rv[1]
            # 字典
            elif isinstance(rv, dict):
                return jsonify(rv)
            # bytes值
            elif isinstance(rv, bytes):
                rv = rv.decode('utf-8')
                return jsonify(rv)
            else:
                return jsonify(rv)
        return f

    return decorator
        