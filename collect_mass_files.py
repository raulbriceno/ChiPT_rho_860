import os 

list0=[['T1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p000-T1mP-wKK.t29/t06/MassJackFiles/mass_t0_6_reorder_state0.jack'],['T1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p000-T1mP-wKK.t29/t06/MassJackFiles/mass_t0_6_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p100-D4A1P-wKK.short.redo/t09/MassJackFiles/mass_t0_9_reorder_state0.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p100-D4A1P-wKK.short.redo/t09/MassJackFiles/mass_t0_9_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p100-D4A1P-wKK.short.redo/t09/MassJackFiles/mass_t0_9_reorder_state2.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p100-D4E2P.short/t09/MassJackFiles/mass_t0_9_reorder_state0.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p100-D4E2P.short/t09/MassJackFiles/mass_t0_9_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2A1P-wKK.short.lessproj/t08/MassJackFiles/mass_t0_8_reorder_state0.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2A1P-wKK.short.lessproj/t08/MassJackFiles/mass_t0_8_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2A1P-wKK.short.lessproj/t08/MassJackFiles/mass_t0_8_reorder_state2.jack'],['B1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2B1P/t08/MassJackFiles/mass_t0_8_reorder_state0.jack'],['B1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2B1P/t08/MassJackFiles/mass_t0_8_reorder_state1.jack'],['B2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p110-D2B2P.tmax29/t06/MassJackFiles/mass_t0_6_reorder_state0.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p111-D3A1P-wKK.short/t07/MassJackFiles/mass_t0_7_reorder_state0.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p111-D3A1P-wKK.short/t07/MassJackFiles/mass_t0_7_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p111-D3A1P-wKK.short/t07/MassJackFiles/mass_t0_7_reorder_state2.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p111-D3E2P/t07/MassJackFiles/mass_t0_7_reorder_state0.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p111-D3E2P/t07/MassJackFiles/mass_t0_7_reorder_state1.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p200-D4A1P.tmax27/t09/MassJackFiles/mass_t0_9_reorder_state0.jack'],['A1','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p200-D4A1P.tmax27/t09/MassJackFiles/mass_t0_9_reorder_state1.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p200-D4E2P.tmax25/t07/MassJackFiles/mass_t0_7_reorder_state0.jack'],['E2','/work/JLabLQCD/LHPC/Spectrum/Clover/NF2+1/szscl21_32_256_b1p50_t_x4p300_um0p0860_sm0p0743_n1p265/redstar/rho/fits_djw/p200-D4E2P.tmax25/t07/MassJackFiles/mass_t0_7_reorder_state1.jack']]


cmd='mkdir masses_jack'
os.system(cmd)

for n0 in range(len(list0)):
  irrep=list0[n0][0]
  filename=list0[n0][1]
  print ""
  print n0
  #tmp0 has the form "p000-T1mP-wKK.t29"
  tmp0=filename.split('/')[11]
  mom=tmp0.split('-')[0]
  print tmp0


  #tmp1 has the form "mass_t0_6_reorder_state0.jack"
  tmp1=filename.split('/')[-1]
  print tmp1
  tmp1=tmp1.split('.')[0]
  state_num=tmp1.split('_')[-1]

  final_filename=irrep+"_"+mom+"_"+state_num


  print final_filename

  cmd='cp '+filename+' masses_jack/'+final_filename
  os.system(cmd)  

