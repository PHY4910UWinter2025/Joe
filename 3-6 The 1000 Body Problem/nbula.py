#!/usr/bin/env python3

from nbody import Particle, System
import argparse
from sys import argv

# options

parser = argparse.ArgumentParser(description='Evolve an N-body system forward in time.')
parser.add_argument('filename', type=str, help='Initial conditions (in the correct format)')
parser.add_argument('-out', dest='out_file_base', default="snapshot", type=str, help='Base of output filename')
parser.add_argument('-dt', dest='dt', type=float, default=0.01, help='Timestep in system time units')
parser.add_argument('-tf', dest='tf', type=float, default=10.0, help='Time to stop in system time units')
parser.add_argument('-dt_out', dest='dt_out', type=float, default=0.1, help='Time between snapshot outputs')
parser.add_argument('-dt_log', dest='dt_log', type=float, default=0.01, help='Time between printed information')
parser.add_argument('-e', dest='eps', type=float, default=0.0, help='Softening length')
args = parser.parse_args()

dt = args.dt
tf = args.tf
dt_out = args.dt_out
dt_log = args.dt_log

s = System.read(args.filename)
ti = s.time

# calculate energies for later; need to update accels first
s.calc_accels()
E0 = s.T + s.U

t = ti
t_out = ti
t_log = ti
while t < tf:

	# use leapfrog to evolve particles
	s.update_positions(0.5 * dt)	
	s.calc_accels(args.eps)
	s.update_velocities(dt)
	s.update_positions(0.5 * dt)
	
	t += dt
		
	s.time = t
	
	if t >= t_out:
		fname = args.out_file_base + f"_{t:07.3f}.dat"
		s.write(fname)
		t_out += dt_out
        
	if t >= t_log:
		print(f"t = {t} | dE = { (s.T + s.U - E0)/E0}")
		t_log += dt_log

print(f"Done!")

