# Dependencies
import customtkinter
from PIL import Image
from threading import Thread

from utils import *
from app import App

# Set the appearance mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Window class
class Tutorial(customtkinter.CTk):
	def __init__(self):
		# Initialize the window
		super().__init__()
		self.geometry("500x600")
		self.title("VisualMouse - Movement start-up tutorial")
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.on_closing)
		center_window(self)

		# Fonts
		self.bold_font = customtkinter.CTkFont(size=13, weight='bold')
		self.main_font = customtkinter.CTkFont(size=13)
		self.copyright_font = customtkinter.CTkFont(size=9, slant='italic')

		# Drawing of the tutorial
		image_presentation = Image.open("Content/presentation.png")
		self.drawing_presentation = customtkinter.CTkImage(light_image=image_presentation, dark_image=image_presentation, size=(400, 400))

		image_movement = Image.open("Content/movement.png")
		self.drawing_movement = customtkinter.CTkImage(light_image=image_movement, dark_image=image_movement, size=(400, 400))

		image_left = Image.open("Content/left.png")
		self.drawing_left = customtkinter.CTkImage(light_image=image_left, dark_image=image_left, size=(400, 400))

		image_right = Image.open("Content/right.png")
		self.drawing_right = customtkinter.CTkImage(light_image=image_right, dark_image=image_right, size=(400, 400))

		self.frame_drawing = customtkinter.CTkFrame(self)
		self.frame_drawing.pack(expand=True, fill="both", padx=10, pady=10)
		self.label_drawing = customtkinter.CTkLabel(self.frame_drawing, text="")
		self.label_drawing.pack(expand=True, fill="both", padx=10, pady=10)

		# Text of the current step in the tutorial
		self.label_step = customtkinter.CTkLabel(self, font=self.bold_font)
		self.label_step.pack(pady=5)

		# Text of the current step in the tutorial
		self.frame = customtkinter.CTkFrame(self)
		self.frame.pack()
		self.label_explanation = customtkinter.CTkLabel(self.frame, font=self.main_font)
		self.label_explanation.pack(padx=10, pady=5)

		# Initialize the buttons
		self.button = customtkinter.CTkButton(self)
		self.button.pack(pady=15)

		# Informations text
		self.label_info = customtkinter.CTkLabel(self, text=f"{VERSION} by Léon Pupier", font=self.copyright_font, text_color="grey")
		self.label_info.place(x=495, y=590, anchor="e")

		# Launch the tutorial
		self.opening()

		# Initialize the window loop
		self.mainloop()
	

	def opening(self):
		self.label_drawing.configure(image=self.drawing_presentation)
		self.label_step.configure(text="Welcome to VisualMouse !", font=self.bold_font)
		self.label_explanation.configure(text="This is a tutorial to help you understand how to use VisualMouse. The right hand is taken as an example.", wraplength=380)
		self.button.configure(text="Begin →", command=self.step_1)
	

	def step_1(self):
		self.label_drawing.configure(image=self.drawing_movement)
		self.label_step.configure(text="1/3")
		self.label_explanation.configure(text="To move the mouse on the screen, you can move your hand. The pointer follows your thumb.", wraplength=400)
		self.button.configure(command=self.step_2)

	
	def step_2(self):
		self.label_drawing.configure(image=self.drawing_left)
		self.label_step.configure(text="2/3")
		self.label_explanation.configure(text="To simulate a left mouse click, you need to lower the tip of your index.", wraplength=400)
		self.button.configure(command=self.step_3)

	
	def step_3(self):
		self.label_drawing.configure(image=self.drawing_right)
		self.label_step.configure(text="3/3")
		self.label_explanation.configure(text="To simulate a right mouse click, you need to lower the tip of your middle finger.", wraplength=400)
		self.button.configure(text="Start now !", command=self.start)


	def on_closing(self):
		# Destroy the window
		self.destroy()
		exit(0)
	
	
	def start(self):
		# Destroy the window
		self.after_cancel(self)
		self.destroy()

		# Launch the app
		app_thread = Thread(target=App)
		app_thread.start()



# Launch the tutorial
if __name__ == "__main__":
	Tutorial()
