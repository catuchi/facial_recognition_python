import face_recognition

image_of_jordan = face_recognition.load_image_file('./img/known/Michael Jordan.jpg')
jordan_face_encoding = face_recognition.face_encodings(image_of_jordan)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/jordan-basketball.jpeg')
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

# print(jordan_face_encoding)

# compare faces
results = face_recognition.compare_faces([jordan_face_encoding], unknown_image_encoding)[0]

# print(results)

if results:
  print('This is Micheal Jordan')
else:
  print('This is not Micheal Jordan')