#Script by Ed0
#Chunk & Subchunk grid marker v1.0
from pymclevel.materials import alphaMaterials

displayName = "Chunk Grid Marker"

block1=1
block2=2

inputs=(
("Block 1",alphaMaterials[159, 2]),
("Block 2",alphaMaterials[159, 5]),
("SubChunks", False),
)
def changeBlock(current):
	return{
		block1: block2,
		block2: block1,
	}[current]

def perform(level, box, options):
	y = box.miny
	x = box.minx
	z = box.minz
	global block1
	block1 = options["Block 1"]
	global block2
	block2 = options["Block 2"]
	subchunks = options["SubChunks"]
	blockToPlace = block1
	lastBlock = block1
	
	
	if subchunks:
		print str(abs(box.maxx - box.minx))+', '+str(abs(box.maxz - box.minz))
		if (abs(box.maxx - box.minx)) > (abs(box.maxz - box.minz)):
			for x in xrange(box.minx, box.maxx):
				if x%16==0:
					lastBlock=changeBlock(lastBlock)
				blockToPlace=lastBlock;
					
				for y in xrange(box.miny, box.maxy):
					if y%16==0:
						blockToPlace=changeBlock(blockToPlace)
					
					level.setBlockAt(x,y,z,blockToPlace.ID)
					level.setBlockDataAt(x,y,z,blockToPlace.blockData)
		else:
			for z in xrange(box.minz, box.maxz):
				if z%16==0:
					lastBlock=changeBlock(lastBlock)
				blockToPlace=lastBlock;
					
				for y in xrange(box.miny, box.maxy):
					if y%16==0:
						blockToPlace=changeBlock(blockToPlace)
					
					level.setBlockAt(x,y,z,blockToPlace.ID)
					level.setBlockDataAt(x,y,z,blockToPlace.blockData)
			
		
	else:
		for x in xrange(box.minx, box.maxx):
			if x%16==0:
				lastBlock=changeBlock(lastBlock)
			blockToPlace=lastBlock;
					
			for z in xrange(box.minz, box.maxz):
				if z%16==0:
					blockToPlace=changeBlock(blockToPlace)
					
				level.setBlockAt(x,y,z,blockToPlace.ID)
				level.setBlockDataAt(x,y,z,blockToPlace.blockData)