
# teleport.py
# Moves player to given position
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Simple delay to see things
time.sleep(2)


pos = mc.player.getPos()
mc.postToChat("Our position : %f %f %f " % (pos.x, pos.y, pos.z))

# Now teleport to other position
x = 10
y = 1000
z = 12
mc.player.setTilePos(x,y,z);

pos = mc.player.getPos()
mc.postToChat("Our new position : %f %f %f " % (pos.x, pos.y, pos.z))