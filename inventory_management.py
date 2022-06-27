import json
from math import prod
import os.path
import time
import random
from turtle import clear
from tabulate import tabulate
import os
from inventory import Inventory


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


products = [
    {
        "id": 1,
        "name": "pinho sol",
        "price": 10,
        "category": "limpeza",
        "quantity": 10,
    },
    {
        "id": 2,
        "name": "água sanitária",
        "price": 8,
        "category": "limpeza",
        "quantity": 100,
    },
    {
        "id": 3,
        "name": "biscoito água e sal",
        "price": 2,
        "category": "comida",
        "quantity": 500,
    },
    {
        "id": 4,
        "name": "pasta de dente",
        "price": 9,
        "category": "higiene pessoal",
        "quantity": 50,
    },
]


def list_products(inventory):
    data_table = []
    for product in inventory.list_products():
        product_data = [product["id"], product["name"], product["quantity"]]
        data_table.append(product_data)

    print(tabulate(data_table, ['ID', 'Nome', 'Quantidade']))
    print("\nPressione ENTER para continuar")
    input()


def read_product(inventory):
    print("Digite o ID do produto")
    product_id = int(input())

    clear_console()

    try:
        product = inventory.get_product(product_id)

        product_data = [[
                product["id"],
                product["name"],
                product["price"],
                product["category"],
                product["quantity"]
            ]]

        headers = [
            "ID",
            "Nome",
            "Preço",
            "Categoria",
            "Quantidade"
        ]

        print(tabulate(product_data, headers))
    except Exception as error:
        print(str(error))

    print("\nPressione ENTER para continuar")
    input()


def create_product(inventory):
    print("Digite o id do produto:")
    product_id = int(input())
    print("Digite o nome do produto:")
    name = input()
    print("Digite o valor unitário do produto:")
    price = input()
    print("Digite a categoria do produto:")
    category = input()
    print("Digite a quantidade do produto")
    quantity = input()

    try:
        new_product = inventory.create_product(product_id, name, price, category, quantity)
        print("Produto \""+str(new_product["id"])+"\" adicionado com sucesso!")
    except Exception as error:
        print(str(error))

    print("\nDigite ENTER para continuar")
    input()


def update_product(inventory):
    print("Digite o ID do produto:")
    product_id = int(input())

    clear_console()

    try:
        product = inventory.get_product(product_id)

        product_data = [[
                product["id"],
                product["name"],
                product["price"],
                product["category"],
                product["quantity"]
            ]]

        headers = [
            "ID",
            "Nome",
            "Preço",
            "Categoria",
            "Quantidade"
        ]

        print(tabulate(product_data, headers))
    except Exception as error:
        print(str(error))
        print("\nDigite ENTER para continuar")
        input()
        return

    print("\n")

    attributes_table = [
        ["1", "id"],
        ["2", "name"],
        ["3", "price"],
        ["4", "category"],
        ["5", "quantity"],
    ]

    print(tabulate(attributes_table, ["Código", "Nome"]))
    print("\n\nDigite o código do atributo a ser atualizado")

    attribute_id = input()
    attribute_name = None

    for attribute in attributes_table:
        if attribute[0] == attribute_id:
            attribute_name = attribute[1]

    clear_console()

    try:
        print("\nDigite o novo valor:")
        new_value = input()
        inventory.update_product(product_id, attribute_name, new_value)
        print("\nProduto atualizado com sucesso!")
    except Exception as error:
        print(str(error))

    print("\nDigite ENTER para continuar")
    input()


def delete_product(inventory):
    print("Digite o ID do produto:")
    product_id = int(input())

    clear_console()

    try:
        inventory.delete_product(product_id)
        print("Produto removido com sucesso!")
    except Exception as error:
        print(str(error))

    print("\nDigite ENTER para continuar")
    input()


