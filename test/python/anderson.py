from pytriqs.gf import *
from pytriqs.archive import *
from numpy import zeros
import pytriqs.utility.mpi as mpi
from pytriqs.utility.h5diff import h5diff

from ctint_tutorial import Solver

# Parameters
beta = 20.0
n_iw = 200;
U = 1.0
delta = 0.1;
n_cycles = 10000;

S = Solver(beta, n_iw)

# init the Green function
mu = 1.3 - U/2
eps0 = 0.2
S.G0_iw << inverse(iOmega_n + mu - 1.0 * inverse(iOmega_n - eps0))

S.solve(U, delta, n_cycles)

if mpi.is_master_node():
  A = HDFArchive("anderson.out.h5",'w')
  A['G'] = S.G_iw['up']

# -------- Compare ---------
# Not present
# h5diff("anderson.out.h5", "anderson.ref.h5")
