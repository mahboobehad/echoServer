import asyncio, utils

class Server(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))

        elif self.data:
            print('Client {} sent {} but then closed'.format(self.address, self.data))
        else:
            print('Client {} closed socket'.format(self.address))

if __name__ == '__main__':
    address = utils.parse_command_line('Echo server')
    loop = asyncio.get_event_loop()
    coro = loop.create_server(Server, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
