# Consensus
## three nodes reach a conensus about the leader and the data.

There are three nodes that the "Node.py" runs on them.  
At first, they reach a consensus about the leader.
Then, they are ready to receive requests.
A node that runs the "Client.py" code communicates with these tree nodes.
It chooses a node randomly and sent an integer to it.
If the target node is the leader, it saves the integer.
If the target node is not the leader, it forwards data to the leader and the leader saves that integer.
the leader sends its data to other nodes when it has gotten 3 integers.

