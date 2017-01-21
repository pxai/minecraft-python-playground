# helloworld.py
# Simple code to show a message in the chat
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()
# IF THE SERVER IS NOT LOCALHOST, SET THE IP
# mc = minecraft.Minecraft.create('172.30.0.123')

mc.postToChat("Hello World!")