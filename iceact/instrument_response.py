from eventio import IACTFile
import pandas as pd
import numpy as np
from scipy.spatial import KDTree
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('response_file')


def load_response(file_name, num_pixel):

    df = pd.read_csv(file_name, index_col=0)
    columns = ['t_sipm_{}'.format(pixel) for pixel in range(num_pixel)]
    response = df[columns].values
    rest_probability = 1-response.sum(axis=1)
    response = np.append(response, rest_probability.reshape((-1, 1)), axis=1)
    tree = KDTree(df[['u', 'v']].values)
    return response, tree


def select_hit_photons(photons):
    '''select photons which hit the camera '''
    r = np.sqrt(photons['x']**2 + photons['y']**2)
    mask = r < 25.35
    return photons[mask]


def calculated_detection_pixel(photons, response, tree):
    distances, indices = tree.query(np.column_stack([photons['cx'], photons['cy']]))
    pixels = list()
    for i, index in enumerate(indices):
        pixels.append(np.random.choice(response.shape[1], p=response[index]))
    return np.array(pixels)


def count_photons_per_pixel(pixels, num_pixel):
    num_photons = np.bincount(pixels)
    return num_photons[:-1]


if __name__ == '__main__':
    args = parser.parse_args()
    response, tree = load_response(args.response_file, num_pixel=61)

    f = IACTFile(args.input_file)
    event = f[0]
    photons = event.photon_bunches[0]

    selected_photons = select_hit_photons(photons)
    pixels = calculated_detection_pixel(selected_photons, response, tree)
    detected = pixels < 61
    print(pixels[detected])
    num_photons = np.bincount(pixels)
    print(num_photons)
