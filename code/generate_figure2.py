import numpy as np
import matplotlib.pyplot as plt
import yaml
import os

# Load parameters
with open("../data/parameters.yaml", "r") as f:
    params = yaml.safe_load(f)

hazard_low = params["hazard_low"]
hazard_high = params["hazard_high"]
ai_effect_low = params["ai_effect_low"]
ai_effect_high = params["ai_effect_high"]

t = np.linspace(
    params["time_horizon"]["start"],
    params["time_horizon"]["end"],
    200
)

# Survival trajectories
S_low_noAI  = np.exp(-hazard_low * t)
S_low_AI    = np.exp(-(hazard_low + ai_effect_low) * t)

S_high_noAI = np.exp(-hazard_high * t)
S_high_AI   = np.exp(-(hazard_high + ai_effect_high) * t)

# Plot
plt.figure(figsize=(6.5, 4.5))

plt.plot(t, S_high_noAI, linestyle="--", label="High readiness – No AI")
plt.plot(t, S_high_AI, linestyle="-",  label="High readiness – With AI")

plt.plot(t, S_low_noAI,  linestyle=":",  label="Low readiness – No AI")
plt.plot(t, S_low_AI,    linestyle="-.", label="Low readiness – With AI")

plt.xlabel("Educational time")
plt.ylabel("Probability of remaining in trajectory")
plt.legend(frameon=False)
plt.grid(True, linestyle=":", alpha=0.6)

# Save figure
os.makedirs("../figures", exist_ok=True)
output_path = "../figures/ai_institutional_readiness_learning_trajectories.png"

plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Figure saved to {output_path}")

