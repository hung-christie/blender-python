import bpy

# import the data for US
US_male, US_female = [], []
with open('US_2020.csv') as f:
    for line in f:
        fields = line.strip()
        fields = fields.split(',')
        US_male.append((fields[1]))
        US_female.append((fields[2]))
US_male.pop(0)
US_female.pop(0)
US_male = [int(i) for i in US_male]
US_female = [int(i) for i in US_female]

# import the data for Japan
JP_male, JP_female = [], []
with open('Japan_2019.csv') as f:
    for line in f:
        fields = line.strip()
        fields = fields.split(',')
        JP_male.append((fields[1]))
        JP_female.append((fields[2]))
JP_male.pop(0)
JP_female.pop(0)
JP_male = [int(i) for i in JP_male]
JP_female = [int(i) for i in JP_female]

# clears the scene
bpy.ops.object.select_all(action = 'SELECT')
bpy.ops.object.delete(use_global = False)

# graph the US female population
for i, number in enumerate(US_female):
    bpy.ops.mesh.primitive_cube_add(size = 1)
    this_cube = bpy.context.active_object
    this_cube.location[0] = i * 1.5
    this_cube.scale = (1, number / 100000, 1)

# graph the US male population
for i, number in enumerate(US_male):
    bpy.ops.mesh.primitive_cube_add(size = 1)
    this_cube = bpy.context.active_object
    this_cube.location[0] = i * 1.5
    this_cube.scale = (1, -(number / 100000), 1)

# graph the Japanese female population
for i, number in enumerate(JP_female):
    bpy.ops.mesh.primitive_cube_add(size = 1)
    this_cube = bpy.context.active_object
    this_cube.location[0] = (i * 1.5) + 50
    this_cube.scale = (1, number / 100000, 1)

# graph the Japanese male population
for i, number in enumerate(JP_male):
    bpy.ops.mesh.primitive_cube_add(size = 1)
    this_cube = bpy.context.active_object
    this_cube.location[0] = (i * 1.5) + 50
    this_cube.scale = (1, -(number / 100000), 1)

print("done")
