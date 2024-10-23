import os
import json

def main():
    arquivo = os.path.join(os.path.dirname(__file__), "database\\products.json")
    print(arquivo)
    #with open(arquivo, 'w') as file:
    #        product = {"name": "n sei", "description": "lorem ipsum"}
    #        json.dump(product, file, indent=4)

if __name__ == "__main__":
    main()