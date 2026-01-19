import matplotlib.pyplot as plt
import matplotlib


# What is a matplotlib backend

# Backends are used for displaying matplotlib figures on the screen
# or for writing to files
# A backend is basically a different rendering type i guess?
# Two types of backends:
# ui backend / interactive backends
# Used for displaying stuff on the screen
# hardcopy backends / non-interactive backends
# Used to make image files


# setting a backend
print(matplotlib.get_backend())
matplotlib.use("TkAgg")
print(matplotlib.get_backend())
fig, axs = plt.subplots(2, 2, figsize=(4, 3), layout="constrained")

# plt.show()
