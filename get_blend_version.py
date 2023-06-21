import bpy


def get_blend_version(blend_path: str) -> tuple[int, int, int]:
    with bpy.data.libraries.load(blend_path, link=True) as _, _:
        pass

    for library in bpy.data.libraries:
        if library.filepath == blend_path:
            return library.version
