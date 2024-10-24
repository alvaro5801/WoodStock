class Product:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.__id = None
    
    @property
    def id(self) -> int:
        return self.__id