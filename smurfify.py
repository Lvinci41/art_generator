import cv2 as cv
import matplotlib.pyplot as plt

def smurfify(img):
    return img[:,:,[2,1,0]]

def cv2_imshow(img):
  plt.figure(figsize=(18,18))
  plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
  plt.axis('off')
  plt.show()

path = 'C:\\Users\\Luke\\Documents\\Projects\\Popart' #C:\Users\Luke\Documents\Projects\Popart
filename = "IMG_2552_val.PNG"

img = cv.imread(filename)

smurf = smurfify(img)
cv2_imshow(smurf)