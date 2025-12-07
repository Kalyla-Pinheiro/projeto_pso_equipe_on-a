import matplotlib.pyplot as plt
import pandas as pd

def plot_history(history, save=False, path="results/convergence.png"):
    
    plt.plot(history, marker='o')
    plt.title("Convergência do PSO")
    plt.xlabel("Iterações")
    plt.ylabel("Melhor Resistência Prevista (MPa)")
    plt.grid()

    if save:
        plt.savefig(path, dpi=300)

    plt.show()

def save_best(best_pos, best_fit, path="results/best_result.csv"):
    
    df = pd.DataFrame([{
        "Composição (kg/m³)": best_pos,
        "Resistência Prevista (MPa)": best_fit
    }])
    df.to_csv(path, index=False)
