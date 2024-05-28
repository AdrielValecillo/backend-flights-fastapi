from fastapi import HTTPException

class Responses:
    def __init__(self):
        pass

    def response_message(self, data: dict, message: str, code: int):
        return {"status": True, "data": data, "message": message, "code": code}
    
    def message_HTTPException(self, e: HTTPException):
        return {"status": False, "data": None, "messagehttp": e.detail, "code": e.status_code}

    def message_exception(self, e: Exception):
        return {"status": False, "data": None, "messagefatal": str(e), "code": 500}