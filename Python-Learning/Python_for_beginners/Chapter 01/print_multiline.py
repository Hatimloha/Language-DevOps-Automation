# By using 3 qutos inside the print brecket help in printing multipe line through single command.

print('''
In networking, a bridge is a device that connects and filters traffic between two or more network segments, allowing them to communicate as if they were a single network. 

It operates primarily at the data link layer (Layer 2) of the OSI model. Here’s a breakdown of what a bridge does:

Segmentation: A bridge can divide a large network into smaller, more manageable segments, which can reduce network congestion. It helps in isolating traffic to specific segments, which can improve overall network performance.

Filtering: Bridges use MAC (Media Access Control) addresses to determine if a frame should be forwarded or filtered. When a frame arrives, the bridge checks its MAC address and forwards it only to the segment where the destination device resides. This helps in reducing unnecessary traffic on other network segments.

Learning: Bridges maintain a MAC address table (or forwarding table) that keeps track of which devices are on which segments. As they receive frames, they learn the MAC addresses of devices and their associated segments, which helps in making more efficient forwarding decisions.

Forwarding: When a bridge receives a frame, it uses its MAC address table to decide whether to forward the frame to another segment or to drop it if it's not necessary.

Compatibility: Bridges are used to connect networks that might use different types of network technologies or protocols, ensuring seamless communication between them.

Overall, bridges play a crucial role in optimizing and managing network traffic, enhancing performance, and facilitating the growth and integration of network segments.
''')
