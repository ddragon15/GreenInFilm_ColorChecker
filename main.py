import numpy
import cv2
import msvcrt as m
import os

width = 720
height = 576



print ("Please put Videoclip in the Movie Folder")
input()
print ("Enter file name:")
input_name = input()
# print ("Please enter RGB value (like 255)")
# print ("Which RGB Value you want to check? (R G B)")
print ("To Which offset? (0-255 | 255 being pure channel")
print ("Warning: 50 is already a high value!")
color_offset = int(input())

filename = os.path.join('movie/' + input_name)

cv2.namedWindow("VideoSet")
cap = cv2.VideoCapture(filename)

# Progressbar
# framepercent = int(cap.)/100
# progress = 0

currentFrame = 0
cv2.destroyAllWindows()
while(True):
    # Capture frame-by-frame
	ret, frame = cap.read()

	for x in range((width-1)//16):
		for y in range((height-1)//16):
			#print("x=" + str(i), "y=" + str(j))
			p = frame[y*16,x*16]
			if p[1] > p[0]+color_offset and p[1] > p[2]+color_offset:#
				# Saves image of the current frame in jpg file
				name = './data/frame' + str(currentFrame) + '.jpg'
				# print ('Creating...  ' + name)
				# cv2.imshow(currentFrame, frame)
				cv2.imwrite(name, frame)
				break

	# To stop duplicate images
	# print ('Frame ' + str(currentFrame))
	# if (frame / framepercent > progress):
		# progress = frame / framepercent
		# print (progress)
	currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
