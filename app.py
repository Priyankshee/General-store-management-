from flask import Flask, render_template, request,redirect,jsonify,url_for
import mysql.connector
from mysql.connector.errors import IntegrityError
app = Flask(__name__)

# Establish connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="STORE"
)

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/createproduct')
def createproduct():
    return render_template('createproduct.html')

@app.route('/createcustomer')
def createcustomer():
    return render_template('createcustomer.html')

@app.route('/createpurchase')
def createpurchase():
    return render_template('createpurchase.html')

@app.route('/createsupplier')
def createsupplier():
    return render_template('createsupplier.html')

@app.route('/createsupplies')
def createsupplies():
    return render_template('createsupplies.html')

@app.route('/submit_customer', methods=['POST'])
def submit_customer():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    customer_id = request.form['Customer_ID']
    customer_name = request.form['C_name']
    customer_phone = request.form['C_phone']

    # Insert the new customer into the database
    sql = "INSERT INTO Customer (customerid, customername, phno) VALUES (%s, %s, %s)"
    val = (customer_id, customer_name, customer_phone)
    mycursor.execute(sql, val)
    mydb.commit()

    # Close the cursor
    mycursor.close()

    return "Customer created successfully!"

@app.route('/submit_product', methods=['POST'])
def submit_product():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    product_id = request.form['productid']
    product_name = request.form['prodname']
    cost_price = request.form['costprice']
    selling_price = request.form['price']
    stock_quantity = request.form['quantity']
    supplier_id = request.form['supplier_id']

    # Insert the new product into the database
    sql = "INSERT INTO Product (productid, prodname, costprice, price, quantity, supplier_id) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (product_id, product_name, cost_price, selling_price, stock_quantity, supplier_id)
    mycursor.execute(sql, val)
    mydb.commit()

    # Close the cursor
    mycursor.close()

    return "Product created successfully!"

@app.route('/submit_supplier', methods=['POST'])
def submit_supplier():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    supplier_id = request.form['Supplier_ID']
    supplier_name = request.form['S_name']
    supplier_phone = request.form['S_phone']

    # Insert the new supplier into the database
    sql = "INSERT INTO Supplier (supplierid, suppliername, phno) VALUES (%s, %s, %s)"
    val = (supplier_id, supplier_name, supplier_phone)
    mycursor.execute(sql, val)
    mydb.commit()

    # Close the cursor
    mycursor.close()

    return "Supplier created successfully!"

@app.route('/submit_purchase', methods=['POST'])
def submit_purchase():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Retrieve form data
    customer_id = request.form['customer_id']
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    date_of_purchase = request.form['date_of_purchase']

    # Insert the new purchase into the database
    sql = "INSERT INTO Purchase (product_id, customer_id, quantity, dateofpurchase) VALUES (%s, %s, %s, %s)"
    val = (product_id, customer_id, quantity, date_of_purchase)
    mycursor.execute(sql, val)
    mydb.commit()

    # Close the cursor
    mycursor.close()

    return "Purchase created successfully!"
@app.route('/submit_supplies', methods=['POST'])
def submit_supplies():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # Retrieve form data
    supplier_id = request.form['supplier_id']
    prod_id = request.form['prod_id']
    stock_quantity = request.form['stock_quantity']
    stock_date = request.form['stock_date']

    # Insert the new supply into the database
    sql = "INSERT INTO Supplies (supplier_id, prod_id, stock_quantity, stock_date) VALUES (%s, %s, %s, %s)"
    val = (supplier_id, prod_id, stock_quantity, stock_date)
    mycursor.execute(sql, val)
    mydb.commit()

    # Close the cursor
    mycursor.close()

    return "Supply added successfully!"

@app.route('/view_products')
def view_products():
    # Fetch products from the database
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM Product")
    products = mycursor.fetchall()
    mycursor.close()

    # Render the view_products.html template with the products data
    return render_template('viewproducts.html', products=products)
@app.route('/view_suppliers')
def view_suppliers():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor(dictionary=True)

    # Execute SQL query to retrieve suppliers
    mycursor.execute("SELECT * FROM Supplier")
    suppliers = mycursor.fetchall()
    
    # Close the cursor
    mycursor.close()

    # Render view_suppliers.html template with the list of suppliers
    return render_template('viewsuppliers.html', suppliers=suppliers)
