from tabulate import tabulate

class Inventory:
    def __init__(self):
        self.products = [
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
    
    def list_products(self):
        return self.products
    
    def create_product(self, product_id, name, price, category, quantity):
        ids = map(lambda product: product["id"], self.products)

        if product_id not in ids:
            self.products.append({
                'id': product_id,
                'name': name,
                'price': price,
                'category': category,
                'quantity': quantity,
            })
            return self.products[-1]
        else:
            raise Exception("ID já está em uso!")

    def update_product(self, product_id, attribute_name, new_value):
        product_index = None

        for (index, product) in enumerate(self.products):
            if product["id"] == product_id:
                product_index = index

        if product_index == None:
            raise Exception("Produto não encontrado!\nDigite ENTER para continuar")

        self.products[product_index][attribute_name] = new_value

        return self.products[product_index]

    def delete_product(self, product_id):
        product_index = None

        for (index, product) in enumerate(self.products):
            if product["id"] == product_id:
                product_index = index

        if product_index != None:
            del self.products[product_index]
            return product_id
        else:
            raise Exception("Produto não encontrado!")

    def delete_all_products(self):
        self.products.clear()

    def sell_product(self, product_id, quantity):
        product_index = None

        for (index, product) in enumerate(self.products):
            if product["id"] == product_id:
                product_index = index

        if product_index != None:
            if quantity > self.products[index]["quantity"]:
                raise Exception("Quantidade não pode ser maior que o disponível no estoque")
            else:
                self.products[index]["quantity"] -= quantity
                return self.products[index]
        else:
            raise Exception("Produto não encontrado!")

    def buy_product(self, product_id, quantity):
        product_index = None

        for (index, product) in enumerate(self.products):
            if product["id"] == product_id:
                product_index = index

        if product_index != None:
            if quantity < 1:
                raise Exception("Quantidade não pode ser menor que 1")
            else:
                self.products[index]["quantity"] += quantity
                return self.products[index]
        else:
            raise Exception("Produto não encontrado!")
    
    def list_category_products(self, category):
        categories = map(lambda product: product["category"], self.products)

        if category not in categories:
            raise Exception("Categoria vazia!")

        products_table = []

        for product in self.products:
            if product["category"] == category:
                product_data = [
                    product["id"],
                    product["name"],
                    product["price"],
                    product["category"],
                    product["quantity"]
                ]
                products_table.append(product_data)

        return products_table

    def delete_category_products(self, category):
        categories = map(lambda product: product["category"], self.products)

        if category not in categories:
            raise Exception("Categoria vazia!")

        deleted_product_ids = []

        for (index, product) in enumerate(self.products):
            if product["category"] == category:
                product_id = product["id"]
                del self.products[index]
                deleted_product_ids.append(product_id)

        return deleted_product_ids