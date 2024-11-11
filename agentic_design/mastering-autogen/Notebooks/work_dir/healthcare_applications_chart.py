# filename: healthcare_applications_chart.py
import matplotlib.pyplot as plt

# Data: healthcare applications and their corresponding number of papers
applications = [
    "Community Level Work",
    "Risk Management/Preventive Care",
    "Healthcare Operation Management",
    "Remote Care",
    "Early Detection",
    "Predictive Modeling",
    "Phenotyping",
    "Generative Models",
    "Reinforcement Learning",
    "Personalized Healthcare Services",
    "IoT-based Healthcare Systems",
    "Control and Monitoring Applications",
    "Fairness in Classification",
    "Intelligent Wearable Devices",
    "Data Analytics for Insights"
]

# Count of papers for each application
counts = [
    1,  # Community Level Work
    1,  # Risk Management/Preventive Care
    1,  # Healthcare Operation Management
    1,  # Remote Care
    1,  # Early Detection
    1,  # Predictive Modeling
    1,  # Phenotyping
    1,  # Generative Models
    1,  # Reinforcement Learning
    1,  # Personalized Healthcare Services
    1,  # IoT-based Healthcare Systems
    1,  # Control and Monitoring Applications
    1,  # Fairness in Classification
    1,  # Intelligent Wearable Devices
    1   # Data Analytics for Insights
]

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.barh(applications, counts, color='skyblue')
plt.xlabel('Number of Papers')
plt.title('Healthcare Applications and the Number of Papers Discussing Each Application')
plt.grid(axis='x')

# Save the chart to a file
plt.tight_layout()
plt.savefig('healthcare_applications_chart.png')
plt.close()