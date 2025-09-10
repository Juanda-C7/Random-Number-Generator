import numpy as np
import matplotlib.pyplot as plt

def visualize_rng(numbers: list, title="Randomness"):
    """
    Visualiza una lista de enteros como imagen en escala de grises.
    Ajusta automáticamente al tamaño cuadrado más cercano.
    """
    # Normalizar a 0–255
    if max(numbers) > 0:
        normalized = [(n / max(numbers)) * 255 for n in numbers]
    else:
        normalized = [0] * len(numbers)

    # Calcular tamaño más cercano a cuadrado
    size = int(len(normalized) ** 0.5)
    total = size * size

    # Recortar para ajustar
    adjusted = normalized[:total]
    image_array = np.array(adjusted).reshape((size, size))

    # Mostrar imagen
    plt.figure(figsize=(8, 8))
    plt.imshow(image_array, cmap="gray", vmin=0, vmax=255)
    plt.title(f"{title} ({size}x{size}, {total} valores)")
    plt.axis("off")
    plt.show()
