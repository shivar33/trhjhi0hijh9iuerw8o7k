import matplotlib.pyplot as plt
import numpy as np

Astn=["Joshie","James", "Olivia", "Charlotte", "Emma", "Evelyn"]
Astm=[10,86,77,45,59,98]

def bar():
    plt.plot(Astn,Astm)
    plt.xlabel("student names")
    plt.ylabel("student mark")
    plt.show()
bar()

