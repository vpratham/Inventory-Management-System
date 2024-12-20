#MainWindow.py

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import threading
import os
import tkinter.messagebox as messagebox
from database import fetch_stock,place_order_db
from sqli import sanitize

#from SniffMod import button_start_scan, button_stop_scan, set_result_display, starting_function, button_apply_filter
#from PassCheck import password_checker_call
#from document_scan import click
#from dcs import button_call


def onClickHome():
	switch_frame(frame_default)

def onClickNotif():
    switch_frame(frame_notis)

def onClickPlaceOrder():
    switch_frame(frame_porder)

def onClickCheckStock():
    switch_frame(frame_cstock)

def onClickHelp():
    switch_frame(frame_faq)

def switch_frame(new_frame):
    global currently_displayed_frame
    if currently_displayed_frame is not None:
        currently_displayed_frame.pack_forget()
    currently_displayed_frame = new_frame
    new_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

def mainWindow(userName, password):
    #CREATING FRAMES FOR DIFFERENT TABS
    global frame_notis, frame_porder, frame_faq, frame_cstock, frame_default, currently_displayed_frame, entry

    # CONSTANTS
    screenSize = "1000x680"
    colorSideBar = "#1d1d1d"
    default_color_but_darker = "#2d2d2d"
    customColor1 = "#4d4b4b"
    default_color = "#2B2B2B"
    VerInfo = "Ver 1.0\n24-9-24"
    
    
    # WINDOWS
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
	
    root = ctk.CTk()
    root.title("--Title--")
    root.geometry(screenSize)

    # WIDGETS
    main_frame = ctk.CTkFrame(root, fg_color=default_color, bg_color=default_color)
    main_frame.pack(fill=tk.BOTH, expand=1)

    sidebar_frame = ctk.CTkFrame(main_frame, width=400, fg_color=colorSideBar, bg_color=colorSideBar)
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)

    content_frame = ctk.CTkFrame(main_frame)
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    frame_default = ctk.CTkFrame(content_frame)
    frame_notis = ctk.CTkFrame(content_frame)
    frame_porder = ctk.CTkFrame(content_frame)
    frame_faq = ctk.CTkFrame(content_frame)
    frame_cstock = ctk.CTkFrame(content_frame)

    currently_displayed_frame = frame_default
    frame_default.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def create_home():
        # CREATE DEFAULT FRAME CONTENTS
        df_container_frame = ctk.CTkFrame(frame_default, width=450, height=450, fg_color="gray")
        df_container_frame.pack(expand=1, anchor="center")
        df_container_frame.pack_propagate(0)
        # HOME PAGE ELEMENTS
        label_title = ctk.CTkLabel(df_container_frame, text=f"Welcome {userName}!", font=("Helvetica", 30))
        label_title.pack(expand=1, pady=10, anchor="center")

        label_name = ctk.CTkLabel(df_container_frame, text="OptiStock Solutions™", font=("Helvetica", 18))
        label_name.pack(expand=1, pady=2, anchor="center")

        label_tag = ctk.CTkLabel(df_container_frame, text="Effecient Inventory, Simplified", font=("Helvetica", 18))
        label_tag.pack(expand=1, pady=2, anchor="center")

        label_version = ctk.CTkLabel(df_container_frame, text = VerInfo, font=("Helvetica",12))
        label_version.pack(expand=1, pady=2, anchor="center")
		
    def init_sidebar():
        
        #home page
        btn = ctk.CTkButton(sidebar_frame, text="Home", height=35, command=onClickHome)
        btn.pack(pady=10, padx=10)
		#dashboard 1 - notifications
        #btn1 = ctk.CTkButton(sidebar_frame, text="Notifications", height=35, command=onClickNotif)
        #btn1.pack(pady=10, padx=10)
		#dashboard 2 - place order
        btn2 = ctk.CTkButton(sidebar_frame, text="Place Order", height=35, command=onClickPlaceOrder)
        btn2.pack(pady=10, padx=10)
		#dashboard 3 - check stock level
        btn4 = ctk.CTkButton(sidebar_frame, text="Stock Levels", height=35, command=onClickCheckStock)
        btn4.pack(pady=10, padx=10)

        btn5 = ctk.CTkButton(sidebar_frame, text="Help", height=35, command=onClickHelp)
        btn5.pack(pady=10, padx=10)
	#Notifs
    def init_notif():
        pass
	
	#Place Order
    def init_porder():
        def place_order():
            s_item = dropdown_item.get()  # Get the selected item
            s_qty = dropdown_qty.get()    # Get the selected quantity
            if s_item == "Choose Item" or s_qty == "Select Quantity":
                messagebox.showerror("Invalid Entry", "Please select both an item and quantity.")  # Alert user
            else:
                response = messagebox.askokcancel("COnfirmation", f"Placing an Order for {s_qty} of {s_item}")
                if response:  # If the user clicks "OK"
                    #messagebox.showinfo("Success", f"Order submitted for {s_qty} of {s_item}!")  # Success message
                    print("Make an api call to palce order")
                    
                    flag = place_order_db(s_item,s_qty)
                    if flag:
                        messagebox.askokcancel("Success", "Order placed successfully")
                        #update()
                    else:
                        messagebox.askokcancel("Error", "Insufficient Stock")
                    print("Api call made")
                    dropdown_item.set("Choose Item")
                    dropdown_qty.set("Select Quantity")
                else:  # If the user clicks "Cancel"
                    pass

        items = []
        qtys = []

        for i in range(1,20):
            qtys.append(f"{i}")

        stock_data = fetch_stock()
        if stock_data:
            for product_id, product_info in stock_data.items():
                items.append(product_id)  # Retrieve the 'name' field, default to 'N/A' if missing
                #qtys.append(product_info.get("stock", "0"))  # Retrieve the 'stock' field, default to '0' if missing
                #tree.insert("", "end", values=(product_id, product_name, product_stock))

        #print("Place Order Click")

        df_containter_placeOrder = ctk.CTkFrame(frame_porder, width=400, height=400, fg_color=default_color_but_darker)
        df_containter_placeOrder.pack(expand=1,anchor="center")
        df_containter_placeOrder.pack_propagate(0)

        lbl = ctk.CTkLabel(df_containter_placeOrder, text="Place Order", font=("Helvetica", 20))
        lbl.pack(pady=20, anchor="center")

        lbl_item = ctk.CTkLabel(df_containter_placeOrder, text="Choose Item")
        lbl_item.pack(pady=(0,2), anchor="center")

        dropdown_item = ctk.CTkOptionMenu(df_containter_placeOrder, values=items)
        dropdown_item.set("Choose Item")  # Set the default text
        dropdown_item.pack(pady=(0,20), anchor="center")  # Adjust padding as needed

        lbl_qty = ctk.CTkLabel(df_containter_placeOrder, text="Choose Quantity")
        lbl_qty.pack(pady=(0,2), anchor="center")

        dropdown_qty = ctk.CTkOptionMenu(df_containter_placeOrder, values=qtys)
        dropdown_qty.set("Select Quantity")
        dropdown_qty.pack(pady=(0,20), anchor="center")  # Adjust padding as needed

        btn_submit = ctk.CTkButton(df_containter_placeOrder, text="Submit", command=place_order)
        btn_submit.pack(pady=10, anchor="center")
    	
    #Check Stock
    def init_cstock():
        app = ctk.CTkFrame(frame_cstock, width=600, fg_color=default_color_but_darker)
        app.pack(expand=1, anchor="center", fill=tk.Y)
        app.pack_propagate(False)

        # Define Treeview with three columns: ID, NAME, and STOCK
        tree = ttk.Treeview(app, columns=("ID", "NAME", "STOCK"), show="headings")
        
        # Set the headers for each column
        tree.heading("ID", text="Product ID")
        tree.heading("NAME", text="Product Name")
        tree.heading("STOCK", text="Stock Quantity")

        # Set the widths for each column
        tree.column("ID", width=150, anchor="center")
        tree.column("NAME", width=200, anchor="center")
        tree.column("STOCK", width=150, anchor="center")

        tree.pack(fill="both", expand=True, pady=10)

        # Fetch stock data from Firebase
        def update():
            def clear_tree():
                for item in tree.get_children():
                    tree.delete(item)

            clear_tree()
            stock_data = fetch_stock()
            
            if stock_data:
                # Insert each product's ID, Name, and Stock into the Treeview
                for product_id, product_info in stock_data.items():
                    product_name = product_info.get("name", "N/A")  # Retrieve the 'name' field, default to 'N/A' if missing
                    product_stock = product_info.get("stock", "0")  # Retrieve the 'stock' field, default to '0' if missing
                    tree.insert("", "end", values=(product_id, product_name, product_stock))

        button_refresh = ctk.CTkButton(app, text="Refresh", command=update)
        button_refresh.pack(anchor="center")

        update()

    def init_help():
        # Creating a help window

        def validate():
            name = name_entry_help.get()
            email = email_entry_help.get()
            desc = help_entry.get("1.0", "end-1c").strip()

            if sanitize(name,email,desc):
                print("Submitting request")
            else:
                print("Do nothing")


        helpw = ctk.CTkFrame(frame_faq, width=400,height=400, fg_color=default_color_but_darker)
        helpw.pack(expand=1, anchor="center")
        helpw.grid_columnconfigure(0, weight=1)  # First column
        helpw.grid_propagate(False)  # Keeps the frame from shrinking, but allows for size flexibility

        # Name Entry
        title_help = ctk.CTkLabel(helpw,text="User Queires",font=("Helvetica", 20))
        title_help.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")  # Span across both columns

        name_label_help = ctk.CTkLabel(helpw, text="Name")
        name_label_help.grid(row=1, column=0, padx=20, pady=10)  # Align label to the left
        name_entry_help = ctk.CTkEntry(helpw, placeholder_text="Enter your name", width=200)
        name_entry_help.grid(row=1, column=1, padx=20, pady=10)

        # Email Entry
        email_label_help = ctk.CTkLabel(helpw, text="Email")
        email_label_help.grid(row=2, column=0, padx=20, pady=10)  # Align label to the left
        email_entry_help = ctk.CTkEntry(helpw, placeholder_text="Enter your email", width=200)
        email_entry_help.grid(row=2, column=1, padx=20, pady=10)

        help_label = ctk.CTkLabel(helpw,text="Description: ")
        help_label.grid(row=3,column=0)
        help_entry = ctk.CTkTextbox(helpw, height=80, width=200)  # Adjust height as needed
        help_entry.grid(row=3, column=1, padx=20, pady=10)

        submit_button_help = ctk.CTkButton(helpw, text="Submit", command=validate)
        submit_button_help.grid(row=4, column=0, columnspan=2, padx=20, pady=20, sticky="ew")  # Span across both columns

    create_home()
    init_sidebar()
    init_notif()
    init_porder()
    init_cstock()
    init_help()
    root.mainloop()

if __name__ == "__main__":
    mainWindow("root", "rooooot")