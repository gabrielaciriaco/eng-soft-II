import unittest
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def test_should_initialize_without_products(self):
        inventory = Inventory()
        
        self.assertEqual([], inventory.products)

    def test_should_list_products(self):
        inventory = Inventory()
        
        self.assertEqual([], inventory.list_products())

    def test_create_product_should_return_new_product(self):
        inventory = Inventory()
        new_product = inventory.create_product(5, "test", 10, "test", 10)
        
        self.assertEqual(new_product, {
            "id": 5,
            "name": "test",
            "price": 10,
            "category": "test",
            "quantity": 10,
        })

    def test_create_product_should_add_to_product_list(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        
        self.assertEqual(inventory.list_products(), [{
            "id": 5,
            "name": "test",
            "price": 10,
            "category": "test",
            "quantity": 10,
        }])

    def test_create_product_should_raise_exception_if_id_exists(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)

        with self.assertRaises(Exception) as error:
            inventory.create_product(5, "test_2", 10, "test_2", 10)
        
        self.assertEqual(str(error.exception), 'ID já está em uso!')

    def test_update_product_should_return_updated_product(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        updated_product = inventory.update_product(5, "name", "test_2")
        
        self.assertEqual(updated_product, {
            "id": 5,
            "name": "test_2",
            "price": 10,
            "category": "test",
            "quantity": 10,
        })

    def test_update_product_should_update_product_list(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        inventory.update_product(5, "name", "test_2")
        
        self.assertEqual(inventory.list_products(), [{
            "id": 5,
            "name": "test_2",
            "price": 10,
            "category": "test",
            "quantity": 10,
        }])

    def test_update_product_should_raise_exception_if_id_not_exists(self):
        inventory = Inventory()

        with self.assertRaises(Exception) as error:
            inventory.update_product(5, "name", "test_2")
        
        self.assertEqual(str(error.exception), 'Produto não encontrado!')

    def test_update_product_should_raise_exception_if_attribute_name_not_exists(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)

        with self.assertRaises(Exception) as error:
            inventory.update_product(5, "test", "test_2")
        
        self.assertEqual(str(error.exception), 'Atributo inválido!')

    def test_delete_product_should_return_deleted_product_id(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        deleted_product_id = inventory.delete_product(5)
        
        self.assertEqual(deleted_product_id, 5) 

    def test_delete_product_should_update_product_list(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        inventory.delete_product(5)
        
        self.assertEqual(inventory.list_products(), [])

    def test_delete_product_should_raise_exception_if_id_not_exists(self):
        inventory = Inventory()

        with self.assertRaises(Exception) as error:
            inventory.delete_product(5)
        
        self.assertEqual(str(error.exception), 'Produto não encontrado!')

    def test_delete_all_products_should_update_product_list(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        inventory.create_product(6, "test_2", 10, "test_2", 10)
        inventory.delete_all_products()
        
        self.assertEqual(inventory.list_products(), [])
        
    def test_sell_product_should_return_updated_product(self):
        inventory = Inventory()
        inventory.create_product(5, "test", 10, "test", 10)
        updatedProduct = inventory.sell_product(5, 2)
        
        self.assertEqual(updatedProduct, {
            "id": 5,
            "name": "test",
            "price": 10,
            "category": "test",
            "quantity": 8,
        }) 

    def test_sell_product_should_raise_exception_if_id_not_exists(self):
        inventory = Inventory()

        with self.assertRaises(Exception) as error:
            inventory.sell_product(5, 2)
        
        self.assertEqual(str(error.exception), 'Produto não encontrado!')