def delete_products():
    print("Digite os IDs dos produtos removidos, separados por vírgula:")
    product_ids = input().split(",")

    for (index, product_id) in enumerate(product_ids):
        product_ids[index] = int(product_id)

    for product_id in product_ids:
        clear_console()
        product_found = False

        for (index, product) in enumerate(products):
            if product["id"] == product_id:
                product_found = True
                del products[index]

        if product_found == False:
            print(
                f"Não foi possível encontrar um produto com o ID {product_id}")
            print("\nDigite ENTER para continuar")
            input()
        else:
            print(f"Produto de ID {product_id} removido")
            print("\nDigite ENTER para continuar")
            input()


def delete_all_products():
    products.clear()
    print("Todos os produtos foram removidos com sucesso!")
    print("\nDigite ENTER para continuar")
    input()


def sell_product():
    print("Digite ID do produtos comprado:")
    product_id = int(input())

    clear_console()
    print(f"Digite a quantidade do produto de ID {product_id}")
    quantity = int(input())
    product_found = False
    invalid_quantity = False
    clear_console()

    for (index, product) in enumerate(products):
        if product["id"] == product_id:
            product_found = True
            if quantity > products[index]["quantity"]:
                invalid_quantity = True
                print("Quantidade não pode ser maior que o disponível no estoque")
            else:
                products[index]["quantity"] -= quantity

    if invalid_quantity == True:
        print("\nDigite ENTER para continuar")
        input()
        return

    if product_found == False:
        print(
            f"Não foi possível encontrar um produto com o ID {product_id}")
        print("\nDigite ENTER para continuar")
        input()
    else:
        print(f"Quantidade do produto de ID {product_id} atualizada")
        print("\nDigite ENTER para continuar")
        input()


def sell_products():
    print("Digite os IDs dos produtos comprados, separados por vírgula:")
    product_ids = map(lambda product_id: int(product_id), input().split(","))

    for product_id in product_ids:
        clear_console()
        print(f"Digite a quantidade do produto de ID {product_id}")
        quantity = int(input())
        product_updated = False
        invalid_quantity = False
        clear_console()

        for (index, product) in enumerate(products):
            if product["id"] == product_id:
                if quantity > products[index]["quantity"]:
                    print("Quantidade não pode ser maior que o disponível no estoque")
                    invalid_quantity = True
                else:
                    products[index]["quantity"] -= quantity
                    product_updated = True

        if invalid_quantity == False and product_updated == False:
            print(
                f"Não foi possível encontrar um produto com o ID {product_id}")
        else:
            print(f"Quantidade do produto de ID {product_id} atualizada")

        print("\nDigite ENTER para continuar")
        input()


def buy_product():
    print("Digite o ID do produto comprado:")
    product_id = int(input())

    clear_console()
    print(f"Digite a quantidade do produto de ID {product_id}")
    quantity = int(input())
    product_found = False
    invalid_quantity = False
    clear_console()

    for (index, product) in enumerate(products):
        if product["id"] == product_id:
            product_found = True
            if quantity < 1:
                invalid_quantity = True
                print("Quantidade não pode ser menor que 1")
            else:
                products[index]["quantity"] += quantity

    if invalid_quantity == True:
        print("\nDigite ENTER para continuar")
        input()
        return

    if product_found == False:
        print(
            f"Não foi possível encontrar um produto com o ID {product_id}")
        print("\nDigite ENTER para continuar")
        input()
    else:
        print(f"Quantidade do produto de ID {product_id} atualizada")
        print("\nDigite ENTER para continuar")
        input()


