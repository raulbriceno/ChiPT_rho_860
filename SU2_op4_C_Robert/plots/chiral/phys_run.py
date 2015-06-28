import os

##here are the elements of the execution 




exe="~/bin/make_plots "
mean_vals=" minimise_chipt_su3_op4_mean.Andre_scale.min.xml "
masses= " masses.phys.Andre_scale.xml "
control=" plot_controls.chipt_su3_op4.ini.xml "

cmd=exe+mean_vals+masses+control

os.system(cmd)

