#loginwin.py

import tkinter as tk
import customtkinter as ctk 
from MainWindow import mainWindow
from passwordSec import validate_user
from passSec import check_admin_privilages,add_admin_account, create_user
def mainLogin():

	#CONSTANTS

	customColor1 = "#4d4b4b"
	customColor2 = "#de4343" #invalid credentials color

	constPasswordHolder = "*"
	
	constPassword = "home"
	constUsername = "home"

	def onSubmit(event=None):

		passw = password_Textbox.get()
		usern = username_Textbox.get()

		if validate_user(usern,passw):
			#end_background_tasks()

			label_authStat.pack_forget()
			password_Textbox.configure(bg_color="transparent")
			username_Textbox.configure(bg_color="transparent")

			home.destroy()

			mainWindow(usern,passw)

		else:
			label_authStat.pack(pady=1)
			password_Textbox.configure(bg_color="red")
			username_Textbox.configure(bg_color="red")


	def show_password():
		if password_Textbox.cget("show") == constPasswordHolder:
			password_Textbox.configure(show="")
			show_password_button.configure(text="Hide Password")
		else:
			password_Textbox.configure(show=constPasswordHolder)
			show_password_button.configure(text="Show Password")
	

	def onValidateAdmin():
		usern = username_tb_admin.get()
		pasw = password_tb_admin.get()

		flag_admin = check_admin_privilages(usern, pasw)
		#return flag_admin
		if flag_admin:
			frame_fields.pack_forget()
			frame_addu.pack(expand=1, anchor="center")
		else:
			label_authStat2.pack(pady=1)

	def create_new_user():
		usr = username_add.get()
		passw = password_add.get()
		admin_f = checkbox_var.get()

		#
		if admin_f:
			create_user(usr,passw)
			add_admin_account(usr)

			add_user_win.destroy()
		else:
			create_user(usr,passw)
			add_user_win.destroy()



	def add_user():
		global username_tb_admin, password_tb_admin, frame_fields, frame_addu, username_add, password_tb, checkbox_var, password_add, username_add, add_user_win, label_authStat2
		add_user_win = ctk.CTk()
		add_user_win.title("Add a new user")
		add_user_win.geometry("500x500")
		#
		frame_fields = ctk.CTkFrame(add_user_win, width=450, height=450, fg_color=customColor1)
		frame_fields.pack(expand=1,anchor="center")
		label_authStat2 = ctk.CTkLabel(frame_fields, text="Invalid Credentials", text_color="red")

		label_title = ctk.CTkLabel(frame_fields, text="Note: You need an admin account to add users")
		label_title.pack(expand=1,pady=10)

		username_tb_admin = ctk.CTkEntry(frame_fields, placeholder_text="Enter Admin Username")
		username_tb_admin.pack(pady=2, padx=10, expand=1)

		password_tb_admin = ctk.CTkEntry(frame_fields, placeholder_text="Enter Password", show=constPasswordHolder)
		password_tb_admin.pack(pady=2, padx=10, expand=1)

		btn_a = ctk.CTkButton(frame_fields, text="Login", command=onValidateAdmin)
		btn_a.pack(pady=10,padx=10)

		frame_addu = ctk.CTkFrame(add_user_win, width=450,height=450,fg_color=customColor1)

		abel_title = ctk.CTkLabel(frame_addu, text="Create User")
		label_title_add = ctk.CTkLabel(frame_addu, text="Create User")
		label_title_add.pack(expand=1,pady=10)

		username_add = ctk.CTkEntry(frame_addu, placeholder_text="Enter Username")
		username_add.pack(pady=2, padx=10, expand=1)

		password_add = ctk.CTkEntry(frame_addu, placeholder_text="Enter Password", show=constPasswordHolder)
		password_add.pack(pady=2, padx=10, expand=1)

		checkbox_var = tk.IntVar()

		checkbox = tk.Checkbutton(frame_addu, text="root user", variable=checkbox_var)
		checkbox.pack(pady=20)

		btn_add = ctk.CTkButton(frame_addu, text="Create User", command=create_new_user)
		btn_add.pack(pady=10,padx=10)

		add_user_win.mainloop()

	#APP PREFS
	ctk.set_appearance_mode("dark") 
	ctk.set_default_color_theme("dark-blue")

	#home WINDOW DEFINITIONS

	home = ctk.CTk()
	home.title("--Login--")
	home.geometry("800x640")

	home.bind("<Return>", onSubmit)

	main_frame = ctk.CTkFrame(home)
	main_frame.pack(fill=tk.BOTH, expand=1)

	#WINDOW CONTENT

	content_frame = ctk.CTkFrame(main_frame, width=440, height=440, fg_color=customColor1)
	content_frame.pack(expand=1, anchor="center")

	label_title = ctk.CTkLabel(content_frame, text="Login Page")
	label_title.pack(expand=1, pady=10)

	label_authStat = ctk.CTkLabel(content_frame, text="Invalid Credentials", text_color="red")

	username_Textbox = ctk.CTkEntry(content_frame, placeholder_text="Enter Username")
	username_Textbox.pack(pady=2, padx=10, expand=1)

	password_Textbox = ctk.CTkEntry(content_frame, placeholder_text="Enter Password", show=constPasswordHolder)
	password_Textbox.pack(pady=2, padx=10, expand=1)

	global show_password_button
	show_password_button = ctk.CTkButton(content_frame, text="Show Password", command=show_password)
	show_password_button.pack(pady=2)

	btn1 = ctk.CTkButton(content_frame, text="Login", command=onSubmit)
	btn1.pack(pady=10,padx=10)

	btn2 = ctk.CTkButton(content_frame, text="Create User", command=add_user).pack(pady=(0,25))

	home.mainloop()



if __name__ == "__main__":
	mainLogin()