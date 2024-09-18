<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-e-sim.dat>
  <DataDisplay=punto-e-sim.dpl>
  <OpenDisplay=1>
  <Script=punto-e-sim.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Título>
  <FrameText1=Dibujado por:>
  <FrameText2=Fecha:>
  <FrameText3=Revisión:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <DigiSource S1 1 120 100 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 120 210 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 120 350 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <AND Y1 1 310 210 -26 37 0 0 "3" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 230 440 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
</Components>
<Wires>
  <120 100 240 100 "" 0 0 0 "">
  <240 100 240 190 "" 0 0 0 "">
  <240 190 280 190 "" 0 0 0 "">
  <120 210 280 210 "" 0 0 0 "">
  <120 350 250 350 "" 0 0 0 "">
  <250 230 250 350 "" 0 0 0 "">
  <250 230 280 230 "" 0 0 0 "">
  <120 100 120 100 "X" 150 70 0 "">
  <120 210 120 210 "Y" 150 180 0 "">
  <120 350 120 350 "Z" 150 320 0 "">
  <340 210 340 210 "j" 370 180 0 "">
</Wires>
<Diagrams>
  <Truth 470 317 256 217 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 1 315 0 225 "" "" "">
	<"x.X" #0000ff 0 3 0 0 0>
	<"y.X" #0000ff 0 3 0 0 0>
	<"z.X" #0000ff 0 3 0 0 0>
	<"j.X" #0000ff 0 3 0 0 0>
  </Truth>
</Diagrams>
<Paintings>
</Paintings>
