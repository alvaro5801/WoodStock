import json, os
from entities.product import Product
from batch_repository import BatchRepository
from typing import List

class ProductRepository:
    """
    Classe responsável por consultar e salvar produtos no banco de dados
    """
    def __init__(self) -> None:
        """
        Guarda todos os registros de produtos do banco de dados e o caminho para o banco de dados
        """
        self.path_name = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}products.json"
        with open(self.path_name, 'r') as file:
            self.products_list = json.load(file)
    
    def find_by_id(self, id: int) -> Product:
        """
        Retorna o produto com o id fornecido

        Args:
            id (int): id do produto

        Returns:
            Product: entidade de Produto contendo o objeto do respectivo produto
        """
        product_index = id -1
        product = self.products_list[product_index]
        product_batches = BatchRepository().find_by_product_id(id)
        product_entity = Product(product["name"], product["description"], [product_batches])
        product_entity._Product__id = product["id"]
        return product_entity
        
    def find_last(self) -> Product:
        """
        Encontra o último registro de produto (o mais novo)

        Returns:
            Product: entidade de Produto contendo o objeto do último produto registrado
        """
        product = self.products_list[-1]
        product_entity = Product(product["name"], product["description"])
        product_entity._Product__id = product["id"]
        product_entity.batches_list = BatchRepository().find_by_product_id(product_entity.id)
        return product_entity

    def find_all(self) -> List[Product]:
        """
        Retorna todos os registros de produtos

        Returns:
            list: Lista de entidades dos produtos 
        """
        all_product_entities = []
        for product in self.products_list:
            product_entity = Product(product["name"], product["description"])
            product_entity._Product__id = product["id"]
            product_entity.batches_list = BatchRepository().find_by_product_id(product_entity.id)
            all_product_entities.append(product_entity)
        
        return all_product_entities
    
    def create(self, product: Product) -> True:
        """
        Cria um registro de produto no banco de dados

        Args:
            product (Product): Uma instância de Product

        Returns:
            bool: True caso o produto tenha sido criado com sucesso
        """
        current_product_id = self.find_last().id + 1 if self.products_list != [] else 1
        self.products_list.append({"id": current_product_id, "name": product.name, "description": product.description})
        batch_repository = BatchRepository()
        for batch in product.batches_list:
            batch._Batch__product_id = current_product_id
            batch_repository.create(batch, current_product_id)
        with open(self.path_name, "w") as file:
            json.dump(self.products_list, file, indent=4, ensure_ascii=False)
        return True


