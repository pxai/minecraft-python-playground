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
playerName = "josu"
myId = mc.getPlayerEntityId(playerName);
pos = mc.entity.getPos(myId)



for i in range(0,5):
    mc.setEntity(pos.x, pos.y, pos.z, entity.WITHER_SKULL)

for i in range(0,1):
    mc.setEntity(pos.x, pos.y, pos.z, entity.WITHER)

for i in range(0,1):
    mc.setEntity(pos.x, pos.y, pos.z, entity.ENDER_DRAGON)

mc.postToChat('Animals created.')
