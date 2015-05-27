#!/usr/bin/perl

die "Usage: $0 <spec.list> <J> <xi> <m1> <m2> <outfile prefix> <mean.min.xml> <masses.xml> \n\n" unless @ARGV == 8;

$exeold="/u/home/djwilson/Lattice/scattering-splines/build-gcc-48/built/bin/single_level_single_wave_elastic_delta";
$exe="/u/home/djwilson/Lattice/scattering_dudek_working/build-gcc-48/built/bin/elastic_phase_shift_ensem";

$spec_file = shift(@ARGV);
$J=shift(@ARGV);
$xi=shift(@ARGV);#3.444;
$m1=shift(@ARGV);#0.06906;
$m2=shift(@ARGV);#0.09698;
$out_pref=shift(@ARGV);
$mean_min_xml=shift(@ARGV);
$masses_xml=shift(@ARGV);

$maxE=0.21;#shift(@ARGV);
$minE=$m1+$m2;

$pid = $$;

open my $read_spec_file, '<', $spec_file or die "Could not open file $spec_file for reading: $!\n";

#prepare output files
$linereal = "Ecm,        qsq,         Re delta  deg";
$lineimag = "Ecm,        qsq,         Im delta  rad";
$linekcot = "Ecm,        qsq,         k2J+1 cot del";

$file_real = "$out_pref.delta.real.data";
$file_imag = "$out_pref.delta.imag.data";
$file_kcot = "$out_pref.delta.kcot.data";

#remove any files that we would otherwise overwrite
system("rm $file_real 2>/dev/null");
system("rm $file_imag 2>/dev/null");
system("rm $file_kcot 2>/dev/null");

my $OUT_REAL;
my $OUT_IMAG;
my $OUT_KCOT;

open $OUT_REAL, '>>', $file_real;
open $OUT_IMAG, '>>', $file_imag;
open $OUT_KCOT, '>>', $file_kcot;

#loop over lines in spec
print "Obtaining delta $J for: \n";

$fixed_higher = 0; #used to enable higher waves section below

while (my $line = <$read_spec_file>)
{ 
  # spec.list format: <mom> <irrep> <L> <ELabfile.jack>
  # phase shift input format: <ELabfile.jack> <mom> <irrep> <J> <L> <xi> <m1> m2> <fixed.delta>

  my @linevalues = split(/\s+/,$line);
  my $massjack = clean($linevalues[3]);
  my $mom =  $linevalues[0];
  my $irrep = $linevalues[1];
  my $vol = $linevalues[2];

  $newline = "$massjack $mom $irrep $J $vol $xi $m1 $m2";
 
  $file_elab = clean(`calcbc 'real(\"$massjack\")' | awk '\{print \$2\}'`);
  
  $volfac = ((2.0*3.141592653589)/(3.453*$vol))**2;
  
  if ($mom == "000") {$file_ecm = $file_elab;}
  if (($mom == "100") || ($mom == "001")) {$file_ecm = ($file_elab**2-1.0*$volfac)**(0.5);}
  if (($mom == "110") || ($mom == "011")) {$file_ecm = ($file_elab**2-2.0*$volfac)**(0.5);}
  if (($mom == "111"))                    {$file_ecm = ($file_elab**2-3.0*$volfac)**(0.5);}
  if (($mom == "200") || ($mom == "002")) {$file_ecm = ($file_elab**2-4.0*$volfac)**(0.5);}
  
  print $mom, " ", $file_ecm, " ", $file_elab, "\n";
   
  $fixed_string="";
  if ( $fixed_higher )
  {
    @Jha=(0);
    #print $Jha[0], " ", $Jha[1], "\n";
    
    &get_fixed_delta($file_ecm, @Jha);
    #system("cat fixed.delta");
    $newline = "$massjack $mom $irrep $J $vol $xi $m1 $m2 fixed.delta";
  }

  print $newline, "\n";  

  $tmp_file =  "/tmp/phase.tmp.$pid";
  system("$exe $newline &> $tmp_file");
  open my $read_tmp_file, '<', $tmp_file or die "Could not open file $tmp_file for reading: $!\n";
  
  #dumb declaration?
  $ecm = ""; $qsq = ""; $realdel = ""; $imagdel = ""; $kcotdel = "";
  
  while (my $tmp_line = <$read_tmp_file>)
  {
    if ( grep { /Ecm/ } $tmp_line ) { $ecm = clean($tmp_line); }
    if ( grep { /qsq/ } $tmp_line ) { $qsq = clean($tmp_line); }
    if ( grep { /real/ } $tmp_line ) { $realdel = clean($tmp_line) }
    if ( grep { /imag/ } $tmp_line ) { $imagdel = clean($tmp_line) }
    if ( grep { /2J/ } $tmp_line ) {$kcotdel = clean($tmp_line) }
  }
  
  $ecm =~ s/Ecm = //g;
  $qsq =~ s/qsq = //g;
  $realdel =~ s/real\(delta\) = //g;
  $realdel =~ s/ degrees = /   /g;
  $realdel =~ s/degrees//g;
    
  $imagdel =~ s/imag\(delta\) = //g;
  $kcotdel =~ s/k\^\(2J+1\)*cot\(delta\) = //g;
  
  #$linereal = "$ecm        $qsq         $realdel";
  $linereal = sprintf "%-3s %-2s %-2s   %-35s %-35s %-35s\n", $irrep, $mom, $vol, $ecm, $qsq, $realdel;
  $lineimag = sprintf "%-3s %-2s %-2s   %-35s %-35s %-35s\n", $irrep, $mom, $vol, $ecm, $qsq, $imagdel;
  $linekcot = sprintf "%-3s %-2s %-2s   %-35s %-35s %-35s\n", $irrep, $mom, $vol, $ecm, $qsq, $kcotdel;
  
  print { $OUT_REAL } $linereal;
  print { $OUT_IMAG } $lineimag;
  print { $OUT_KCOT } $linekcot;
  
  system("rm $tmp_file");
}