@app.route('/view_customers')
def view_customers():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor(dictionary=True)

    # Execute SQL query to retrieve customers
    mycursor.execute("SELECT * FROM Customer")
    customers = mycursor.fetchall()
    
    # Close the cursor
    mycursor.close()

    # Render view_customers.html template with the list of customers
    return render_template('viewcustomers.html', customers=customers)
@app.route('/view_purchases')
def view_purchases():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor(dictionary=True)

    # Execute SQL query to retrieve purchases
    mycursor.execute("SELECT * FROM Purchase")
    purchases = mycursor.fetchall()
    
    # Close the cursor
    mycursor.close()

    # Render view_purchases.html template with the list of purchases
    return render_template('viewpurchases.html', purchases=purchases)
@app.route('/view_supplies')
def view_supplies():
    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor(dictionary=True)

    # Execute SQL query to retrieve supplies
    mycursor.execute("SELECT * FROM Supplies")
    supplies = mycursor.fetchall()
    
    # Close the cursor
    mycursor.close()

    # Render viewsupplies.html template with the list of supplies
    return render_template('viewsupplies.html', supplies=supplies)
@app.route('/delete_supplier', methods=['POST'])
def delete_supplier():
    if request.method == 'POST':
        # Get the supplier ID from the form submission
        supplier_id = request.form['supplier_id']
        
        try:
            # Perform deletion logic here (e.g., delete the supplier from the database)
            mycursor = mydb.cursor()
            sql = "DELETE FROM Supplier WHERE supplierid = %s"
            val = (supplier_id,)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()

            # Redirect to the view suppliers page after successful deletion
            return redirect(url_for('view_suppliers'))
        except IntegrityError as e:
            # If the supplier is linked to other tables, handle the integrity error
            return "Can't delete supplier because it is linked to other tables"
# #trial
# @app.route('/purchase', methods=['POST'])
# def purchase():
#     if request.method == 'POST':
#         product_id = request.form['product_id']
#         quantity = request.form['quantity']

#         # Update stock quantity in Product table
#         mycursor = mydb.cursor()
#         mycursor.execute("UPDATE Product SET quantity = quantity - %s WHERE productid = %s", (quantity, product_id))
#         mydb.commit()
#         mycursor.close()

#         # Fetch updated product information
#         updated_product = fetch_product_info(product_id)

#         return jsonify(updated_product)

# @app.route('/supply', methods=['POST'])
# def supply():
#     if request.method == 'POST':
#         product_id = request.form['product_id']
#         quantity = request.form['quantity']

#         # Update stock quantity in Product table
#         mycursor = mydb.cursor()
#         mycursor.execute("UPDATE Product SET quantity = quantity + %s WHERE productid = %s", (quantity, product_id))
#         mydb.commit()
#         mycursor.close()

#         # Fetch updated product information
#         updated_product = fetch_product_info(product_id)

#         return jsonify(updated_product)

# def fetch_product_info(product_id):
#     # Fetch product information from the database
#     mycursor = mydb.cursor(dictionary=True)
#     mycursor.execute("SELECT * FROM Product WHERE productid = %s", (product_id,))
#     product_info = mycursor.fetchone()
#     mycursor.close()

#     return product_info
# Route to handle the deletion of a supplier

