import cv2
import numpy as np

input_files = ["Vase_binary.png", "Flower_binary.png", "Idol_binary.png"]  

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

    dt = np.array(dt)

    skeleton = np.zeros((h, w), dtype=np.uint8)
    for y in range(1, h-1):
        for x in range(1, w-1):
            if dt[y, x] > 0:
                if all(dt[y, x] >= dt[ny, nx]
                       for ny in range(y-1, y+2)
                       for nx in range(x-1, x+2)
                       if not (nx == x and ny == y)):
                    skeleton[y, x] = 255

    superimposed = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            if skeleton[y, x] == 255:
                superimposed[y, x] = [0, 0, 255]
            elif image[y, x] != 0:
                superimposed[y, x] = [200, 200, 200] 
            else:
                superimposed[y, x] = [0, 0, 0] 

    base = fname.split(".")[0]  
    cv2.imwrite(f"{base}_skeleton_only.png", skeleton)
    cv2.imwrite(f"{base}_skeleton_superimposed.png", superimposed)
