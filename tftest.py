import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

tf.compat.v1.disable_eager_execution()

x1 = tf.constant(5)
x2 = tf.constant(6)

result = tf.multiply(x1,x2)

print (result)


with tf.compat.v1.Session() as sess:
	output = sess.run(result)
	print(output)

print(output)