# Webcam
webcam_w = 600
webcam_h = 500

# Screen
screen_w = 1920
screen_h = 1080

# Pointer position
pointer_x = 60
pointer_y = 100

# Base les coordonnées de la webcam par apport a son centre
x = pointer_x - webcam_w / 2
y = pointer_y - webcam_h / 2

# Correction des coordonnées de la webcam par apport a la taille de l'écran
x = x * screen_w / (webcam_w * 0.8)
y = y * screen_h / (webcam_h * 0.8)

# Repasser les coordonnées en positif pour le deplacement souris
x = x + screen_w / 2
y = y + screen_h / 2

print(x)
print(y)