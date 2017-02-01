# Socket.py
A socket is effectively a type of file handle, behind which can lie a network session.
You can read and write it (mostly) like any other file handle and have the data go to and come from the other end of the session.

The specific actions you're describing are for the server end of a socket. A server establishes (binds to) a socket which can be used to accept incoming connections. Upon acceptance, you get another socket for the established session so that the server can go back and listen on the original socket for more incoming connection.

How they're represented in memory varies depending on your abstraction level.

At the lowest level in C, they're just file descriptors, a small integer. However, you may have a higher-level Socket class which encapsulates the behaviour of the low-level socket.

-paxdiablo, "http://stackoverflow.com/questions/16233193/what-exactly-is-socket?answertab=oldest#tab-top"
