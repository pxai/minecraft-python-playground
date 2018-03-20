import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

mc = minecraft.Minecraft.create()

# Lo egin
time.sleep(2)

# Get your id
jokalaria = "josu"
jokalariID = mc.getPlayerEntityId(jokalaria);
posizioa = mc.entity.getPos(jokalariID)

mc.setBlock(posizioa.x, posizioa.y, posizioa.z, block.GOLD_BLOCK)

mc.postToChat('Bloke bat jarri dut.')

for i in range(0,20):
	mc.setBlock(posizioa.x, posizioa.y+i, posizioa.z, block.GOLD_BLOCK)