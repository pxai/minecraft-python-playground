
# teleport.py
# Moves player to given position
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()
# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')

# Simple delay to see things
time.sleep(2)


# Get your id
myId = mc.getPlayerEntityId("june");
pos = mc.entity.getPos(myId)

josuId = mc.getPlayerEntityId("josu");
posJosu = mc.entity.getPos(josuId)

# Show your position
mc.postToChat("My position : %f %f %f " % (pos.x, pos.y, pos.z))

# Now teleport to other position
x = 475
y = 68
z = 190
mc.entity.setTilePos(myId, posJosu.x,posJosu.y,posJosu.z)

pos = mc.entity.getPos(myId)
mc.postToChat("My new position : %f %f %f " % (pos.x, pos.y, pos.z))