# Route to handle the update of a supplier
@app.route('/update_supplier', methods=['GET', 'POST'])
def update_supplier():
    if request.method == 'POST':
        # Get the updated supplier data from the form submission
        supplier_id = request.form['supplier_id']
        new_name = request.form['new_name']
        new_phone = request.form['new_phone']
        
        # Perform update logic here (e.g., update the supplier in the database)
        mycursor = mydb.cursor()
        sql = "UPDATE Supplier SET suppliername = %s, phno = %s WHERE supplierid = %s"
        val = (new_name, new_phone, supplier_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        # Redirect to the view suppliers page after update
        return redirect(url_for('view_suppliers'))

    

@app.route('/update_product', methods=['POST'])
def update_product():
    if request.method == 'POST':
        # Get the form data
        product_id = request.form['product_id']
        new_name = request.form['new_name']
        new_costprice = request.form['new_costprice']
        new_price = request.form['new_price']
        new_quantity = request.form['new_quantity']
        
        # Update the product record in the database
        mycursor = mydb.cursor()
        sql = "UPDATE Product SET prodname = %s, costprice = %s, price = %s, quantity = %s WHERE productid = %s"
        val = (new_name, new_costprice, new_price, new_quantity, product_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        # Redirect to the view products page after updating
        return redirect(url_for('view_products'))

@app.route('/delete_product', methods=['POST'])
def delete_product():
    if request.method == 'POST':
        try:
            # Get the product ID from the form submission
            product_id = request.form['product_id']
            
            # Delete the product record from the database
            mycursor = mydb.cursor()
            sql = "DELETE FROM Product WHERE productid = %s"
            val = (product_id,)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()

            # Redirect to the view products page after deletion
            return redirect(url_for('view_products')) 
        except IntegrityError:
            # Handle integrity error
            return "Cannot delete product because it is referenced in other tables."

@app.route('/update_customer', methods=['POST'])
def update_customer():
    if request.method == 'POST':
        # Get the form data
        customer_id = request.form['customer_id']
        new_name = request.form['new_name']
        new_phone = request.form['new_phone']
        
        # Update the customer record in the database
        mycursor = mydb.cursor()
        sql = "UPDATE Customer SET customername = %s, phno = %s WHERE customerid = %s"
        val = (new_name, new_phone, customer_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        # Redirect to the view customers page after updating
        return redirect(url_for('view_customers'))


@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    if request.method == 'POST':
        # Get the customer ID from the form submission
        customer_id = request.form['customer_id']
        
        # Attempt to delete the customer record from the database
        try:
            mycursor = mydb.cursor()
            sql = "DELETE FROM Customer WHERE customerid = %s"
            val = (customer_id,)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()

            # Redirect to the view customers page after successful deletion
            return redirect(url_for('view_customers'))
        except IntegrityError as e:
            # Handle integrity error (foreign key constraint violation)
            return"Cannot delete customer because it is referenced by other tables."
            
# Update Purchase Route
@app.route('/update_purchase', methods=['POST'])
def update_purchase():
    if request.method == 'POST':
        # Get the form data
        purchase_id = request.form['purchase_id']
        new_quantity = request.form['new_quantity']
        new_date = request.form['new_date']
        
        # Server-side validation
        if new_quantity.isdigit():  # Check if new_quantity is a valid integer
            # Update the purchase record in the database
            mycursor = mydb.cursor()
            sql = "UPDATE Purchase SET quantity = %s, dateofpurchase = %s WHERE purchaseid = %s"
            val = (new_quantity, new_date, purchase_id)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()

            # Redirect to the view purchases page after updating
            return redirect(url_for('view_purchases'))
        else:
            # If new_quantity is not a valid integer, return an error message
            return "Error: Quantity must be a valid integer."

# Delete Purchase Route
@app.route('/delete_purchase', methods=['POST'])
def delete_purchase():
    if request.method == 'POST':
        # Get the purchase ID from the form submission
        purchase_id = request.form['purchase_id']
        
        # Delete the purchase record from the database
        mycursor = mydb.cursor()
        sql = "DELETE FROM Purchase WHERE purchaseid = %s"
        val = (purchase_id,)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()

        # Redirect to the view purchases page after deletion
        return redirect(url_for('view_purchases'))

@app.route('/update_supply_quantity', methods=['POST'])
def update_supply_quantity():
    if request.method == 'POST':
        # Get form data
        supplier_id = request.form['supplier_id']
        prod_id = request.form['prod_id']
        new_quantity = request.form['new_quantity']

        try:
            # Assuming you are using MySQL and have a connection named 'mydb'
            mycursor = mydb.cursor()

            # Update the stock quantity in the database
            sql_quantity = "UPDATE Supplies SET stock_quantity = %s WHERE supplier_id = %s AND prod_id = %s"
            val_quantity = (new_quantity, supplier_id, prod_id)

            mycursor.execute(sql_quantity, val_quantity)

            mydb.commit()
            mycursor.close()

            # Redirect to the view supplies page after updating
            return redirect(url_for('view_supplies'))

        except Exception as e:
            # Handle database errors or other exceptions
            return f"Error updating supply quantity: {str(e)}"

@app.route('/update_supply_date', methods=['POST'])
def update_supply_date():
    if request.method == 'POST':
        # Get form data
        supplier_id = request.form['supplier_id']
        prod_id = request.form['prod_id']
        new_date = request.form['new_date']

        try:
            # Assuming you are using MySQL and have a connection named 'mydb'
            mycursor = mydb.cursor()

            # Update the stock date in the database
            sql_date = "UPDATE Supplies SET stock_date = %s WHERE supplier_id = %s AND prod_id = %s"
            val_date = (new_date, supplier_id, prod_id)

            mycursor.execute(sql_date, val_date)

            mydb.commit()
            mycursor.close()

            # Redirect to the view supplies page after updating
            return redirect(url_for('view_supplies'))

        except Exception as e:
            # Handle database errors or other exceptions
            return f"Error updating supply date: {str(e)}"
@app.route('/delete_supply', methods=['POST'])
def delete_supply():
    supplier_id = request.form['supplier_id']
    prod_id = request.form['prod_id']
    try:
        # Create cursor object
        mycursor = mydb.cursor()
        # Delete the supply from the database
        mycursor.execute("DELETE FROM Supplies WHERE supplier_id = %s AND prod_id = %s", (supplier_id, prod_id))
        # Commit changes
        mydb.commit()
        # Close cursor
        mycursor.close()
        return redirect(url_for('view_supplies'))
    except Exception as e:
        return jsonify({'error': str(e)})
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Supplier ("
                 "supplierid VARCHAR(30) PRIMARY KEY NOT NULL,"
                 "suppliername VARCHAR(255) NOT NULL,"
                 "phno VARCHAR(20) NOT NULL"
                 ")")

# Create Product table
mycursor.execute("CREATE TABLE IF NOT EXISTS Product ("
                 "productid VARCHAR(30) PRIMARY KEY,"
                 "prodname VARCHAR(255) NOT NULL,"
                 "costprice FLOAT NOT NULL,"
                 "price FLOAT NOT NULL,"
                 "quantity INT NOT NULL,"
                 "supplier_id VARCHAR(30) NOT NULL,"
                 "FOREIGN KEY (supplier_id) REFERENCES Supplier(supplierid)"
                 ")")

# Create Customer table
mycursor.execute("CREATE TABLE IF NOT EXISTS Customer ("
                 "customerid VARCHAR(30) PRIMARY KEY NOT NULL,"
                 "customername VARCHAR(255) NOT NULL,"
                 "phno VARCHAR(20)"
                 ")")

# Create Purchase table
mycursor.execute("CREATE TABLE IF NOT EXISTS Purchase ("
                 "purchaseid INT AUTO_INCREMENT PRIMARY KEY,"
                 "product_id VARCHAR(30) NOT NULL,"
                 "customer_id VARCHAR(30) NOT NULL,"
                 "quantity INT NOT NULL,"
                 "dateofpurchase DATE NOT NULL,"
                 "FOREIGN KEY (product_id) REFERENCES Product(productid),"
                 "FOREIGN KEY (customer_id) REFERENCES Customer(customerid)"
                 ")")


# Create Supplies table
mycursor.execute("CREATE TABLE IF NOT EXISTS Supplies ("
                 "supplier_id VARCHAR(30) NOT NULL,"
                 "prod_id VARCHAR(30) NOT NULL,"
                 "stock_quantity INT NOT NULL,"
                 "stock_date DATE NOT NULL,"
                 "PRIMARY KEY (supplier_id, prod_id),"
                 "FOREIGN KEY (supplier_id) REFERENCES Supplier(supplierid),"
                 "FOREIGN KEY (prod_id) REFERENCES Product(productid)"
                 ")")

# Close the cursor
mycursor.close()

if __name__ == '__main__':
    app.run(debug=True)

