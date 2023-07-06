# @dong
# get map 20230707

from utils.map_lib import get_map

# @ap50
MINOVERLAP = 0.5
map_out_path = 'map_out'

print("----Get map-------.")
get_map(MINOVERLAP, True, 0.5, map_out_path)
print("-------Get map done.")