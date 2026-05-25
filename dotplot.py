"""
Dotplot generator
"""

# USER DATA
SEQ1 = """
DOROTHYHODGKIN
"""

SEQ2 = """
DOROTHYCROWFOOTHODGKIN
"""

WINDOW = 3        # must be an odd number
THRESHOLD = 1     # number of matches in the diagonal window
OUTPUT_FILE_NAME = "dotplot.pdf"

# PROGRAM START
import sys

if WINDOW <= 0 or WINDOW % 2 == 0:
    print("WINDOW must be a positive odd number!")
    sys.exit(1)

SEQ1 = SEQ1.replace("\n", "").replace(" ", "")
SEQ2 = SEQ2.replace("\n", "").replace(" ", "")

# Initialize score matrix
score_matrix = [[1 if SEQ1[i] == SEQ2[j] else 0 for j in range(len(SEQ2))] for i in range(len(SEQ1))]

# Initialize dotplot
dotplot = [[0 for _ in range(len(SEQ2))] for _ in range(len(SEQ1))]

for i in range(len(SEQ1)):
    for j in range(len(SEQ2)):
        if score_matrix[i][j] == 0:
            continue  # skip if central match is not found

        diag_down_space = min(len(SEQ1) - 1 - i, len(SEQ2) - 1 - j)
        diag_up_space = min(i, j)

        winup = min(WINDOW // 2, diag_up_space)
        windown = min(WINDOW // 2, diag_down_space)

        # balance short edges
        updiff = (WINDOW // 2) - winup
        downdiff = (WINDOW // 2) - windown
        winup += downdiff
        windown += updiff
        winup = min(winup, diag_up_space)
        windown = min(windown, diag_down_space)

        winlen = winup + windown + 1
        thresh = int(THRESHOLD / WINDOW * winlen) or 1

        window_score = sum(score_matrix[i + w][j + w] for w in range(-winup, windown + 1))

        if window_score >= thresh:
            dotplot[i][j] = 1

# PLOT SECTION
try:
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(len(SEQ2) * 0.4, len(SEQ1) * 0.4), dpi=150)

    ax.set_xlim(0, len(SEQ2))
    ax.set_ylim(0, len(SEQ1))
    ax.invert_yaxis()  # <-- Important: so (0,0) is top-left
    ax.set_xticks([j + 0.5 for j in range(len(SEQ2))])
    ax.set_yticks([i + 0.5 for i in range(len(SEQ1))])
    ax.set_xticklabels(list(SEQ2))
    ax.set_yticklabels(list(SEQ1))
    ax.xaxis.tick_top()
    ax.set_xticks(range(len(SEQ2 + " ")), minor=True)
    ax.set_yticks(range(len(SEQ1 + " ")), minor=True)
    ax.grid(True, which='minor', color='lightgrey', linewidth=0.5)
    for i in range(len(SEQ1)):
        for j in range(len(SEQ2)):
            if SEQ1[i] == SEQ2[j]:
                fontweight = 'bold' if dotplot[i][j] else 'normal'
                ax.text(j + 0.5, i + 0.5, SEQ1[i], ha='center', va='center',
                        fontsize=12, fontweight=fontweight, color='black')

    ax.set_title(f"DotPlot matrix\nWindow: {WINDOW}  Threshold: {THRESHOLD}", pad=40)
    ax.tick_params(axis='x')
    ax.set_aspect('equal')

    plt.tight_layout()
    plt.savefig(OUTPUT_FILE_NAME)
    plt.show()  # Uncomment for live viewing

except ImportError:
    print("Matplotlib is not installed. Install it with `pip install matplotlib`.")

