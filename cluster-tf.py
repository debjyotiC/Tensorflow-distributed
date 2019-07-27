import json
import tensorflow as tf

with open('cluster_spec/clusterspec.json', 'r') as f:
    clusterspec = json.load(f)

cluster = tf.train.ClusterSpec(clusterspec)

a = tf.constant(3.0)
b = tf.constant(2.0)

with tf.device("/job:worker/task:0"):
    x = tf.add(a, b)
    y = tf.multiply(a, b)
    z = x + y

with tf.compat.v1.Session('grpc://X.X.X.X:2222', config=tf.compat.v1.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run(z))

