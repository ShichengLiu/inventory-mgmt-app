import csv
import os

def menu(username="@prof-rossetti", products_count=100):

    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []








    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:

            products.append(dict(row))
    return products





def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")

    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id","name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)





def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)



def run():

    products = read_products_from_file()
    menu_1 = menu(username="Shicheng Liu", products_count=len(products))
    crud_operation = input(menu_1).title()
    print("YOU CHOOSE: " + crud_operation)
    if crud_operation == "List":
        list_products(products)
    elif crud_operation == "Show":
        show_product(products)
    elif crud_operation == "Create":
        create_product(products)
    elif crud_operation == "Update":
        update_product(products)
    elif crud_operation == "Destroy":
        destroy_product(products)
    elif crud_operation == "Reset":
        reset_products_file()
    else:
        print("UNRECOGNIZED OPERATION. PLEASE TRY AGAIN.")
        return run()


def list_products(products):
    print("LISTING PRODUCTS HERE")
    for product in products:
        print(" #" + str(product["id"]) + ": " + product["name"])
    return products
def show_product(products):
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")


    product = [p for p in products if p["id"] == product_id]
    if product:

        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER")



def auto_incremented_id(products):
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

def get_product_id(products): return int(products["id"])
headers = ["id", "name", "aisle", "department", "price"]
user_input_headers = [header for header in headers if header != "id"]

def create_product(products):
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id(products) }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)
    write_products_to_file(products=products)

def update_product(products):
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)
    write_products_to_file(products=products)
def destroy_product(products):
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

    write_products_to_file(products=products)


if __name__ == "__main__":
    run()
