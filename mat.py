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

    #create the distance transfer list
    dt = np.array(dt)

    #initializing the blank skeleton image
    skeleton = np.zeros((h, w), dtype=np.uint8)
    for y in range(1, h-1):
        for x in range(1, w-1):
            if dt[y, x] > 0: # Consider only background pixels
                # Check if the current pixel is a local maximum in its 3x3 neighborhood
                if all(dt[y, x] >= dt[ny, nx]
                       for ny in range(y-1, y+2)
                       for nx in range(x-1, x+2)
                       if not (nx == x and ny == y)):
                    # Mark skeleton pixel as white (255)
                    skeleton[y, x] = 255
    
    # Create a color image to superimpose skeleton on the original shape
    superimposed = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            if skeleton[y, x] == 255:
                # Skeleton pixels in RED
                superimposed[y, x] = [0, 0, 255]
            elif image[y, x] != 0:
                # Original shape (foreground) shown in light gray
                superimposed[y, x] = [200, 200, 200] 
            else:
                # Background kept as black
                superimposed[y, x] = [0, 0, 0] 

    # Save skeleton-only and superimposed outputs
    base = fname.split(".")[0]  
    cv2.imwrite(f"{base}_skeleton_only.png", skeleton)
    cv2.imwrite(f"{base}_skeleton_superimposed.png", superimposed)
