# Code from https://www.youtube.com/watch?v=PmZ29Vta7Vc
#Additional Tutorials
# https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale/
# https://www.pyimagesearch.com/2018/09/24/opencv-face-recognition/
import os
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainer.yml")


labels = {}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v : k for k,v in og_labels.items()}

filename = 'video.avi'
frames_per_second = 24.0
resolution = '720p'

cap = cv2.VideoCapture(0);

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def get_dims(cap, res='1080p'):
	width, height = STD_DIMENSIONS['480p']
	if res in STD_DIMENSIONS:
		width, height = STD_DIMENSIONS[res]
	change_res(cap, width, height)
	return width,height

# Standard Video Dimensions Sizes

dims = get_dims(cap, resolution)
video_type = get_video_type(filename)

#out = cv2.VideoWriter(filename, video_type, frames_per_second, dims)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

	for(x ,y, w, h) in faces:
		# print( x, y, w, h)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]


		id_, conf = recognizer.predict(roi_gray)
		if conf >= 45 and conf <= 85:
			print(id_)
			print(labels[id_])
			font = cv2.FONT_HERSHEY_SIMPLEX
			name=labels[id_]
			color = (255,255,255)
			stroke  = 2
			cv2.putText(frame, name, (x,y), font ,1, color, stroke, cv2.LINE_AA)
		
		img_item = "my-image.png"
		cv2.imwrite(img_item, roi_gray);
		#cv2.imwrite(img_item, roi_color);

		color = (255, 0, 0)
		stroke = 2
		end_cord_x = x + w
		end_cord_y = y + h
		cv2.rectangle(frame , ( x, y), (end_cord_x, end_cord_y), color, stroke)

	#out.write(frame)
	cv2.imshow('frame', frame)
	#cv2.imshow('gray', gray)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
#out.release();
cv2.destroyAllWindows()