import openpyxl
from datetime import datetime

from functions import connect

print("First output from main.py file")

try:
    inv_file = openpyxl.load_workbook("resources/inventory.xlsx")
    product_list = inv_file["Sheet1"]

    products_per_supplier = dict()
    total_value_per_supplier = dict()
    product_no_under_21 = dict()
    print(f'{product_list.max_row} rows in sheet')

    #for product_item in product_list.max_row:

    for product_row in range(2, product_list.max_row +   1):
        supplier_name = product_list.cell(product_row, 4).value
        inventory = product_list.cell(product_row, 2).value
        price = product_list.cell(product_row, 3).value
        product_no = product_list.cell(product_row, 1)
        inventory_price = product_list.cell(product_row, 5)

        #enlisting suppliers
        if supplier_name in products_per_supplier:
            #current_number_producs = products_per_supplier[supplier_name]
            current_number_producs = products_per_supplier.get(supplier_name)
            products_per_supplier[supplier_name] = current_number_producs + 1
        else:
            print("Adding new Supplier")
            products_per_supplier[supplier_name] = 1

        #calculating total value per supplier
        if supplier_name in total_value_per_supplier:
            current_total_value_per_supplier = total_value_per_supplier.get(supplier_name) 
            total_value_per_supplier[supplier_name] = current_total_value_per_supplier + (inventory * price)
        else:
            print("Calculating first product total value per supplier")
            total_value_per_supplier[supplier_name] = inventory * price

        #calculating total value per supplier
        if inventory < 21:
            product_no_under_21[product_no] = inventory

        #sumtotal for product
        inventory_price.value  = inventory * price

    print(products_per_supplier)
    print(total_value_per_supplier)
    print(product_no_under_21)

    current_datetime = datetime.now()
    #inv_file.save("resources/new-inventory-with-sumtotal-"+current_datetime.strftime('%m-%d-%Y--%H-%M-%S')+".xlsx")

except Exception:
    print("Something happend")

connect()

print("Last output from main.py file")

 