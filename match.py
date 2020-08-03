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

def detect_faces(frame):
	face_locations = face_recognition.face_locations(frame)
	#face_encodings = face_recognition.face_encodings(frame, face_locations)

	return face_locations

def recognize_face(frame, known_face_names,known_face_encodings):
	#pil_image = Image.fromarray(frame)
	#draw = ImageDraw.Draw(pil_image)
	face_locations = face_recognition.face_locations(frame)
	face_encodings = face_recognition.face_encodings(frame, face_locations)
	names = []
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

		name = "Unknown"

		face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
		best_match_index = np.argmin(face_distances)
		if matches[best_match_index]:
			name = known_face_names[best_match_index]
			names.append(name)
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
		cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
		font = cv2.FONT_HERSHEY_DUPLEX
		cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (0, 0, 0), 1)
		#pil_image.show()
	return names


(known_face_names,known_face_encodings) = train_model()
unknown_image = face_recognition.load_image_file("image5.jpg")
	
name = recognize_face(unknown_image,known_face_names,known_face_encodings)
listToStr = ' '.join(map(str, name)) 

print(listToStr)
