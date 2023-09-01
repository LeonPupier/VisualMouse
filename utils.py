# Dependencies
import numpy as np

# Globals variables
GAP			= 30

# Colors (B,G,R)
BLACK		= (0, 0, 0)
WHITE		= (255, 255, 255)
RED         = (0, 0, 255)

# Colors for HSV mask
LOWER_RED	= np.array([136, 87, 111], np.uint8)
UPPER_RED	= np.array([180, 255, 255], np.uint8)

LOWER_GREEN	= np.array([25, 52, 72], np.uint8)
UPPER_GREEN	= np.array([102, 255, 255], np.uint8)

LOWER_BLUE	= np.array([94, 80, 2], np.uint8)
UPPER_BLUE	= np.array([120, 255, 255], np.uint8)
