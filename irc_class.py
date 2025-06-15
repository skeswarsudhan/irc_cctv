import socket
import sys
import time


class IRC:
    irc = socket.socket()

    def __init__(self):
        # Define the socket
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        # Transfer data
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port, channel, user, botpass, userpass):
        # Connect to the server
        print("Connecting to: " + server)
        self.irc.connect((server, port))

        # Perform user authentication
        self.irc.send(bytes("USER " + user + " " + user + " " + user + " :python\n", "UTF-8"))
        self.irc.send(bytes("NICK " + user + "\n", "UTF-8"))
        self.irc.send(bytes("NICKSERV IDENTIFY " + userpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        # join the channel
        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

