from mcturtle import minecraftturtle
from mcpi import minecraft
from mcpi import block

#create connection to minecraft
mc = minecraft.Minecraft.create()

#get players position
pos = mc.player.getPos()

#create minecraft turtle at the players position and give it a name
steve = minecraftturtle.MinecraftTurtle(mc, pos)

#tell the turtle to go forward 15 blocks
steve.forward(15)

#tell the turtle to go right 90 degrees
steve.right(90)

#tell the turtle to go up by 45 degress
steve.up(45)

turtle to go forward 25 blocks
steve.forward(25)