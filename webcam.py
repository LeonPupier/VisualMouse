# Dependencies
import cv2, pyautogui
import numpy as np
from threading import Thread

from utils import *


# Webcam class
class Webcam:
	def __init__(self, dev_mode) -> None:
		self.dev_mode = dev_mode

		# Initialize the webcam
		self.title = "My Webcam"
		self.webcam = None
		self.state = None
		self.frame = None
		self.webcam_width = 0
		self.height = 0

		# Initialize the pointer
		self.stopped = False
		self.x_pointer = 0
		self.y_pointer = 0
		self.kernel = np.ones((5, 5), "uint8")

		# Screen informations
		self.screen_width, self.screen_height = pyautogui.size()

		# Get the webcam
		self.webcam = cv2.VideoCapture(0)
		self.webcam_width = self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.webcam_height = self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)


	def __del__(self) -> None:
		# Release the webcam
		self.stopped = True
		cv2.destroyAllWindows()
		if self.webcam is not None:
			self.webcam.release()
	

	def initMouse(self):
		# Thread to move the mouse pointer
		thread = Thread(target=self.moveMouse)
		thread.start()


	def launch(self) -> bool:
		while True:
			# Check if the webcam is opened correctly and get the frame
			try:
				self.state, self.frame = self.webcam.read()
			except KeyboardInterrupt:
				print("\n[EXIT] Keyboard interrupt detected.")
				self.stopped = True
				break

			if not self.state:
				print("\n[WARNING] Cannot get frame from the webcam.")
				self.stopped = True
				return (False)

			# Flip the frame and convert it to HSV
			self.frame = cv2.flip(self.frame, 1)
			hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

			# Colors masks
			range_mask = cv2.inRange(hsvFrame, LOWER_RED, UPPER_RED)
			mask = cv2.dilate(range_mask, self.kernel)

			# Creating contour to track the color
			contours = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

			# Find and draw the most important contour
			if len(contours) > 0:
				contour = max(contours, key=cv2.contourArea)
				area = cv2.contourArea(contour)
				if area > 300:
					x, y, w, h = cv2.boundingRect(contour)
					self.frame = cv2.rectangle(self.frame, (x, y), (x + w, y + h), RED, 1)
					cv2.putText(self.frame, "POINTER", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED)

					# Save the pointer position to track the movement later
					self.x_pointer = x
					self.y_pointer = y

			if self.dev_mode:
				# Display the frame
				cv2.imshow(self.title, self.frame)

			# Get the key pressed
			if cv2.waitKey(1) in [27]:
				self.stopped = True
				break

		return (True)


	def moveMouse(self):
		while not self.stopped:
			# Correction of the pointer position to match the screen size
			x = int(self.x_pointer * self.screen_width / self.webcam_width)
			y = int(self.y_pointer * self.screen_height / self.webcam_height)

			# Move the mouse pointer
			if 0 < x < self.screen_width and 0 < y < self.screen_height:
				pyautogui.moveTo(x, y, duration=0)
