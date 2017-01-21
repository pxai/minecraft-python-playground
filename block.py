# block.py
# Simple code to set one block
import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()
# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')

# Simple delay to see things
time.sleep(2)

pos = mc.player.getPos()

mc.setBlock(pos.x,pos.y,pos.z,block.GOLD_BLOCK)

mc.postToChat('Block was set')

#for i in range(0,20):
#	mc.setBlock(pos.x,pos.y+i,pos.z,block.GOLD_BLOCK)