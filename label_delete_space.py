import os
from tqdm import tqdm

path = './out/'

for file in tqdm(os.listdir(path)):
    dst = file.replace(' ', '')
    os.rename(path + file, path + dst)
