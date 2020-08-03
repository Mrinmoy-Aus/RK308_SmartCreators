import face_recognition
from PIL import Image, ImageDraw
import numpy as np
import cv2
import os


def train_model():
	fn_dir = 'face_samples'
	print('Training...')
	(known_face_encodings,known_face_names, id) = ([], {}, 0)

	for (subdirs, dirs, files) in os.walk(fn_dir):
		for subdir in dirs:
			known_face_names[id] = subdir
			subjectpath = os.path.join(fn_dir, subdir)
			for filename in os.listdir(subjectpath):
				f_name, f_extension = os.path.splitext(filename)
				if(f_extension.lower() not in ['.png','.jpg','.jpeg','.gif','.pgm']):
					print("Skipping "+filename+", wrong file type")
					continue
				path = subjectpath + '/' + filename
				name_image = face_recognition.load_image_file(path)
				name_face_encoding = face_recognition.face_encodings(name_image)[0]

				known_face_encodings.append(name_face_encoding)
			id += 1

	#print(known_face_encodings)
	#print(known_face_names)
	return(known_face_names,known_face_encodings)

