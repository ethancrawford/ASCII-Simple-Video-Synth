import random
import time
from pythonosc import osc_message_builder
from pythonosc import udp_client


client=udp_client.SimpleUDPClient("127.0.0.1",8000)

dest = [
    "/red/scale",
    "/red/offset",
    "/red/speed",
    "/green/scale",
    "/green/offset",
    "/green/speed",
    "/blue/scale",
    "/blue/offset",
    "/blue/speed"
]

while True:
    val_set = random.randrange(0,255)
    dest_s = dest[random.randrange(0, len(dest))]

    client.send_message(dest_s,val_set)
    print("sent {} to {}".format(val_set,dest_s))

    time.sleep(1)
