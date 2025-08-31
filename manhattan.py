import cv2
import numpy as np

#list of input image file
input_files = ["Idol_binary.png", "Vase_binary.png", "Flower_binary.png"]  


for fname in input_files:
    #read the image in grayscale mode
    image = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
    #if the image loading fails then skip the file
    if image is None:
        continue
    
    #get the height and width
    h, w = image.shape

    # Initialize distance transform (dt) matrix:
    # If pixel is background (non-zero), set to INF
    # If pixel is foreground (black, value = 0), set to 0
    INF = 9999
    dt = [[INF if image[y, x] != 0 else 0 for x in range(w)] for y in range(h)]
    
    #step1: top-bottom and left-right
    for y in range(h):
        for x in range(w):
            if dt[y][x] != 0:
                if y > 0:
                    dt[y][x] = min(dt[y][x], dt[y-1][x] + 1)
                if x > 0:
                    dt[y][x] = min(dt[y][x], dt[y][x-1] + 1)

    #step2: bottom-top and right-left
    for y in reversed(range(h)):
        for x in reversed(range(w)):
            if dt[y][x] != 0:
                if y < h-1:
                    dt[y][x] = min(dt[y][x], dt[y+1][x] + 1)
                if x < w-1:
                    dt[y][x] = min(dt[y][x], dt[y][x+1] + 1)

    #getting the maximum distance for normalization
    max_dist = max(max(row) for row in dt if row)
    if max_dist == 0:
        max_dist = 1

    img = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            #normalizing
            val = int((dt[y][x] / max_dist) * 255)
            #map distance to color
            R = val
            G = 0
            B = 255 - val
            img[y, x] = [B, G, R]
    
    #save the output
    base = fname.split(".")[0]  
    cv2.imwrite(f"{base}_distance.png", img)
