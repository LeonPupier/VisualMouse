# Dependencies
import sys

from utils import *
from webcam import Webcam
from hands import Hands


def launch() -> bool:
	# Check if the program is in dev mode
	dev_mode = False
	for arg in sys.argv:
		if arg == "--dev":
			dev_mode = True

	# Initialize the webcam
	webcam = Webcam(dev_mode)

	# Initialize the algorithm
	hands = Hands(webcam)
	state = hands.algorithm()

	# Destroy objects
	del hands
	del webcam

	return (state)


# Launch the program
if __name__ == "__main__":
	state = launch()

	if not state:
		exit(1)