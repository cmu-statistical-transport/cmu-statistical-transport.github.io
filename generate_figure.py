import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, FancyBboxPatch
from matplotlib.collections import LineCollection
import matplotlib.patches as mpatches

# Set up the figure with a clean, modern style
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(1, 1, figsize=(14, 8), facecolor='white')

# Define colors - modern palette
color_treated = '#2E86AB'  # Blue
color_control = '#A23B72'  # Purple/Magenta
color_transport = '#F18F01'  # Orange
color_outcome = '#C73E1D'  # Red

# Generate sample distributions for treatment and control groups
np.random.seed(42)

# Treatment group (X1)
n_treat = 80
x1 = np.random.multivariate_normal([2.5, 3], [[0.5, 0.2], [0.2, 0.4]], n_treat)

# Control group (X0)
n_control = 80
x0 = np.random.multivariate_normal([1, 1.5], [[0.4, -0.1], [-0.1, 0.5]], n_control)

# Plot distributions with alpha
ax.scatter(x0[:, 0], x0[:, 1], c=color_control, s=100, alpha=0.6,
           edgecolors='white', linewidth=1.5, label='Control Group (T=0)', zorder=3)
ax.scatter(x1[:, 0], x1[:, 1], c=color_treated, s=100, alpha=0.6,
           edgecolors='white', linewidth=1.5, label='Treated Group (T=1)', zorder=3)

# Create optimal transport map visualization
# Sample a subset for cleaner visualization
n_arrows = 15
indices = np.random.choice(n_control, n_arrows, replace=False)

# Compute simple transport map (for visualization)
for i in indices:
    # Find closest point in treated group (simplified transport)
    distances = np.sum((x1 - x0[i])**2, axis=1)
    j = np.argmin(distances)

    # Draw transport arrow
    arrow = FancyArrowPatch(
        (x0[i, 0], x0[i, 1]),
        (x1[j, 0], x1[j, 1]),
        arrowstyle='->',
        mutation_scale=20,
        linewidth=1.5,
        color=color_transport,
        alpha=0.4,
        zorder=2
    )
    ax.add_patch(arrow)

# Add annotations
ax.text(0.5, 3.8, 'Optimal Transport Map', fontsize=16, fontweight='bold',
        color=color_transport, ha='left')

ax.text(0.3, 0.8, r'$\mathbb{P}_0$', fontsize=18, fontweight='bold',
        color=color_control, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=color_control, linewidth=2))

ax.text(3.3, 3.8, r'$\mathbb{P}_1$', fontsize=18, fontweight='bold',
        color=color_treated, ha='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor=color_treated, linewidth=2))

# Add causal identification text box
textstr = r'$\tau(x) = \mathbb{E}[Y(1) - Y(0) | X=x]$'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8, edgecolor=color_outcome, linewidth=2.5)
ax.text(2.2, 0.3, textstr, fontsize=14, verticalalignment='top',
        bbox=props, ha='center')

# Add title and labels
ax.set_xlabel('Covariate Space $X_1$', fontsize=14, fontweight='bold')
ax.set_ylabel('Covariate Space $X_2$', fontsize=14, fontweight='bold')
ax.set_title('Causal Identification via Optimal Transport\nMatching Distributions to Identify Treatment Effects',
             fontsize=18, fontweight='bold', pad=20)

# Set limits
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)

# Add legend
ax.legend(loc='upper left', fontsize=12, frameon=True, shadow=True, fancybox=True)

# Add grid with custom style
ax.grid(True, alpha=0.2, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Add explanatory text box at bottom
explanation = (
    "Transport maps minimize the cost of moving mass from control to treatment distribution,\n"
    "enabling causal effect identification under overlap assumptions."
)
ax.text(2.0, -0.3, explanation, fontsize=10, ha='center', style='italic',
        bbox=dict(boxstyle='round,pad=0.7', facecolor='lightblue', alpha=0.3))

plt.tight_layout()
plt.savefig('/Users/gonzalomena/statistical-transport-website/assets/images/causal_transport_diagram.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Figure saved to assets/images/causal_transport_diagram.png")
plt.close()
