
import utils
import asyncio

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()



if __name__ == '__main__':
    address = utils.parse_command_line('client')
    loop = asyncio.get_event_loop()
    message = input('Enter your message to server: ')
    coro = loop.create_connection(lambda: EchoClientProtocol(message, loop), address[0] , address[1])
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
