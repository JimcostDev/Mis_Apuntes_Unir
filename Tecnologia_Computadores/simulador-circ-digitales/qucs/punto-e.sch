<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,800,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-e.dat>
  <DataDisplay=punto-e.dpl>
  <OpenDisplay=1>
  <Script=punto-e.m>
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
  <DigiSource S1 1 100 110 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 100 220 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 100 360 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <Inv Y1 1 190 220 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <OR Y2 1 280 330 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <AND Y3 1 410 240 -26 37 0 0 "3" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 140 440 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
</Components>
<Wires>
  <100 220 150 220 "" 0 0 0 "">
  <100 340 100 360 "" 0 0 0 "">
  <100 340 250 340 "" 0 0 0 "">
  <220 220 220 320 "" 0 0 0 "">
  <220 320 250 320 "" 0 0 0 "">
  <100 110 320 110 "" 0 0 0 "">
  <320 110 320 220 "" 0 0 0 "">
  <320 220 380 220 "" 0 0 0 "">
  <150 220 160 220 "" 0 0 0 "">
  <150 180 150 220 "" 0 0 0 "">
  <150 180 300 180 "" 0 0 0 "">
  <300 180 300 240 "" 0 0 0 "">
  <300 240 380 240 "" 0 0 0 "">
  <310 260 310 330 "" 0 0 0 "">
  <310 260 380 260 "" 0 0 0 "">
  <100 110 100 110 "X" 130 80 0 "">
  <100 220 100 220 "Y" 130 190 0 "">
  <100 360 100 360 "Z" 130 330 0 "">
  <440 240 440 240 "j" 470 210 0 "">
</Wires>
<Diagrams>
  <Truth 530 372 221 202 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 1 315 0 225 "" "" "">
	<"x.X" #0000ff 0 3 0 0 0>
	<"y.X" #0000ff 0 3 0 0 0>
	<"z.X" #0000ff 0 3 0 0 0>
	<"j.X" #0000ff 0 3 0 0 0>
  </Truth>
</Diagrams>
<Paintings>
</Paintings>
