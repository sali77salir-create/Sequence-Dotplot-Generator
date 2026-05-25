# Sequence Dotplot Generator 📊🧬

A Python implementation of the classic Dotplot algorithm for visualizing sequence similarities. Unlike high-level wrapper tools, this script implements the core matrix logic, sliding-window noise filtering, and dynamic edge-handling from scratch.

## 📌 Overview
In bioinformatics, a dot plot is a graphical method used to compare two biological sequences and identify regions of close similarity. This script goes beyond simple 1:1 character matching by implementing a configurable **sliding window** and **threshold** system. This approach effectively filters out background noise, highlighting true structural alignments and homologies.

## ⚙️ Technical Architecture
* **Language:** Python 3.x
* **Data Visualization:** `matplotlib`
* **Algorithm:** Matrix-based sequence alignment with sliding window filtering.

## 🚀 Key Features
* **From-Scratch Algorithmic Logic:** Built the core 2D matrix generation and scoring logic purely in Python, without relying on external bioinformatics libraries.
* **Noise Filtering:** Utilizes a customizable `WINDOW` size and `THRESHOLD` to eliminate random, isolated matches and emphasize continuous sequence homology.
* **Dynamic Edge Handling:** Intelligently balances the sliding window at the edges of the sequence matrices to prevent `IndexError` anomalies and ensure accurate border scoring.
* **Automated Data Visualization:** Renders a clean, highly readable grid plot using `matplotlib`. The script dynamically adjusts the figure size based on sequence length, bolds significant matches, and exports the analytical result directly to a PDF file (`dotplot.pdf`).

## 💻 Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/yourusername/Sequence-Dotplot-Generator.git](https://github.com/yourusername/Sequence-Dotplot-Generator.git)
cd Sequence-Dotplot-Generator
```

2. **Install dependencies:**
This script requires `matplotlib` for generating the visual plots.
```bash
pip install matplotlib
```

## 🏃‍♂️ Usage
1. Open the `dotplot.py` file.
2. Modify the target sequences and algorithm parameters in the `# USER DATA` section at the top of the file:
```python
SEQ1 = "YOUR_FIRST_SEQUENCE"
SEQ2 = "YOUR_SECOND_SEQUENCE"
WINDOW = 3        # Must be an odd number
THRESHOLD = 1     # Number of matches required in the diagonal window
```
3. Execute the script:
```bash
python dotplot.py
```
4. The script will generate a high-resolution `dotplot.pdf` file in the same directory.
