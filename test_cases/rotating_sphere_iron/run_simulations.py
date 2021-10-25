#!/usr/bin/env python3

import numpy as np
import os
import shutil
import libconf

s_iron = 105
bulk_iron = 113.5

shears = np.arange(105, 50, -10)
bulks = np.arange(113.5, 50, -10)
factor = 1e9

def nu_kmu(K, mu):
    return (3*K - 2*mu) / 2 / (3*K + mu)

def mu_knu(K, nu):
    return 3*K* (1 - 2*nu) / 2 / (1 + nu)

def new_simulation(bulk, shear):
    nextdir = f"k{int(bulk)}mu{int(shear)}/"
    try:
        os.mkdir(nextdir)
        shutil.copy("material.cfg", nextdir)
        shutil.copy("sphere.0000", nextdir)
        shutil.copy("run_slurm.sh", nextdir)
        shutil.copy("plot_L.py", nextdir)
        os.chdir(nextdir)

        with open("material.cfg", 'r+') as m:
            material = libconf.load(m)

            eos = material["materials"][0]["eos"]
            eos["bulk_modulus"] = bulk*factor
            eos["shear_modulus"] = shear*factor

            m.seek(0)
            libconf.dump(material, m)
            m.truncate()

        os.system(f"sbatch -J rcj_{nextdir} run_slurm.sh")
        os.chdir("..")
    except:
        pass


# for bulk in bulks[2::2]:
#     for shear in shears:
#     	new_simulation(bulk, shear)

nu = nu_kmu(bulk_iron, s_iron)
for bulk in bulks[1:]:
#    new_simulation(bulk, shears[0])
    new_simulation(bulk, mu_knu(bulk, nu))