# Distance Transform and Medial Axis Transform

This project implements **Distance Transform (DT)** using the **Manhattan distance metric** and computes the **Medial Axis Transform (MAT)** to extract the inherent skeleton of binary images.  
The results are visualized and saved as images.

## 📌 Features
- Compute **Manhattan Distance Transform (DT)**
- Extract **Medial Axis Transform (MAT)**
- Save results as images:
  - DT → `{name}_binary_distance.png`
  - Skeleton (MAT) → `{name}_skeleton.png`
  - Superimposed skeleton on binary image → `{name}_skeleton_superimposition.png`


## 🛠 Requirements

- Python
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

## 🚀 Usage

1. Place your **binary images** inside the project folder (e.g., `Flower_binary.png`, `Vase_binary.png`, `Idol_binary.png`).
2. Run the **Manhattan Distance Transform**:
   ```bash
   python manhattan.py
   ```
   Output → `{name}_binary_distance.png`

3. Run the **Medial Axis Transform (MAT)**:
   ```bash
   python mat.py
   ```
   Output → 
   - `{name}_skeleton.png`  
   - `{name}_skeleton_superimposition.png`

## 📂 Project Structure

```
├── Input Images/                 # Folder for input binary images
│   ├── Flower_binary.png
│   ├── Vase_binary.png
│   └── Idol_binary.png
│
├── Output Images/                # Results will be saved here
│   ├── Flower_binary_distance.png
│   ├── Flower_skeleton.png
│   ├── Flower_skeleton_superimposition.png
│   ├── Vase_binary_distance.png
│   ├── Vase_skeleton.png
│   ├── Vase_skeleton_superimposition.png
│   ├── Idol_binary_distance.png
│   ├── Idol_skeleton.png
│   └── Idol_skeleton_superimposition.png
│
├── manhattan.py                  # Manhattan Distance Transform
├── mat.py                        # Medial Axis Transform
├── Report.pdf                    # Project Report
└── README.md                     # Project documentation
```

## 📖 Notes
- Input images **must be binary** (foreground = white, background = black)  
- Skeletonization extracts the **thin medial axis** while preserving topology 
- Superimposition helps visualize how the skeleton fits inside the original shape  