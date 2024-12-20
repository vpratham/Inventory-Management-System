import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyANZeGyzfbkBFQDosbt4aQzO2CcjJiDhjE",
  "authDomain": "se-inventory-management-system.firebaseapp.com",
  "databaseURL": "https://se-inventory-management-system-default-rtdb.firebaseio.com",
  "projectId": "se-inventory-management-system",
  "storageBucket": "se-inventory-management-system.appspot.com",
  "messagingSenderId": "582543037725",
  "appId": "1:582543037725:web:a4c9278b4c04c3d5e53df4",
  "measurementId": "G-H062P4186M"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def fetch_stock():
    products = db.child("products").get()
    return products.val()

def place_order_db(product_id,quantity):
  print(product_id,quantity)
  if not product_id or not quantity.isdigit():
    #messagebox.showwarning("Input Error", "Please select a product and enter a valid quantity.")
    return False

  quantity = int(quantity)
  stock_data = fetch_stock()

  print(stock_data)

  print(0)
  if product_id in stock_data:
    current_stock = stock_data[product_id]["stock"]

    if quantity > current_stock:
      return False
      #messagebox.showwarning("Stock Error", f"Only {current_stock} units available for {stock_data[product_id]['name']}.")
    else:
      new_stock = current_stock - quantity
      db.child("products").child(product_id).update({"stock": new_stock})
      return True
      #messagebox.showinfo("Order Placed", f"Order placed for {quantity} units of {stock_data[product_id]['name']}.")
      # Refresh the stock display
      #update_stock_display()
  else:
    return False
    #messagebox.showerror("Error", "Selected product not found.")
#print(fetch_stock())

place_order_db("product10","10")