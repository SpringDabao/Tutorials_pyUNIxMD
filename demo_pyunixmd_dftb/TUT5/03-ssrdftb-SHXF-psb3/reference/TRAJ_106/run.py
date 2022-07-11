from molecule import Molecule
import qm, mqc

# Define the target system.
with open("geom.xyz", "r") as fp:
    geom = fp.read()
mol = Molecule(geometry=geom, nstates=2, charge=+1)

# Set QM method.
qm = qm.dftbplus.SSR(molecule=mol, tuning = [3.2, 3.2, 3.2], l_range_sep=True, l_state_interactions=True, version="20.1", install_path="/home/dhhan/program/_install_dftb_20.1/", sk_path="/home/dhhan/program/slko/ob2-1-1/base/")

# Determine MD method.
md = mqc.SHXF(molecule=mol, nsteps=600, nesteps=1000, dt=0.5, istate=1, elec_object="density", sigma=0.1)

# Execute the simulation.
md.run(qm=qm)
