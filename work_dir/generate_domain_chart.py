# filename: generate_domain_chart.py
import matplotlib.pyplot as plt

domains = {
    "General Human-AI Interaction": 6,
    "Robotics/HRI": 2,
    "Decision Support": 4,
    "Autonomous Vehicles": 1,
    "Machine Translation": 1,
    "Large Language Models": 1,
    "Gesture Recognition": 1,
    "Gig Economy/Scheduling": 1,
    "AI-Assisted Teaching": 1
}

domain_names = list(domains.keys())
paper_counts = list(domains.values())

plt.figure(figsize=(12, 6))
plt.bar(domain_names, paper_counts)
plt.xlabel("Application Domain")
plt.ylabel("Number of Papers")
plt.title("Number of Papers per Application Domain")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("domain_chart.png")
print("Bar chart saved to domain_chart.png")