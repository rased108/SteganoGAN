# py .\setup.py build
# py .\setup.py install

import os
from os import listdir
import warnings
from os.path import isfile, join
from steganogan import SteganoGAN
from multiprocessing import Pool, freeze_support, cpu_count
from progress.bar import IncrementalBar

warnings.filterwarnings("ignore")

input_path = 'research\\data\\div2k\\val\\_'
output_path = 'research\\StegImages'
files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

bar = IncrementalBar('Processing', max=len(files))

steganogan = SteganoGAN.load(architecture='dense', cuda=False)
# steganogan = SteganoGAN.load(path='research/models/1664212615/weights.steg', cuda=False)
# steganogan.encode('research/input.png', 'research/output.png', 'This is a super secret message!')

def process(file):
    input_file_path = os.path.join(input_path, file)
    output_file_path = os.path.join(output_path, file)
    #print('processing ' + file)
    # steganogan.encode('research/input.png', 'research/output.png', 'This is a super secret message!')
    steganogan.encode(input_file_path, output_file_path, 'This is a super secret message!')
    bar.next()

if __name__ == '__main__':
    freeze_support()
    #cpu_cores = int(cpu_count() * 0.25)
    cpu_cores=2
    print('No of CPU cores: ' + str(cpu_cores) + ' of ' + str(cpu_count()))
    pool = Pool(cpu_cores)
    pool.map(process, files)
    bar.finish()