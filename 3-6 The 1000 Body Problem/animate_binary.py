#!/usr/bin/env python3

from nbody import Particle, System
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d
import matplotlib.animation as animation
import argparse
from sys import argv
from time import sleep

parser = argparse.ArgumentParser(description='Display the positions of an N-body file.  If more than one file is given, they\'ll be animated.')
parser.add_argument('filenames', type=str, nargs='+', help='the list of file names')
parser.add_argument('-fps', dest='fps', type=float, default=10, help='How many frames per second to show')
parser.add_argument('-f', dest='out_file', default="", help='Save as a file')
parser.add_argument('-3d', dest="threed", action='store_true', help="Use 3D projection (slow)")
parser.add_argument('-alpha', dest="alpha", default=1, type=float, help="Alpha for each point")
parser.add_argument('-ms', dest="ms", default=4, type=float, help="Marker size for each point")
parser.add_argument('-l', dest='limits', type=float, default=None, nargs=4, help='Limits for the plot')
parser.add_argument('-view', dest='view', type=str, default=['x', 'y'], nargs=2, help='Which coordinates to plot')
args = parser.parse_args()

fig = plt.figure(figsize=(6, 6), dpi=150, facecolor="white")
if args.threed:
    ax = fig.add_subplot(111, projection='3d')
else:
    ax = fig.add_subplot(111)

ax.axis('off')
ax.set_aspect('equal')

s = System.read_binary(args.filenames[0])

if args.threed:
    x = s.all_x()
    y = s.all_y()
    z = s.all_z()
else:
    if args.view[0] == 'x':
        x = s.all_x()
    elif args.view[0] == 'y':
        x = s.all_y()
    else:
        x = s.all_z()

    if args.view[1] == 'x':
        y = s.all_x()
    elif args.view[1] == 'y':
        y = s.all_y()
    else:
        y = s.all_z()

if args.threed:
    line, = ax.plot(x, y, z, color="black", marker="o", markersize=args.ms, alpha=args.alpha, mfc="grey", mec="black", linestyle='none')
    label = ax.text(0,0,0, "t = {0:4.2f}".format(s.time), None, transform=ax.transAxes, fontsize=8)
else:
    line, = ax.plot(x, y, color="black", marker="o", markersize=args.ms, alpha=args.alpha, mfc="grey", mec="black", linestyle='none')
    label = ax.text(0,0, "t = {0:4.2f}".format(s.time), transform=ax.transAxes, fontsize=8)
    
if args.threed:
    ax.view_init(45, 45)

if args.limits == None:
    ax.autoscale()
else:
    ax.set_xlim(args.limits[0], args.limits[1])
    ax.set_ylim(args.limits[2], args.limits[3])

def update(fname):
    s = System.read_binary(fname)       
    
    if args.threed:
        x = s.all_x()
        y = s.all_y()
        z = s.all_z()
    else:
        if args.view[0] == 'x':
            x = s.all_x()
        elif args.view[0] == 'y':
            x = s.all_y()
        else:
            x = s.all_z()

        if args.view[1] == 'x':
            y = s.all_x()
        elif args.view[1] == 'y':
            y = s.all_y()
        else:
            y = s.all_z()

    
    line.set_data(x, y)
    if args.threed:
        line.set_3d_properties(zs=z)
    
    label.set_text("t = {0:4.2f}".format(s.time))
    

if len(args.filenames) > 1:
    interval = int(1.0/args.fps*1000.0)
    ani = animation.FuncAnimation(fig, update, frames=args.filenames[1:], interval=interval, repeat=False)
    
    if args.out_file != "":
        Writer = animation.writers['imagemagick']
        writer = Writer(fps=4, bitrate=-1)
    
        ani.save(args.out_file, writer=writer, dpi = 150)
    else:
        plt.show()
else:
    plt.show()

    

