import mcpi.minecraft as minecraft
import mcpi.block as block
import time as time

def cleareBlock(size):
    mc = minecraft.Minecraft.create()
    pos = mc.player.getTilePos()
    # Виды блоков
    bl1 = block.AIR #это блок воздуха
    bl2 = block.STONE#это блок камня
    bl3 = block.GOLD_BLOCK#это блок золота
    bl4 = block.LEAVES


    # Координаты персонажа
    x = pos.x + 1 #Ширина
    y = pos.y #Высота
    z = pos.z #Длина

    time.sleep(2)

    mc.setBlocks(x, y, z, x + size, y + size, z + size, bl4)
    mc.postToChat("Очистка произведена")