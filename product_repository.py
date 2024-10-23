import json, os
from product import Product

class ProductRepository:
    """
    Classe responsável por consultar e salvar produtos no banco de dados
    """
    def __init__(self):
        """
        Guarda todos os registros de produtos do banco de dados e o caminho para o banco de dados
        """
        self.path_name = os.path.dirname(__file__) + "\\database\\products.json"
        with open(self.path_name, 'r') as file:
            self.products_dict = json.load(file)
    
    def find_by_id(self, id: int) -> dict:
        """
        Retorna o produto com o id fornecido

        Args:
            id (int): id do produto

        Returns:
            dict: dicionário contendo as informações do produto
        """
        for product in self.products_dict:
            if (product['id'] == id):
                return product
            
    def find_last(self) -> dict:
        """
        Encontra o último registro de produto (o mais novo)

        Returns:
            dict: dicionário contendo as informações do produto
        """
        return self.products_dict[-1]

    def find_all(self) -> list:
        """
        Retorna todos os registros de produtos

        Returns:
            list: Lista de dicionários contendo os produtos 
        """
        return self.products_dict
    
    def create(self, name, description):
        """
        Cria um registro de produto no banco de dados

        Args:
            product (Product): Uma instância de Product

        Returns:
            bool: True caso o produto tenha sido criado com sucesso
        """
        last_id = self.find_last()["id"]
        self.products_dict.append({"id": last_id + 1, "name": name, "description": description})
        with open(self.path_name, "w") as file:
            json.dump(self.products_dict, file, indent=4, ensure_ascii=False)
        return True


