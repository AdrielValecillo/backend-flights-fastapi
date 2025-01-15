from app.db.database import SessionLocal

#

class Base:
    def __init__(self):
        self.db = SessionLocal()
        
        
        