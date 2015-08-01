from land import BasicLand, BasicLandType

s = BasicLand(BasicLandType.SWAMP)
s.info()
print(s.tap(),"\n")
f = BasicLand(BasicLandType.FOREST)
f.info()
print(f.tap())
