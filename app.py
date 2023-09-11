# Dependencies
import customtkinter
from tkVideoPlayer import TkinterVideo
from PIL import Image

from main import launch
from utils import *

# Set the appearance mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Window class
class App(customtkinter.CTk):
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

		# Video	player
		self.frame_video = customtkinter.CTkFrame(self)
		self.video = None

		# Text of the current step in the tutorial
		self.label_step = customtkinter.CTkLabel(self, font=self.bold_font)

		# Text of the current step in the tutorial
		self.frame = customtkinter.CTkFrame(self)
		self.label_explanation = customtkinter.CTkLabel(self.frame, font=self.main_font)

		# Initialize the buttons
		self.button = customtkinter.CTkButton(self)

		# Informations text
		self.label_info = customtkinter.CTkLabel(self, text="[Dev Version] v0.0.1 by Leon Pupier", font=self.copyright_font, text_color="grey")
		self.label_info.place(x=495, y=590, anchor="e")

		# Launch the tutorial
		self.opening()

		# Initialize the loop
		self.loop()

		# Initialize the window loop
		self.mainloop()
	

	def opening(self):
		self.frame_video.pack(expand=True, fill="both", padx=10, pady=10)
		self.video = TkinterVideo(master=self.frame_video, scaled=True)
		self.video.configure(bg="#1A1A1A")
		self.video.load("Content/opening.mp4")
		self.video.play()
		self.video.pack(expand=True, fill="both", padx=10, pady=10)

		self.label_step.configure(text="Welcome to VisualMouse !", font=self.bold_font)
		self.label_step.pack(pady=5)
		
		self.label_explanation.configure(text="This is a tutorial to help you understand how to use VisualMouse.", wraplength=400)
		self.label_explanation.pack(padx=10, pady=5)
		self.frame.pack()
		
		self.button.configure(text="Begin →", command=self.step_1)
		self.button.pack(pady=15)


	def step_1(self):
		self.video.destroy()
		self.video.pack_forget()
		self.video = TkinterVideo(master=self.frame_video, scaled=True)
		self.video.configure(bg="#1A1A1A")
		self.video.load("Content/presentation.mp4")
		self.video.play()
		self.video.pack(expand=True, fill="both", padx=10, pady=10)

		self.label_step.configure(text="1/4")
		self.label_step.pack()
		
		self.label_explanation.configure(text="This is the best way to position your hand so that the programme understands your movements.", wraplength=450)
		self.label_explanation.pack(padx=10, pady=5)
		self.frame.pack()
		self.frame.pack()
		
		self.button.configure(text="Next →", command=self.step_2)
		self.button.pack(pady=15)
	

	def step_2(self):
		self.video.destroy()
		self.video.pack_forget()
		self.video = TkinterVideo(master=self.frame_video, scaled=True)
		self.video.configure(bg="#1A1A1A")
		self.video.load("Content/movement.mp4")
		self.video.play()
		self.video.pack(expand=True, fill="both", padx=10, pady=10)

		self.label_step.configure(text="2/4")
		self.label_explanation.configure(text="To move the mouse on the screen, you can move your hand. The pointer follows your thumb.", wraplength=400)
		
		self.button.configure(command=self.step_3)

	
	def step_3(self):
		self.video.destroy()
		self.video.pack_forget()
		self.video = TkinterVideo(master=self.frame_video, scaled=True)
		self.video.configure(bg="#1A1A1A")
		self.video.load("Content/left.mp4")
		self.video.play()
		self.video.pack(expand=True, fill="both", padx=10, pady=10)
		
		self.label_step.configure(text="3/4")
		self.label_explanation.configure(text="To simulate a left mouse click, you need to lower your middle finger as shown.", wraplength=400)
		
		self.button.configure(command=self.step_4)

	
	def step_4(self):
		self.video.destroy()
		self.video.pack_forget()
		self.video = TkinterVideo(master=self.frame_video, scaled=True)
		self.video.configure(bg="#1A1A1A")
		self.video.load("Content/right.mp4")
		self.video.play()
		self.video.pack(expand=True, fill="both", padx=10, pady=10)
		
		self.label_step.configure(text="4/4")
		self.label_explanation.configure(text="To simulate a right mouse click, you need to lower your index finger as shown.", wraplength=400)
		
		self.button.configure(text="Start now !", command=self.start)

	
	def loop(self):
		# Replay the video if it's the end
		try:
			if self.video.is_paused():
				self.video.play()
		except:
			pass
			
		# Loop method
		self.after(10, self.loop)


	def on_closing(self):
		# Destroy the window
		self.destroy()
		exit(0)
	
	
	def start(self):
		# Destroy the window
		self.destroy()

		state = launch()
		if not state:
			exit(1)
		exit(0)



# Launch the app
if __name__ == "__main__":
	App()
