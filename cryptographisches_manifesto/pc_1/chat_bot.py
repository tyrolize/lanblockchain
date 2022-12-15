import sys
import time
sys.path.insert(0, '..') # Import the files where the modules are located

from p2p_node import MyOwnPeer2PeerNode

node = MyOwnPeer2PeerNode("172.17.0.2", 8080, 1)


time.sleep(5)

node.start()


time.sleep(5)

debug = False
node.debug = debug



node.connect_with_node('172.17.0.3', 8080)


time.sleep(5)

node.send_to_nodes("message: Hi there! I am PC1, yo")

while True:
    #send 1 message
    msg = input()
    if msg == "kill":
        break
    else:
        node.send_to_nodes(msg)

node.stop()