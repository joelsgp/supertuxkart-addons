#!/bin/bash
set -eux

# https://github.com/supertuxkart/stk-blender#importing-blender-files-created-from-older-blender-versions

blender-2.7 \
    "$1" \
    --background \
    --python ~/src/supertuxkart/stk-blender/extras/uv_textures_to_materials.py \
    --python ~/src/supertuxkart/blender_save.py \
