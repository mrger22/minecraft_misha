import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time
from func.cleare_block import cleareBlock


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

cleareBlock(10)
