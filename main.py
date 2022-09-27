# py .\setup.py build
# py .\setup.py install

import os
from os import listdir
from os.path import isfile, join
from steganogan import SteganoGAN

input_path = 'research\\data\\div2k\\val\\_'
output_path = 'research\\StegImages'
files = [f for f in listdir(input_path) if isfile(join(input_path, f))]

steganogan = SteganoGAN.load(architecture='dense', cuda=False)
# steganogan = SteganoGAN.load(path='research/models/1664212615/weights.steg', cuda=False)

for file in files:
    input_file_path = os.path.join(input_path, file)
    output_file_path = os.path.join(output_path, file)
    print('processing ' + file)
    # steganogan.encode('research/input.png', 'research/output.png', 'This is a super secret message!')
    steganogan.encode(input_file_path, output_file_path, 'This is a super secret message!')