# block.py
# Simple code to set one block
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')
mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

# Get your id
playerName = "PUT_YOUR_PLAYER_NAME!!!"
myId = mc.getPlayerEntityId(playerName);
pos = mc.entity.getPos(myId)

# Set the block
mc.setBlock(pos.x, pos.y, pos.z, block.GOLD_BLOCK)

mc.postToChat('He puesto un bloque, uoooo')

#for i in range(0,20):
#	mc.setBlock(pos.x,pos.y+i,pos.z,block.GOLD_BLOCK)