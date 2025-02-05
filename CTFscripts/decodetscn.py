# Node data extracted from the scene
nodes = [
    {"name": "YBN", "text": "YBN", "offset_left": 298.0, "offset_top": 278.0},
    {"name": "a", "text": "}", "offset_left": 535.0, "offset_top": 277.0},
    {"name": "n", "text": "7", "offset_left": 459.0, "offset_top": 279.0},
    {"name": "b", "text": "{", "offset_left": 353.0, "offset_top": 277.0},
    {"name": "c", "text": "73", "offset_left": 426.0, "offset_top": 279.0},
    {"name": "d", "text": "g", "offset_left": 362.0, "offset_top": 277.0},
    {"name": "e", "text": "n", "offset_left": 511.0, "offset_top": 279.0},
    {"name": "x", "text": "3", "offset_left": 523.0, "offset_top": 279.0},
    {"name": "y", "text": "0", "offset_left": 372.0, "offset_top": 278.0},
    {"name": "z", "text": "3", "offset_left": 501.0, "offset_top": 279.0},
    {"name": "o", "text": "_", "offset_left": 470.0, "offset_top": 279.0},
    {"name": "f", "text": "5", "offset_left": 480.0, "offset_top": 279.0},
    {"name": "g", "text": "c", "offset_left": 491.0, "offset_top": 278.0},
    {"name": "h", "text": "24", "offset_left": 331.0, "offset_top": 278.0},
    {"name": "i", "text": "_", "offset_left": 415.0, "offset_top": 277.0},
    {"name": "k", "text": "07", "offset_left": 395.0, "offset_top": 278.0},
    {"name": "j", "text": "x", "offset_left": 448.0, "offset_top": 278.0},
    {"name": "l", "text": "d", "offset_left": 383.0, "offset_top": 278.0},
]

# Sort nodes by position (left-to-right, then top-to-bottom)
sorted_nodes = sorted(nodes, key=lambda node: (node["offset_left"], node["offset_top"]))

# Concatenate the text in sorted order
flag = "".join(node["text"] for node in sorted_nodes)

print("Reconstructed flag:", flag)
