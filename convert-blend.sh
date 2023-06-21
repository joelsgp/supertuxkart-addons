#!/bin/bash
set -eux

blender-2.7 \
    "$1" \
    --background \
    --python ~/src/supertuxkart/stk-blender/extras/uv_textures_to_materials.py \
    --python ~/src/supertuxkart/blender_save.py \
