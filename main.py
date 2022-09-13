# py .\setup.py build
# py .\setup.py install

from steganogan import SteganoGAN
steganogan = SteganoGAN.load(architecture='dense')
steganogan.encode('research/input.png', 'research/output.png', 'This is a super secret message!')