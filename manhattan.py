import cv2
import numpy as np

input_files = ["Idol_binary.png", "Vase_binary.png", "Flower_binary.png"]  

for fname in input_files:
    image = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    if image is None:
        continue

    h, w = image.shape

    INF = 9999
    dt = [[INF if image[y, x] != 0 else 0 for x in range(w)] for y in range(h)]

    for y in range(h):
        for x in range(w):
            if dt[y][x] != 0:
                if y > 0:
                    dt[y][x] = min(dt[y][x], dt[y-1][x] + 1)
                if x > 0:
                    dt[y][x] = min(dt[y][x], dt[y][x-1] + 1)

    for y in reversed(range(h)):
        for x in reversed(range(w)):
            if dt[y][x] != 0:
                if y < h-1:
                    dt[y][x] = min(dt[y][x], dt[y+1][x] + 1)
                if x < w-1:
                    dt[y][x] = min(dt[y][x], dt[y][x+1] + 1)

    max_dist = max(max(row) for row in dt if row)
    if max_dist == 0:
        max_dist = 1

    img = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            val = int((dt[y][x] / max_dist) * 255)
            R = val
            G = 0
            B = 255 - val
            img[y, x] = [B, G, R]

    base = fname.split(".")[0]  
    cv2.imwrite(f"{base}_distance.png", img)
