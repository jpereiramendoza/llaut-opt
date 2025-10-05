import matplotlib.pyplot as plt
import numpy as np

# ==============================
# Datos para generar el grafico (rescatados del Jupyter Notebook)
# ==============================
metrics = ["Total Power (W)", "Total Weight (kg)", "Average Age (years)", "Total Technique"]
real_team = [100, 100, 100, 100]
sequential_model = [107.0, 98.2, 98.7, 101.6]
weighted_model = [102.4, 98.2, 99.3, 96.8]

# ==============================
# Configuracion del Plot
# ==============================
plt.figure(figsize=(6, 3.5))  # larger size for publication
plt.grid(True, linestyle="--", alpha=0.3)

# Balanced dark color palette
colors = {
    "real_team": "#1f77b4",   # medium blue
    "sequential": "#d67f00",  # dark orange
    "weighted": "#2ca02c"     # dark green
}

# ==============================
# Lineas del plot 
# ==============================
plt.plot(metrics, real_team, label="Real team", color=colors["real_team"],
         marker="o", markersize=7, linewidth=2)
plt.plot(metrics, sequential_model, label="Sequential model", color=colors["sequential"],
         marker="s", markersize=7, linewidth=2)
plt.plot(metrics, weighted_model, label="Weighted model", color=colors["weighted"],
         marker="D", markersize=6, linewidth=2)

# ==============================
# Porcentajes 
# ==============================
for i, (seq, wgt) in enumerate(zip(sequential_model, weighted_model)):
    diff_seq = seq - 100
    diff_wgt = wgt - 100
    if i == 1:
        plt.text(i, seq + 2.7, f"{diff_seq:+.1f}%", fontsize=8, color="#9C6500", ha="center")
    elif i == 2:
        plt.text(i, seq + 2.7, f"{diff_seq:+.1f}%", fontsize=8, color="#9C6500", ha="center")
    else:
        plt.text(i, seq + 0.7, f"{diff_seq:+.1f}%", fontsize=8, color="#9C6500", ha="center")
        
    if i == 0:
        plt.text(i, wgt - 4.2, f"{diff_wgt:+.1f}%", fontsize=8, color="#385723", ha="center")
    elif i == 2:
        plt.text(i, wgt - 2.2, f"{diff_wgt:+.1f}%", fontsize=8, color="#385723", ha="center")
    else:
        plt.text(i, wgt - 1.8, f"{diff_wgt:+.1f}%", fontsize=8, color="#385723", ha="center")

# ==============================
# Estilos del grafico
# ==============================
plt.ylim(90, 110)
plt.ylabel("Relative to the real team (%)", fontsize=10)
plt.title("Comparison of metrics between the real team and optimization models", fontsize=10.5)
plt.xticks(rotation=20, fontsize=9)
plt.yticks(fontsize=9)

# ==============================
# Cuadro de leyenda
# ==============================
plt.legend(
    loc="lower right",
    bbox_to_anchor=(0.31, 0.02),
    frameon=True,
    fancybox=True,
    framealpha=0.95,
    edgecolor="gray",
    fontsize=8,
    title="Models",
    title_fontsize=9
)

# ==============================
# Generacion del grafico
# ==============================
plt.tight_layout()
plt.show()

