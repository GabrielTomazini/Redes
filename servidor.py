import socket
import sys
from Classes import Barbarian
from Classes import Cleric
from Classes import Rogue
from Classes import Wizard


def main():
    socketConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ("127.0.0.1", 50000)
    socketConnection.bind(address)
    socketConnection.listen(1)


if __name__ == "__main__":
    main()
