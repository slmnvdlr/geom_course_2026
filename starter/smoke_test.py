"""Минимальная проверка окружения для первого практического занятия."""

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main() -> None:
    x = np.linspace(0, 2 * np.pi, 200)
    frame = pd.DataFrame({"x": x, "sin(x)": np.sin(x)})

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(frame["x"], frame["sin(x)"], label="sin(x)")
    ax.set(xlabel="x", ylabel="y", title="Проверка окружения")
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()

    output_dir = Path("figures")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "environment-check.png"
    fig.savefig(output_path, dpi=150)

    print(f"Python-библиотеки работают. Matplotlib: {matplotlib.__version__}")
    print(f"Создан файл: {output_path.resolve()}")


if __name__ == "__main__":
    main()

