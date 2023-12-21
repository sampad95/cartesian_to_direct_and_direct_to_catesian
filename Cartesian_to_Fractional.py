import numpy as np

def carte_to_frac(str_file):
    with open(str_file, 'r') as data:
        fl = data.readlines()

        scale_factor = float(fl[1])
        lattice_matrix = scale_factor*np.array([list(map(float, fl[2:5][i].split())) for i in range(len(fl[2:5]))]).T
        carte_coord_matrix = np.array([list(map(float, fl[8:][i].split())) for i in range(len(fl[8:]))]).T
        fractional_coord = np.dot(np.linalg.inv(lattice_matrix), carte_coord_matrix).T

    with open('poscar_frac', 'w') as output:
        for i in fractional_coord:
            output.write(str(i[0])+'\t')
            output.write(str(i[1])+'\t')
            output.write(str(i[2])+'\n')
    return fractional_coord


str_file = input('Enter the POSCAR format file with cartesian coordinate\n')
carte_to_frac(str_file)
