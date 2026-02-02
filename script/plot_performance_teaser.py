import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
methods = ["PAR (ours)", "FrameDiff", "RFDiffusion", "Genie2", "Proteina"]
colors = ["#0077b6", "#90e0ef", "#546e7a", "#90a4ae", "#cfd8dc"]

# FPSD Metrics (Lower is better)
fpsd_pdb = [161.0, 194.2, 253.7, 350.0, 271.3]
fpsd_afdb = [228.4, 258.1, 252.4, 313.8, 272.6]

# Designability Metric (Higher is better)
designability = [96.6, 65.4, 94.4, 95.2, 92.6]

# --- Layout Setup ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), dpi=1200, 
                               gridspec_kw={'width_ratios': [2, 1]})

width = 0.15
x_fpsd = np.arange(2) 
x_design = np.arange(1)

def plot_grouped_bars(ax, x_pos, data_list, is_design=False):
    """Helper to plot grouped bars with scaled font sizes"""
    for i, method in enumerate(methods):
        if is_design:
            scores = [data_list[i]]
        else:
            scores = [data_list[0][i], data_list[1][i]]
            
        offset = i * width
        rects = ax.bar(x_pos + offset, scores, width, label=method, color=colors[i])
        
        # Add score labels above bars - BUMPED TO 11pt
        for rect in rects:
            height = rect.get_height()
            is_bold = "bold" if "ours" in method.lower() else "normal"
            ax.annotate(f'{height:.1f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 5), 
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=16, fontweight=is_bold, color="#333333")

# --- Plot 1: FPSD ---
plot_grouped_bars(ax1, x_fpsd, [fpsd_pdb, fpsd_afdb])
ax1.set_xticks(x_fpsd + width * 2)
# X-TICK LABELS BUMPED TO 16pt
ax1.set_xticklabels(["FPSD-PDB ↓", "FPSD-AFDB ↓"], fontweight='bold', fontsize=16, color="#2c3e50")
ax1.set_ylim(50, 420)
# Y-AXIS LABEL BUMPED TO 16pt
ax1.set_ylabel("FPSD Score", fontweight='bold', fontsize=16, color="#546e7a")

# --- Plot 2: Designability ---
plot_grouped_bars(ax2, x_design, designability, is_design=True)
ax2.set_xticks(x_design + width * 2)
# X-TICK LABELS BUMPED TO 16pt
ax2.set_xticklabels(["Designability ↑"], fontweight='bold', fontsize=16, color="#2c3e50")
ax2.set_ylim(30, 100)
# Y-AXIS LABEL BUMPED TO 16pt
ax2.set_ylabel("Percentage (%)", fontweight='bold', fontsize=16, color="#546e7a")

# --- Universal Styling ---
for ax in [ax1, ax2]:
    ax.grid(axis='y', linestyle='--', alpha=0.3, color="#90a4ae")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Y-AXIS TICKS BUMPED TO 14pt
    ax.tick_params(axis='y', colors='#546e7a', labelsize=16)

# --- Header Legend ---
# Legend font size bumped to 20pt for clear "Header" visibility
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.05),
           ncol=5, frameon=False, fontsize=20, handletextpad=0.4, columnspacing=1.2)

# Adjust layout: increased the top margin (0.88) to accommodate the much larger legend
plt.tight_layout(rect=[0.0, 0.0, 1, 0.88]) 

plt.savefig('../static/img/PAR_performance_teaser.png', dpi=1200, bbox_inches='tight')