
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
#playerName = "Player"
#myId = mc.getPlayerId(playerName);
myId = 602
pos = mc.entity.getPos(myId)

# Show your position
mc.postToChat("Our position : %f %f %f " % (pos.x, pos.y, pos.z))

# Now teleport to other position
x = 100
y = 100
z = 100
mc.entity.setTilePos(myId, x,y,z)

pos = mc.entity.getPos(myId)
mc.postToChat("Our new position : %f %f %f " % (pos.x, pos.y, pos.z))