import datetime
import os
import json
from typing import List
from entities.batch import Batch

class BatchRepository:
    def __init__(self) -> None:
        self.path_name = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}batches.json"
        with open(self.path_name, 'r') as file:
            self.batches_list = json.load(file)
    
    def find_by_id(self, id: int) -> Batch:
        """
        Retorna o lote com o id fornecido

        Args:
            id (int): id do lote

        Returns:
            Batch: entidade de lote contendo o objeto do respectivo lote
        """
        batch_index = id -1
        batch = self.batches_list[batch_index]
        arrivalDate = datetime.datetime.strptime(batch["arrival_date"], "%d/%m/%Y")
        expirationDate =  datetime.datetime.strptime(batch["expiration_date"], "%d/%m/%Y")
        batch_entity = Batch(arrivalDate, expirationDate, batch["quantity"])
        batch_entity._Batch__id = batch["id"]
        return batch_entity
        
    def find_last(self) -> Batch:
        """
        Encontra o último registro de lote (o mais novo)

        Returns:
            Batch: entidade de Produto contendo o objeto do último lote registrado
        """
        batch = self.batches_list[-1]
        arrivalDate = datetime.datetime.strptime(batch["arrival_date"], "%d/%m/%Y")
        expirationDate =  datetime.datetime.strptime(batch["expiration_date"], "%d/%m/%Y")
        batch_entity = Batch(arrivalDate, expirationDate, batch["quantity"])
        batch_entity._Batch__id = batch["id"]
        return batch_entity

    def find_all(self) -> List[Batch]:
        """
        Retorna todos os registros de produtos

        Returns:
            list: Lista de entidades dos produtos 
        """
        all_batch_entities = []
        for batch in self.batches_list:
            arrivalDate = datetime.datetime.strptime(batch["arrival_date"], "%d/%m/%Y")
            expirationDate =  datetime.datetime.strptime(batch["expiration_date"], "%d/%m/%Y")
            batch_entity = Batch(arrivalDate, expirationDate, batch["quantity"])
            batch_entity._Batch__id = batch["id"]
            all_batch_entities.append(batch_entity)
        
        return all_batch_entities
    
    def find_by_product_id(self, product_id: int) -> List[Batch]:
        batches_finded = []
        for batch in self.batches_list:
            if batch["product_id"] == product_id:
                arrivalDate = datetime.datetime.strptime(batch["arrival_date"], "%d/%m/%Y")
                expirationDate =  datetime.datetime.strptime(batch["expiration_date"], "%d/%m/%Y")
                batch_entity = Batch(arrivalDate, expirationDate, batch["quantity"])
                batch_entity._Batch__id = batch["id"]
                batches_finded.append(batch_entity)
        return batches_finded
    
    def create(self, batch: Batch, product_id: int) -> True:
        """
        Cria um registro de lote no banco de dados

        Args:
            batch (Batch): Uma instância de Batch

        Returns:
            bool: True caso o lote tenha sido criado com sucesso
        """
        current_batch_id = self.find_last().id + 1 if self.batches_list != [] else 1
        self.batches_list.append({"id": current_batch_id, "product_id": product_id, "arrival_date": batch.arrival_date.strftime("%d/%m/%Y"), "expiration_date": batch.expiration_date.strftime("%d/%m/%Y"), "quantity": batch.quantity})
        with open(self.path_name, "w") as file:
            json.dump(self.batches_list, file, indent=4, ensure_ascii=False)
            
        return True