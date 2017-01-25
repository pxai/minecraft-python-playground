# helloworld.py
# Simple code to show a message in the chat
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')

mc.postToChat("Hello World!")

# We get player id with the name
myPlayerId = mc.getPlayerEntityId("PUT_YOUR_USER_NAME")
pos = mc.entity.getPos(myPlayerId)
print "Your entity id ", myPlayerId
mc.postToChat("My position : %f %f %f " % (pos.x, pos.y, pos.z))