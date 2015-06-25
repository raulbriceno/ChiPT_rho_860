import os

exe = '~/arch/scattering/master/bin/fit_spectrum '

input_file=' minimise_chipt_su3_op4.ini.xml '

mass_file=' ../masses.ini.xml '

"""to run Dave's spec list"""
spec_list=' ../djwilson_spec_list/spec_final_elastic.list'

"""to run my spec list"""
spec_list=' ../spec_final_elastic.list'

rel_dir=' /'

cmd=exe+input_file+mass_file+spec_list+rel_dir
print cmd

os.system(cmd)

