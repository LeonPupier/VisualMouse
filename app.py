# Dependencies
import customtkinter, sys
from threading import Thread

from utils import *
from webcam import Webcam
from hands import Hands

# Set the appearance mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Window class
class App(customtkinter.CTk):
	def __init__(self) -> None:
		# Check if the program is in dev mode
		self.dev_mode = False
		for arg in sys.argv:
			if arg == "--dev":
				self.dev_mode = True

		# Initialize the window
		super().__init__()
		self.geometry("300x65")
		self.title("VisualMouse")
		self.resizable(False, False)
		self.protocol("WM_DELETE_WINDOW", self.on_closing)
		center_window(self)

		# Fonts
		self.bold_font = customtkinter.CTkFont(size=13, weight='bold')
		self.main_font = customtkinter.CTkFont(size=13)
		self.copyright_font = customtkinter.CTkFont(size=9, slant='italic')

		# Text of the current state of the program execution
		self.frame = customtkinter.CTkFrame(self)
		self.frame.grid(row=0, column=0, padx=10, pady=5)
		self.label_state = customtkinter.CTkLabel(self.frame, font=self.main_font)

		# Initialize the buttons
		self.button = customtkinter.CTkButton(self, width=80, command=self.pause)

		# Informations text
		self.label_info = customtkinter.CTkLabel(self, text=f"{VERSION} by Léon Pupier", font=self.copyright_font, text_color="grey", width=0, height=0)
		self.label_info.place(x=10, y=self.winfo_height() - 10, anchor="w")

		# Text to exit the program
		self.label_exit = customtkinter.CTkLabel(self.frame, font=self.main_font, text="Do you want to exit ?")

		# Buttons to exit the program
		self.button_yes = customtkinter.CTkButton(self, text="Yes", width=65, command=self.exit)
		self.button_no = customtkinter.CTkButton(self, text="No", width=65, command=self.show)

		# Initialize the webcam
		self.webcam = None

		# Initialize the algorithm
		self.hands = None
		self.algo_thread = None

		# Show the window
		self.show()

		# Start the algorithm
		self.resume()

		# Initialize the window loop
		self.mainloop()
	

	def __del__(self) -> None:
		# Destroy objects
		if self.hands:
			del self.hands
		if self.webcam:
			del self.webcam
	

	def show(self) -> None:
		# Hide the exit widgets
		self.label_exit.pack_forget()
		self.button_yes.grid_forget()
		self.button_no.grid_forget()

		# Show the widgets
		self.label_state.pack(padx=10, pady=5)
		self.button.grid(row=0, column=1)


	def pause(self) -> None:
		# Wait the end of the algorithm thread
		self.hands.paused = True
		self.algo_thread.join()

		# Destroy the objects
		del self.hands
		del self.webcam
		self.hands = None
		self.webcam = None

		# Pause the program
		self.button.configure(text="Resume", command=self.resume)
		self.label_state.configure(text="State of VisualMouse: Paused")


	def resume(self) -> None:
		# Initialize the webcam
		self.webcam = Webcam(self.dev_mode)

		# Initialize the algorithm
		self.hands = Hands(self.webcam)
		self.hands.paused = False
		
		# Restart the algorithm
		self.algo_thread = Thread(target=self.hands.algorithm)
		self.algo_thread.start()

		# Resume the program
		self.button.configure(text="Pause", command=self.pause)
		self.label_state.configure(text="State of VisualMouse: Running")


	def on_closing(self) -> None:
		# Pack forget the widgets
		self.label_state.pack_forget()
		self.button.grid_forget()

		self.label_exit.pack(padx=10, pady=5)
		self.button_yes.grid(row=0, column=1)
		self.button_no.grid(row=0, column=2, padx=5)
	

	def exit(self) -> None:
		# Wait the end of the algorithm thread
		if self.hands:
			self.hands.paused = True
			self.algo_thread.join()

		# Destroy the window
		self.destroy()
		exit(0)
		

# Launch the app
if __name__ == "__main__":
	App()
