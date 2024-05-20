from fastapi import HTTPException

class Responses:
    def __init__(self):
        pass

    def message_HTTPException(self, e: HTTPException):
        return {"status": False, "data": None, "message": e.detail, "code": e.status_code}

    def message_exception(self, e: Exception):
        return {"status": False, "data": None, "message": str(e), "code": 500}