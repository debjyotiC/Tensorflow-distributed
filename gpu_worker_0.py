import sys
import json
import tensorflow as tf
task_number = int(sys.argv[1])

with open('cluster_spec/clusterspec.json', 'r') as f:
    cluster_spec = json.load(f)

cluster = tf.train.ClusterSpec(cluster_spec)
server = tf.train.Server(cluster, job_name="worker", task_index=task_number)

print("Starting server #{}".format(task_number))

server.start()
server.join()
