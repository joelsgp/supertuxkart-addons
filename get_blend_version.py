import bpy

blend_path = r"D:\asset\data\hqKAZbQSqjx\desert_bush_2.blend"

with bpy.data.libraries.load(blend_path, link =  True) as (data_from, data_to):
    pass

for library in bpy.data.libraries:
    if library.filepath == blend_path:
        print(library.version)
        print(library.filepath)
        bpy.data.libraries.remove(library)
