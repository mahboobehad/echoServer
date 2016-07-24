from socket import *
import argparse

def parse_command_line(description):

    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def recv_until(sock, suffix):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    socket.getpeername()
    message = sock.recv(1096)
    if not message:
     raise EOFError('socket closed')
    while not message.endswith(suffix):
     data = sock.recv(1096)
    if not data:
     raise IOError('received {!r} then socket closed'.format(message))
    message += data
    return message

#logging tools :-"