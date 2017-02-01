# helloworld.py
# Simple code to set one block
import mcpi.minecraft as minecraft
import mcpi.block as block

# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')
mc = minecraft.Minecraft.create()

# Get your id
playerName = "PUT_YOUR_PLAYER_NAME!!!"
myId = mc.getPlayerId(playerName);
pos = mc.entity.getPos(myId)

mc.postToChat('Hello World')
