# getMyId.py
# Simple code to show a message in the chat
import mcpi.minecraft as minecraft

# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')
mc = minecraft.Minecraft.create()

# Get your id
playerName = "PUT_YOUR_PLAYER_NAME!!!"
myId = mc.getPlayerEntityId(playerName);
pos = mc.entity.getPos(myId)

print "My id is: "
print myId


pos = mc.entity.getTilePos(myId)
mc.postToChat("My id: %d My position : %f %f %f " % (myId, pos.x, pos.y, pos.z))
