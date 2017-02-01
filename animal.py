# block.py
# Simple code to set one block
import mcpi.minecraft as minecraft
import mcpi.entity as entity
import time as time

# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')
mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)

# Get your id
playerName = "PUT_YOUR_PLAYER_NAME!!!"
myId = mc.getPlayerId(playerName);
pos = mc.entity.getPos(myId)

# Set the entity
mc.setEntity(pos.x, pos.y, pos.z, entity.OCELOT)

mc.postToChat('He puesto un bicho, uoooo')
