import json

import matplotlib.pyplot as plt

# Load data from JSON file
with open('./loss.json') as f:
    data = json.load(f)

# Extract epoch and loss values
epochs = [entry['epoch'] for entry in data]
losses = [entry['loss'] for entry in data]

# Plot the graph
plt.plot(epochs, losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.show()