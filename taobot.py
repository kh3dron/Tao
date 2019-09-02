import os
import slack
import socket
import threading
import random

#My improvised way of not committing my API keys
with open ("../secrets.txt") as f:
    secrets = f.read().split("\n")

slack_token = secrets[0]
bot_user_token = secrets[1]

bind_ip = "192.168.1.73"
bind_port = 8100

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Ready on %s:%d" % (bind_ip, bind_port))

def get_tao():
    with open("formatted_tao.txt") as g:
        taos = g.read().splitlines()
    quote = (taos[random.randint(0, 663)])
    quote += "\n    _-from Ron Hogan's TAO.txt_"
    return quote

#I'm so sure there's a better way to do this
def get_term(raw, term):
    raw = raw.decode("utf-8")
    raw = raw.split("&")
    for r in raw:
        if term in r:
            r=r.split("=")
            print(r)
            return(r[1])


def make_post(channel):
    client = slack.WebClient(slack_token)
    response = client.chat_postMessage(
        channel=channel,
        text=get_tao())

#client-handling thread

def handle_client(client_socket):

    raw = client_socket.recv(1024)
    #print("[*] Recieved: %s" % raw)

    channel = get_term(raw, "channel_name")
    make_post(channel)

    print("Sent TAO to channel:" + channel)

    #send something back - need to figure this out. the thing works, but
    #I still get a timeout error, which is annoying
    client_socket.send({ "statusCode": 200})
    client_socket.close()

while True:

    client,addr = server.accept()
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
