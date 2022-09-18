import sys
import numpy as np
import matplotlib.pyplot as plt
import pprint

def pdf(x, p1, p2):
    """
    - Args:
        - x (np.ndarray): x=3,4,5,... 
        - p1 (float): probability (0<=p1<=1)
        - p2 (float): probability (0<=p2<=1)
    - Returns:
        - y (np.array)
    """
    y = np.zeros(len(x))
    if (x[0] < 3):
        print(f"error: {sys._getframe().f_code.co_name}")
        sys.exit(1)
    for i, xi in enumerate(x):
        yi = 0
        for xj in np.arange(1, xi):
            yi += p1 * p2 * np.power(1-p1-p2, xj-1) * (np.power(1-p1, xi-xj-1) + np.power(1-p2, xi-xj-1))
        y[i] = yi
    return y


def create_graph(x, y, z):
    """
    - Args:
        - x (np.ndarray)
        - y (np.ndarray)
        - z (np.ndarray)
    - Returns:
    """
    fig = plt.figure(figsize=(8,6), tight_layout=True)
    ax = fig.add_subplot(1, 1, 1)
    # ax.plot(x, y)
    ax.plot(x, z)
    ax.grid()
    fig.savefig("image.jpg")


def get_data():
    """
    - Args:
    - Returns:
    """
    p1 = 1/48  # get probability
    p2 = 1/48  # get probability
    x = np.arange(3, 301)
    y = pdf(x, p1, p2)
    return x, y


def create():
    """
    - Args:
    - Returns:
    """
    x, y = get_data()
    z = np.cumsum(y)
    create_graph(x, y, z)
    

def main():
    """
    - Args:
    - Returns:
    """
    create()


if __name__ == '__main__':
    main()
