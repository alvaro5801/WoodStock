from typing import List
from entities.batch import Batch

class Product:
    def __init__(self, name: str, description: str, batches_list: List[Batch] = []) -> None:
        self.name = name
        self.description = description
        self.batches_list = batches_list
        self.__id = None
    
    @property
    def id(self) -> int:
        return self.__id

    @property
    def quantity(self) -> int:
        if self.batches_list == []:
            return 0
        total_quantity = 0
        for batch in self.batches_list:
            total_quantity += batch.quantity
        return total_quantity