def buy_products():
    print("Digite os IDs dos produtos comprados, separados por vírgula:")
    product_ids = input().split(",")

    for (index, product_id) in enumerate(product_ids):
        product_ids[index] = int(product_id)

    for product_id in product_ids:
        clear_console()
        print(f"Digite a quantidade do produto de ID {product_id}")
        quantity = int(input())
        product_found = False
        invalid_quantity = False
        clear_console()

        for (index, product) in enumerate(products):
            if product["id"] == product_id:
                product_found = True
                if quantity < 1:
                    invalid_quantity = True
                    print("Quantidade não pode ser menor que 1")
                else:
                    products[index]["quantity"] += quantity

        if invalid_quantity == True:
            print("\nDigite ENTER para continuar")
            input()
            continue

        if product_found == False:
            print(
                f"Não foi possível encontrar um produto com o ID {product_id}")
            print("\nDigite ENTER para continuar")
            input()
        else:
            print(f"Quantidade do produto de ID {product_id} atualizada")
            print("\nDigite ENTER para continuar")
            input()


def list_category_products():
    print("Digite a categoria desejada:")
    category = input()

    categories = map(lambda product: product["category"], products)

    clear_console()

    if category not in categories:
        print("Categoria vazia!")
        print("\nDigite ENTER para continuar")
        input()
        return

    headers = [
        "ID",
        "Nome",
        "Preço",
        "Categoria",
        "Quantidade"
    ]

    products_table = []

    clear_console()

    for product in products:
        if product["category"] == category:
            product_data = [
                product["id"],
                product["name"],
                product["price"],
                product["category"],
                product["quantity"]
            ]
            products_table.append(product_data)

    print(tabulate(products_table, headers))

    print("\nDigite ENTER para continuar")
    input()


def delete_category_products():
    print("Digite a categoria desejada:")
    category = input()

    categories = map(lambda product: product["category"], products)

    clear_console()

    if category not in categories:
        print("Categoria vazia!")
        print("\nDigite ENTER para continuar")
        input()
        return

    for (index, product) in enumerate(products):
        if product["category"] == category:
            product_id = product["id"]
            del products[index]
            print(f"Produto de id {product_id}")

    print("\nDigite ENTER para continuar")
    input()


def handle_invalid_command():
    print("Comando Inválido!")
    print("\nDigite ENTER para continuar")
    input()


commands_table = [
    ["0", "Sair"],
    ["1", "Listar itens do estoque"],
    ["2", "Mostrar produto com seus detalhes"],
    ["3", "Inserir produto"],
    ["4", "Atualizar produto"],
    ["5", "Deletar produto"],
    ["6", "Deletar produtos"],
    ["7", "Deletar todos os produtos"],
    ["8", "Vender produto"],
    ["9", "Vender produtos"],
    ["10", "Comprar produto"],
    ["11", "Comprar produtos"],
    ["12", "Listar produtos de categoria"],
    ["13", "Deletar produtos de categoria"],
]

commands = {
    1: list_products,
    2: read_product,
    3: create_product,
    4: update_product,
    5: delete_product,
    6: delete_products,
    7: delete_all_products,
    8: sell_product,
    9: sell_products,
    10: buy_product,
    11: buy_products,
    12: list_category_products,
    13: delete_category_products,
    "invalid": handle_invalid_command
}


def main():
    inventory = Inventory()

    inventory.products = [
        {
            "id": 1,
            "name": "pinho sol",
            "price": 10,
            "category": "limpeza",
            "quantity": 10,
        },
        {
            "id": 2,
            "name": "água sanitária",
            "price": 8,
            "category": "limpeza",
            "quantity": 100,
        },
        {
            "id": 3,
            "name": "biscoito água e sal",
            "price": 2,
            "category": "comida",
            "quantity": 500,
        },
        {
            "id": 4,
            "name": "pasta de dente",
            "price": 9,
            "category": "higiene pessoal",
            "quantity": 50,
        },
    ]

    clear_console()

    print("==== Sistema de controle de estoque ====\n")

    while (1):
        print(tabulate(commands_table, ["Cód.", "Comando"]))
        print("\nDigite o código do comando desejado:")

        n = int(input())

        clear_console()

        if (n == 0):
            break
        else:
            commands.get(n, commands["invalid"])(inventory)

        clear_console()


main()
