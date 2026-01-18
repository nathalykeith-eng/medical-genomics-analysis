import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_variant_distribution(summary, output_path="results/figures") -> str:
    """
    Plot and save variant type distribution.
    """
    # Cria a pasta se não existir
    os.makedirs(output_path, exist_ok=True)

    plt.figure(figsize=(8,5))
    sns.set(style="whitegrid")
    sns.barplot(x=summary.index, y=summary.values)
    plt.title("Distribuição de tipos de variantes")
    plt.xlabel("Tipo de variante")
    plt.ylabel("Contagem")

    # Salva a figura
    file_path = os.path.join(output_path, "variant_distribution.png")
    plt.savefig(file_path)
    plt.close()

    return file_path