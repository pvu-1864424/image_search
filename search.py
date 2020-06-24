from ColorDescriptor import ColorDescriptor
from searcher import Searcher
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--index', required=True,
    help = 'Path to where the computed index will be stored')
ap.add_argument('-q', '--query', required=True,
    help = 'Path to the query image')
ap.add_argument('-r', '--result-path', required = True,
    help = 'Path to the result path')
args = vars(ap.parse_args())

cd = ColorDescriptor((8, 12, 3))