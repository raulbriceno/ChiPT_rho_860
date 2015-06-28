import os

##here are the elements of the execution 




exe="~/bin/make_plots "
mean_vals=" minimise_chipt_su2_op4_mean.min.xml "
masses= " masses.phys.xml "
control=" plot_controls.chipt_su2_op4.ini.xml "

cmd=exe+mean_vals+masses+control

os.system(cmd)

