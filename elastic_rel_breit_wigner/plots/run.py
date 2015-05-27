import os

##here are the elements of the execution 



exe="~/bin/make_plots "
mean_vals=" ../minimise_BW_mean.min.xml "
masses= " ../../masses.ini.xml "
control=" plot_controls.J1.ini.xml "

cmd=exe+mean_vals+masses+control

os.system(cmd)

