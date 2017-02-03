sess = tf.Session()
# operacja zainicjowania zmiennych
init = tf.global_variables_initializer()
sess.run(init)

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print(sess.run(classes, feed_dict={x: mnist.test.images}))
