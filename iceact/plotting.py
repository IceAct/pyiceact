import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
from pkg_resources import resource_filename
import numpy as np


def load_pixel_coordinates():
    filename = resource_filename('iceact', 'resources/pixel_coordinates.txt')
    x, y = np.genfromtxt(filename, unpack=True)
    return x, y


def plot_camera(data, cmap='gray', ax=None):
    '''
    Create an IceAct camera plot

    Parameters
    ----------
    data: array-like with length 61
        data array with one value per pixel
    cmap: str or matplotlib.colors.ColorMap instance
        The colormap to use
    ax: matplotlib.axes.Axes instace
        The axes to use. If not given, the current axes will be used.
    '''

    if ax is None:
        ax = plt.gca()

    x, y = load_pixel_coordinates()

    hexagons = [
        RegularPolygon(xy, 6, radius=1)
        for xy in zip(x, y)
    ]
    collection = PatchCollection(hexagons)
    collection.set_array(data)
    collection.set_cmap(cmap)

    ax.add_collection(collection)
    ax.set_xlim(x.min() - 2, x.max() + 2)
    ax.set_ylim(y.min() - 2, y.max() + 2)
    ax.set_aspect(1)

    return collection
