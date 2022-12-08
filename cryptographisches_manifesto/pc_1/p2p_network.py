import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from p2p_node import MyOwnPeer2PeerNode

node_1 = MyOwnPeer2PeerNode("172.17.0.2", 8001, 1)


time.sleep(1)

node_1.start()


time.sleep(1)

debug = False
node_1.debug = debug



node_1.connect_with_node('172.17.0.3', 8002)


time.sleep(2)

node_1.send_to_nodes("message: Hi there! I am PC1")

time.sleep(2)

print("node 1 is stopping..")

time.sleep(30)

node_1.stop()

print('end test')