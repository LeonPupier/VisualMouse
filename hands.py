# Dependencies
import cv2
import mediapipe as mp

from utils import *


# Webcam class
class Hands:
	def __init__(self, webcam, static_image_mode=False, max_num_hand=1, min_detection_confidence=0.5, model_complexity=1, min_tracking_confidence=0.9):
		# Initialize the webcam
		self.webcam = webcam

		# Initialize the algorithm
		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(static_image_mode, max_num_hand, model_complexity, min_detection_confidence,min_tracking_confidence)
		self.mpDraw = mp.solutions.drawing_utils


	def __del__(self) -> None:
		# Release the hands detection algorithm memory
		self.hands.close()


	def handsDetector(self) -> None:
		# Convert the frame to RGB
		imageRGB = cv2.cvtColor(self.webcam.frame, cv2.COLOR_BGR2RGB)

		# Process the image to detect the hands
		results = self.hands.process(imageRGB)

		# Draw the hands landmarks
		if results.multi_hand_landmarks:
			for handLms in results.multi_hand_landmarks:
				# Draw the landmarks if the dev mode is enabled
				if self.webcam.dev_mode:
					self.mpDraw.draw_landmarks(self.webcam.frame, handLms, self.mpHands.HAND_CONNECTIONS)

				# Follow the thumb to move the mouse pointer
				thumb_position = results.multi_hand_landmarks[0].landmark[self.mpHands.HandLandmark.THUMB_TIP]
				self.webcam.x_pointer = thumb_position.x * self.webcam.webcam_width
				self.webcam.y_pointer = thumb_position.y * self.webcam.webcam_height
				self.webcam.security_out_of_screen = False

				# Detect if the middle finger is closed (Left click)
				middle_finger_position = results.multi_hand_landmarks[0].landmark[self.mpHands.HandLandmark.MIDDLE_FINGER_TIP]
				if middle_finger_position.y < thumb_position.y:
					self.webcam.left_click = False
					self.webcam.leftUp()
				else:
					self.webcam.leftClick()
					self.webcam.left_click = True

				# Detect if the index finger is closed (Right click)
				index_finger_position = results.multi_hand_landmarks[0].landmark[self.mpHands.HandLandmark.INDEX_FINGER_TIP]
				if index_finger_position.y < thumb_position.y:
					self.webcam.right_click = False
					self.webcam.rightUp()
				else:
					self.webcam.rightClick()
					self.webcam.right_click = True


	def algorithm(self) -> bool:
		while True:
			# Get the frame from the webcam
			if not self.webcam.getFrame():
				return (False)
			
			# Hand tracking
			self.handsDetector()

			# Move the mouse pointer
			self.webcam.moveMouse()

			# Show the frame
			if not self.webcam.showFrame():
				break

		return (True)
