from webdeck_custom_module import *

import psutil
from pypresence import Presence
import time
import threading


webdeck = WebDeckAddon("DiscordTools")
command1 = webdeck.define_command(name='RichPresence Toggle', description='Toggle the Discord RPC')
command1.button.button_names.en = "Discord RPC"
command1.button.button_names.fr = "Discord RPC"
command1.button.image = "rpc_icon.png"

rpc_toggle = False
start_time = time.time()

RPC = Presence("1223210717126201385", pipe=0)



@command1.make
def toggle_rich_presence():
    global rpc_toggle
    global RPC
    global start_time
    while rpc_toggle:
        RPC.update(details=f"CPU: {str(round(psutil.cpu_percent(), 1))}%",
                state=f"RAM: {str(round(psutil.virtual_memory().percent, 1))}%",
                large_image="webdeck_icon",
                large_text="Webdeck, THE StreamDeck alternative.",
                start=start_time,
                buttons=[{"label": "WebDeck (Free StreamDeck)", "url": "https://github.com/Lenochxd/WebDeck"}])
        print("DiscordTools: Discord RichPresence updated!")
        time.sleep(15)

    if not rpc_toggle:
        print("DiscordTools: Discord RichPresence toggled to True!")
        rpc_toggle = True
        RPC.connect()
        print("DiscordTools: Discord RichPresence started!")
    else:
        print("DiscordTools: Discord RichPresence toggled to False!")
        rpc_toggle = False
        RPC.close()
        print("DiscordTools: Closed RichPresence connection!")