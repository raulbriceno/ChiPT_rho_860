import os
exe='~/arch/scattering/master/bin/find_amplitude_poles '
fits=' ../minimise_chipt_su3_op4_mean.min.xml '
masses=' ../masses.phys.xml '
inifile=' polefind.ini.xml '
cmd = exe+fits+masses+inifile

os.system(cmd)

