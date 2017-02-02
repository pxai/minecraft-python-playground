# getPlayersInfo.py
# Simple code to show a message in the chat
import mcpi.minecraft as minecraft

# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')
mc = minecraft.Minecraft.create()

# Get players info
players = mc.getPlayerEntityIdsAndNames();

for player in players:
    print player