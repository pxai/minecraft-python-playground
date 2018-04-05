import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.entity as entity
import time as time
from random import randint

mc = minecraft.Minecraft.create()

# Lo egin
time.sleep(4)

# Get your id
jokalaria = "josu"
jokalariID = mc.getPlayerEntityId(jokalaria);
posizioa = mc.entity.getPos(jokalariID)

mc.setEntity(posizioa.x, 
             posizioa.y, 
             posizioa.z, 
             entity.CHICKEN)

for i in range(0,50):
    mc.setEntity(posizioa.x, 
                posizioa.y + randint(10, 20), 
                posizioa.z + randint(10, 20), 
                entity.HORSE)
    time.sleep(0.5)

#for i in range(0,0):
#    mc.setEntity(pos.x, pos.y, pos.z, entity.ZOMBIE)


mc.postToChat('Animals created.')
