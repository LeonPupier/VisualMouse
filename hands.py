# Dependencies
import cv2
import mediapipe as mp

from utils import *

import pyautogui


# Webcam class
class Hands:
	def __init__(self, webcam, mode=False, maxHands=2, detectionCon=0.5, modelComplexity=1, trackCon=0.5):
		# Initialize the webcam
		self.webcam = webcam

		# Initialize the algorithm
		self.mode = mode
		self.maxHands = maxHands
		self.detectionCon = detectionCon
		self.modelComplex = modelComplexity
		self.trackCon = trackCon
		self.mpHands = mp.solutions.hands
		self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex, self.detectionCon, self.trackCon)
		self.mpDraw = mp.solutions.drawing_utils

		# Init the models
		self.models_path = 'Models/gesture_recognizer.task'


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

				# Detect what hand is used
				left_hand = False
				right_hand = False
				if results.multi_handedness:
					for hand_handedness in results.multi_handedness:
						if hand_handedness.classification[0].label == "Left":
							left_hand = True
						elif hand_handedness.classification[0].label == "Right":
							right_hand = True
				
				# Detect the gestures
				if left_hand:
					# Follow the index finger with the mouse pointer
					finger_position = results.multi_hand_landmarks[0].landmark[self.mpHands.HandLandmark.INDEX_FINGER_TIP]
					self.webcam.x_pointer = finger_position.x * self.webcam.webcam_width
					self.webcam.y_pointer = finger_position.y * self.webcam.webcam_height
					self.webcam.security_out_of_screen = False


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