close $OUT_REAL;
close $OUT_IMAG;
close $OUT_KCOT;


#cut out points with large errors to make the plot sexier
my $trim_large_errors = "true";
my $err_cut = 180.0; #in degrees in this case
if ( $trim_large_errors ) 
{

  $sort_file = "$out_pref.sort.delta.real.data";
  my $sort_file_tmp = "$out_pref.sort.delta.real.data_tmp";

  system("cat $out_pref.delta.real.data | sort -n -k12 | awk '{print \$12}' > $sort_file_tmp");
  open my $read_sort_file_tmp, '<', $sort_file_tmp or die "Could not open file $sort_file_tmp for reading: $!\n";

  my $count = 0;
  my $thrown = 0;
  while (my $line = <$read_sort_file_tmp>)	
  {
    if (clean($line) < $err_cut){ $count = $count + 1; } 
    else { $thrown = $thrown +1 } 
  }

  print "Removing $thrown points with errors > $err_cut deg, retained $count points. \n";
  
  system("cat $out_pref.delta.real.data | sort -n -k12 | head -$count > $sort_file");
  system("rm $sort_file_tmp");

  &make_plot_xml($J);
  &get_model_phases($J);

  &make_gnu;
}


sub get_fixed_delta
{

  $Ecm = shift(@_);
  @Jm = @_;
  
  print " E=", $Ecm, "\n";
  
  #print "*", $Ecm, " ", $Jm, " ", $Jm[0], " ", $Jm[1], "\n"; 
  
  system("rm fixed.delta >/dev/null");
  foreach(@Jm)
  {
    my $J = $_;
    &make_plot_xml_ecm($Ecm, $J);

    #print $Ecm, " ", $J, "\n";

    $make_plots_exe = "/u/home/djwilson/Lattice/scattering_dudek_working/build-gcc-48/built/bin/make_plots";
    $plot_control = "/tmp/plot_ctrl_ecm_$pid.J$J.ini.xml";
    system("$make_plots_exe $mean_min_xml $masses_xml $plot_control &> /dev/null");

    my $ecm_file = "/tmp/phase_one_ecm_$pid.J$J.data";

    #system("cat $ecm_file");

    my $fixed_re_delta = clean(`cat $ecm_file | head -1 | awk '{print \$2}'`)*180.0/3.141592653589;
    my $fixed_im_delta = clean(`cat $ecm_file | head -1 | awk '{print \$4}'`)*180.0/3.141592653589;

    #system("echo \"$J $fixed_re_delta $fixed_im_delta  deg\" ");   
    system("echo \"$J $fixed_re_delta $fixed_im_delta  deg\" >> fixed.delta") ;  
  }
  system("cat fixed.delta");
}


