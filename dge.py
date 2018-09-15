import numpy as np

def max_gap_cut(data, low, high):
    data = data[(data > low) & (data < high)]
    data = np.sort(data)
    dx = np.diff(data)

    dx_argmax = np.argmax(dx)

    return data[dx_argmax] + dx[dx_argmax]/2