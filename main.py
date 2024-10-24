import os
import json
from product_repository import ProductRepository
from entities.product import Product
from entities.batch import Batch
import datetime

def main():
    product = ProductRepository().find_last()
    print(f"Código: {product.id}, nome: {product.name}, descrição: {product.description}")
    print(product.quantity)
    
if __name__ == "__main__":
    main()