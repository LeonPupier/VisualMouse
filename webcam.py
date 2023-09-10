# Dependencies
import cv2, pyautogui

from utils import *

# Webcam class
class Webcam:
	def __init__(self, dev_mode) -> None:
		self.dev_mode = dev_mode

		# Initialize the webcam
		self.title = "My Webcam"
		self.webcam = cv2.VideoCapture(0)
		self.webcam_width = self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.webcam_height = self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)
		self.frame = None

		# Init the mouse pointer
		self.stopped = False
		self.security_out_of_screen = True
		self.x_pointer = 0
		self.y_pointer = 0
		
		# Init the mouse click
		self.left_click = False
		self.right_click = False

		# Screen informations
		self.screen_width, self.screen_height = pyautogui.size()


	def __del__(self) -> None:
		# Release the webcam
		self.stopped = True
		cv2.destroyAllWindows()
		if self.webcam is not None:
			self.webcam.release()


	def moveMouse(self) -> None:
		# Check if the pointer is out of the screen
		if self.security_out_of_screen:
			return

		# Correction of the pointer position to match the screen size
		x = int(self.x_pointer * self.screen_width / self.webcam_width)
		y = int(self.y_pointer * self.screen_height / self.webcam_height)

		# Move the mouse pointer
		pyautogui.moveTo(x, y, duration=0, _pause=False)
		
		# Reset the pointer security
		self.security_out_of_screen = True
	

	def leftClick(self):
		# Simulate a left click
		if not self.left_click:
			pyautogui.mouseDown(button="left", _pause=False)
			pyautogui.click(button="left", _pause=False)
		
		# Simulate a left click hold
		else:
			pyautogui.mouseDown(button="left", _pause=False)

	
	def rightClick(self):
		# Simulate a right click
		if not self.right_click:
			pyautogui.mouseUp(button="right", _pause=False)
			pyautogui.click(button="right", _pause=False)
		
		# Simulate a right click hold
		else:
			pyautogui.mouseDown(button="right", _pause=False)


	def getFrame(self) -> bool:
		# Check if the webcam is opened correctly and get the frame
		state, frame = self.webcam.read()

		if not state:
			print(f"\n{output.FAIL}[ERROR]{output.END} Cannot get frame from the webcam.")
			self.stopped = True
			return (False)
	
		# Flip the frame
		self.frame = cv2.flip(frame, 1)

		# Mark the frame as read only
		self.frame.flags.writeable = False

		return (True)
	

	def showFrame(self) -> bool:
		# Display the frame
		if self.dev_mode:
			cv2.imshow(self.title, self.frame)

		# Get the key pressed
		if cv2.waitKey(1) in [27]:
			self.stopped = True
			return (False)
	
		return (True)
