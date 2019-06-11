from __future__ import absolute_import, division, print_function, unicode_literals

# import matplotlib.pylab as plt
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub

from tensorflow.keras import layers

print(tf.VERSION)
print(tf.keras.__version__)

data = [
	('1_banana_room_3days.jpg', 	'banana', 'room', 3, 30),
	# ('2_banana_room_4days.jpg', 	'banana', 'room', 4, 40),
	# ('3_banana_room_6days.jpg', 	'banana', 'room', 6, 60),
	# ('4_banana_room_7days.jpeg', 	'banana', 'room', 7, 70),
	# ('5_banana_room_7days.jpg', 	'banana', 'room', 7, 70),
	# ('6_banana_room_2days.jpg', 	'banana', 'room', 2, 20),
	# ('7_banana_room_3days.jpg', 	'banana', 'room', 3, 30),
	# ('8_banana_room_5days.jpg', 	'banana', 'room', 5, 50),
	# ('9_banana_room_0days.jpg', 	'banana', 'room', 0, 0),
	# ('10_banana_room_0days.jpg', 	'banana', 'room', 0, 0),
	# ('11_banana_room_-1days.jpg', 	'banana', 'room', -1, -10),
	# ('12_banana_room_-1days.jpg', 	'banana', 'room', -1, -10),
	# ('13_banana_fridge_4days.png', 	'banana', 'fridge', 4, 40),
	# ('14_banana_fridge_3days.jpg', 	'banana', 'fridge', 3, 30),
	# ('15_banana_fridge_-1days.jpg', 'banana', 'frdige', -1, -10),
	# ('16_banana_fridge_4days.jpg', 	'banana', 'fridge', 4, 40)
]

filenames = tf.constant([ i[0] for i in data ])
fruit_labels = tf.constant([ i[1] for i in data ])
storage_labels = tf.constant([ i[2] for i in data ])
lifespan_labels = tf.constant([ i[3] for i in data ])

dataset = tf.data.Dataset.from_tensor_slices((filenames, fruit_labels))

def preprocess_image(image):
  image = tf.image.decode_jpeg(image, channels=3)
  image = tf.image.resize(image, [192, 192])
  image /= 255.0  # normalize to [0,1] range
  return image

def load_and_preprocess_image(path):
  image = tf.read_file(path)
  print(image)
  return preprocess_image(image)

def _parse_function(filename, label):
	image_string = tf.read_file('dataset/' + filename)
	image_decoded = tf.image.decode_jpeg(image_string, channels=3)
	image = tf.cast(image_decoded, tf.float32)
	return image
# 	return (image,label)

img_path = '/Users/treziapov/Dropbox/cs221/project/dataset/banana/10_banana_room_0days.jpg'
tf.read_file(img_path)
image = _parse_function(img_path, 'banana')
print(image)

plt.imshow(image)
plt.grid(False)
plt.xlabel(caption_image(img_path))
print()


# dataset = dataset.map(load_and_preprocess_image)
# dataset = dataset.batch(2)

plt.figure(figsize=(8,8))
for n,image in enumerate(dataset.take(4)):
  plt.subplot(2,2,n+1)
  plt.imshow(image)
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  plt.xlabel(caption_image(all_image_paths[n]))
  plt.show()


# iterator = dataset.make_one_shot_iterator()
# for images,labels in iterator:
# 	print(labels)