sub get_model_phases
{
  my $Jp = shift(@_);
  $make_plots_exe = "/u/home/djwilson/Lattice/scattering_dudek_working/build-gcc-48/built/bin/make_plots";
  $plot_control = "/tmp/plot_ctrl_$pid.J$Jp.ini.xml";
  system("$make_plots_exe $mean_min_xml $masses_xml $plot_control");
}


sub make_plot_xml
{
  my $outfile = "fit_phase.J$J.data";
  my $J = shift(@_);
  open(XML, "> /tmp/plot_ctrl_$pid.J$J.ini.xml");
  print XML "<\?xml version=\"1.0\"\?>\n";
  print XML "<Plots>\n";
  print XML "  <version>1</version>\n";
  print XML "  <PartialWaves>\n";
  print XML "    <elem>\n";
  print XML "      <J>$J</J>\n";
  print XML "      <plot>one_channel_elastic_delta</plot>\n";
  print XML "      <control>\n";
  print XML "        <E_limits>$minE $maxE</E_limits>\n";
  print XML "        <npts>1200</npts>\n";
  print XML "        <phase_range>0 3.14159</phase_range>\n"; #needs to be fixed somehow
  print XML "      </control>\n";
  print XML "      <filename>$outfile</filename>\n";
  print XML "    </elem>\n";
  print XML "  </PartialWaves>\n";
  print XML "</Plots>\n";
}


sub make_plot_xml_ecm #input Ecm, J
{
  my $Ecmm = shift(@_);
  my $Ecmp = $Ecmm+2.e-6;
  my $J = shift(@_);
  
  print " E=", $Ecmm, " ", $Ecmp, "\n";
  
  my $outfile = "/tmp/phase_one_ecm_$pid.J$J.data";
  open(XML, "> /tmp/plot_ctrl_ecm_$pid.J$J.ini.xml");
  print XML "<\?xml version=\"1.0\"\?>\n";
  print XML "<Plots>\n";
  print XML "  <version>1</version>\n";
  print XML "  <PartialWaves>\n";
  print XML "    <elem>\n";
  print XML "      <J>$J</J>\n";
  print XML "      <plot>two_channel_delta_delta_eta</plot>\n";
  print XML "      <control>\n";
  print XML "        <E_limits>$Ecmm $Ecmp</E_limits>\n";
  print XML "        <npts>2</npts>\n";
  print XML "        <phase_range>0 3.14159</phase_range>\n"; #needs to be fixed somehow
  print XML "      </control>\n";
  print XML "      <filename>$outfile</filename>\n";
  print XML "    </elem>\n";
  print XML "  </PartialWaves>\n";
  print XML "</Plots>\n";
}


sub clean 
{ 
  my $text = shift;
  $text =~ s/\n//g;
  $text =~ s/\r//g;
  return $text;
}


#Adapted from Z_histogram.pl by JJD.
sub make_gnu {
    open(GNU, "> /tmp/phase_plot_$pid.gnu");
    print GNU "set xzeroaxis\n";
    print GNU "set yrange [-0.01:180]\n";
    print GNU "plot \'$sort_file\' u 4:10:6:12 w xyerrorbars,";
    print GNU "\'$sort_file\' u 4:13:6:15 w xyerrorbars lc 1,";
    print GNU "\'fit_phase.J$J.data\' u 1:(180*\$2/3.14159) w l,";
    print GNU "\'fit_phase.J$J.data\' u 1:(180*(\$2+\$3)/3.14159) w l lc 3,";
    print GNU "\'fit_phase.J$J.data\' u 1:(180*(\$2-\$3)/3.14159) w l lc 3\n";
    print GNU "\n pause -1\n";

# active this to keep a postscript file
#    print GNU "set xrange[-0.01:($xmax+2)]\n";
#    print GNU "set term postscript enhanced solid color eps\n";
#    print GNU "set out \"$out_pref.ps\"\n";
#    print GNU "replot\n";

    close(GNU);

    system("gnuplot -geometry 900x600 -persist /tmp/phase_plot_$pid.gnu");
    system("rm /tmp/phase_plot_$pid.*");
}


exit(0);

