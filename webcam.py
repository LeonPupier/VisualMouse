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
		self.left_click_hold = 0
		self.right_click_hold = 0
		self.gap_hold = 15

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

		# Get the pointer position
		x = self.x_pointer - self.webcam_width / 2
		y = self.y_pointer - self.webcam_height / 2

		# Correct the pointer position
		x = x * self.screen_width / (self.webcam_width * 0.7)
		y = y * self.screen_height / (self.webcam_height * 0.7)

		# Set the pointer position
		x = x + self.screen_width / 2
		y = y + self.screen_height / 2

		# Move the mouse pointer
		try:
			pyautogui.moveTo(x, y, duration=0, _pause=False)

			# Reset the pointer security
			self.security_out_of_screen = True
		except (pyautogui.FailSafeException):
			return
	

	def leftClick(self):
		# Simulate a left click
		if not self.left_click:
			pyautogui.click(button="left", _pause=False)
		
		# Simulate a left click hold
		else:
			if self.left_click_hold >= self.gap_hold:
				pyautogui.mouseDown(button="left", _pause=False)
			self.left_click_hold += 1
	

	def	leftUp(self):
		self.left_click_hold = 0
		pyautogui.mouseUp(button="left", _pause=False)


	def rightClick(self):
		# Simulate a right click
		if not self.right_click:
			pyautogui.click(button="right", _pause=False)
		
		# Simulate a right click hold
		else:
			if self.right_click_hold >= self.gap_hold:
				pyautogui.mouseDown(button="right", _pause=False)
			self.right_click_hold += 1
	

	def rightUp(self):
		self.right_click_hold = 0
		pyautogui.mouseUp(button="right", _pause=False)


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
