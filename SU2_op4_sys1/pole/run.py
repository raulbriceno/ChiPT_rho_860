import os
exe='~/arch/scattering/master/bin/find_amplitude_poles '
fits=' ../minimise_chipt_su2_op4_mean.min.xml '
masses=' ../masses.ini.xml '
inifile=' polefind.ini.xml '
cmd = exe+fits+masses+inifile

os.system(cmd)

