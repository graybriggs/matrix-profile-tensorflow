# Import libraries for simulation
import tensorflow as tf
import numpy as np
import random

x = np.random.rand(10000)

x = tf.constant(x, name='x')
y = tf.Variable(5 * x * x - 3 * x + 15, name='y')


def findNN(x, y)

    x = tf.constant(x, name='x')
    y = tf.constant(y, name='y')

    X = tf.Variable(tf.fft(x), name='X')
    Y = tf.Variable(tf.fft(y), name='Y')
    Z = X



model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))

