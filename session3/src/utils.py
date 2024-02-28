import numpy as np
import glob
from tqdm import tqdm
from scipy.io import loadmat


def merge_npy_data(path):
    all_npy_files = glob.glob(path + "*.npy")

    data = []
    for filename in tqdm(all_npy_files, desc="Merging the licks data"):
        data_per_trial = np.load(filename)
        data.append(data_per_trial)

    stacked_data = np.stack(data)
    return stacked_data

def merge_mat_data(path,col_name='pupil_area'):
    all_mat_files = glob.glob(path + "*.mat")
    
    data = []
    for filename in tqdm(all_mat_files, desc="Merging the " +col_name+ "data"):
        data_per_trial = loadmat(filename)[col_name].squeeze()
        data.append(data_per_trial)

    return np.stack(data)