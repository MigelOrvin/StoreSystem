import tkinter as tk
from PIL import Image, ImageTk


class LoginPage(tk.Frame):
	def __init__(self, parent, App):
		self.application = App
		self.settings = App.settings

		super().__init__(parent)
		self.configure(bg="blue")
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		#CREATE MAIN FRAME
		self.main_frame = tk.Frame(self, height=self.settings.height, width=self.settings.width, bg="blue")
		self.main_frame.pack(expand=True)

		self.label_username = tk.Label(self.main_frame, text="username", font=("Arial", 18, "bold"), bg="blue", fg="white")
		self.label_username.pack(pady=5)

		self.entry_username = tk.Entry(self.main_frame, font=("Arial", 16, "bold"))
		self.entry_username.pack(pady=5)

		self.label_password = tk.Label(self.main_frame, text="password", font=("Arial", 18, "bold"), bg="blue", fg="white")
		self.label_password.pack(pady=5)

		self.entry_password = tk.Entry(self.main_frame, font=("Arial", 16, "bold"), show="*")
		self.entry_password.pack(pady=5)

		self.btn_login = tk.Button(self.main_frame, text="LOGIN", font=("Arial", 18, "bold"), command=lambda:self.application.change_page("app_page"))
		self.btn_login.pack(pady=5)


