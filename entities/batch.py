from datetime import datetime

class Batch:
    def __init__(self, arrival_date: datetime, expiration_date: datetime, quantity: int) -> None:
        self.arrival_date = arrival_date
        self.expiration_date = expiration_date
        self.quantity = quantity
        self.__id = None
        self.__product_id = None
        
    @property
    def id(self) -> int:
        return self.__id