import face_recognition

image = face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations = face_recognition.face_locations(image)

# Array of coords of each face. Each face coord will have top, right, bottom, left
# print(face_locations)

# Number of people in a picture
print(f'There are {len(face_locations)} people in this image')