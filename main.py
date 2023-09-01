# Dependencies
import sys

from webcam import Webcam

# Main function
if __name__ == '__main__':
	# Check the arguments passed to the program
	dev_mode = False
	for arg in sys.argv:
		if arg == "-dev":
			dev_mode = True

	# Initialize the webcam
	webcam = Webcam(dev_mode)

	# Launch the algorithm
	webcam.initMouse()
	state = webcam.launch()

	# Destroy the webcam
	del webcam

	# Exit the program
	if not state:
		exit(1)
