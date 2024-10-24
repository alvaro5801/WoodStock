import os
import json
from product_repository import ProductRepository
from entities.product import Product

def main():
    product_repository = ProductRepository()
    all_products = product_repository.find_all()
    for product in all_products:
        print(f"Código do produto: {product.id} | Nome do produto: {product.name} | Descrição: {product.description}")
    new_product = Product("Cuscuz", "Flocos de milho cozidos no vapor")
    product_repository.create(new_product)
    print(print(f"Código do produto: {new_product.id} | Nome do produto: {new_product.name} | Descrição: {new_product.description}"))

if __name__ == "__main__":
    main()