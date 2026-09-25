from numpy import pi as π
import numpy as np
from Jotun_cycle import *
import sympy as sp

A_combustor_inlet = A2 # = .25*π*(d_outer)**2 - .25*π*(d_inner)**2
A_combustor_outlet = A3
τ = .0053016 # target residence time to decide combustor chamber length
# τ = np.array(.005,.01)

# VOLUME_COMBUSTOR = mdot_air*τ/rho_2
rho_avg_combustor = 0.5 * (rho_2 + rho_3)
total_volume_combustor = mdot_exhaust*τ/rho_avg_combustor
N_cans = 5 # number of cans.

can_combustor_inlet = A2/N_cans
can_combustor_inlet_d = cci_d = d(can_combustor_inlet)

can_combustor_outlet = A3/N_cans
can_combustor_outlet_d = cco_d = d(can_combustor_outlet)

can_volume_combustor = total_volume_combustor/N_cans
θ = to_rad(4.97)
can_L_combustor = (12*can_volume_combustor) / (π*(cci_d**2 + cci_d*cco_d + cco_d**2))
# total_L_combustor = total_volume_combustor

f = mdot_fuel/mdot_air

print(f'Residence time = {τ*1e3} ms')
# print(f'Total combustor length = {total_L_combustor*1e3:.4f} mm')
print(f'Total combustor volume = {total_volume_combustor*1e9:.4f} mm^3')
print(f'Can inlet diameter = {cci_d*1e3} mm')
print(f'Can outlet diameter = {cco_d*1e3} mm')

print(f'Can volume combustor = {can_volume_combustor*1e9:.4f} mm^3')
print(f'Can length combustor = {can_L_combustor*1e3:.4f} mm')


print(f'Total combustor volume = {total_volume_combustor*1e3:.4f} L')
print(f'Can volume combustor = {can_volume_combustor*1e3:.4f} L')

