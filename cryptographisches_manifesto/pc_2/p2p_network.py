import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from p2p_node import MyOwnPeer2PeerNode

node_2 = MyOwnPeer2PeerNode("172.17.0.3", 8002, 2)


time.sleep(1)

node_2.start()


time.sleep(1)

debug = False
node_2.debug = debug



node_2.connect_with_node('172.17.0.2', 8001)


time.sleep(2)

node_2.send_to_nodes("message: Hi there! I am PC2, yo")

time.sleep(2)

print("node 2 is stopping..")

time.sleep(30)

node_2.stop()

print('end test')