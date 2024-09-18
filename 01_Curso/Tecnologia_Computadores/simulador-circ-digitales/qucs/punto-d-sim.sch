<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,884,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-d-sim.dat>
  <DataDisplay=punto-d-sim.dpl>
  <OpenDisplay=1>
  <Script=punto-d-sim.m>
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
  <DigiSource S1 1 80 100 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 80 250 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 80 400 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <Inv Y1 1 190 250 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y2 1 180 400 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <AND Y3 1 370 340 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <AND Y4 1 370 150 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <OR Y5 1 510 260 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 60 470 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
</Components>
<Wires>
  <80 250 160 250 "" 0 0 0 "">
  <80 400 150 400 "" 0 0 0 "">
  <220 250 220 330 "" 0 0 0 "">
  <220 330 340 330 "" 0 0 0 "">
  <210 350 210 400 "" 0 0 0 "">
  <210 350 340 350 "" 0 0 0 "">
  <80 100 80 140 "" 0 0 0 "">
  <80 140 340 140 "" 0 0 0 "">
  <220 160 220 250 "" 0 0 0 "">
  <220 160 340 160 "" 0 0 0 "">
  <400 150 400 250 "" 0 0 0 "">
  <400 250 480 250 "" 0 0 0 "">
  <400 270 400 340 "" 0 0 0 "">
  <400 270 480 270 "" 0 0 0 "">
  <80 100 80 100 "W" 110 70 0 "">
  <80 250 80 250 "X" 110 220 0 "">
  <80 400 80 400 "Z" 110 370 0 "">
  <540 260 540 260 "i" 570 230 0 "">
</Wires>
<Diagrams>
  <Truth 620 387 224 207 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 1 315 0 225 "" "" "">
	<"w.X" #0000ff 0 3 0 0 0>
	<"x.X" #0000ff 0 3 0 0 0>
	<"z.X" #0000ff 0 3 0 0 0>
	<"i.X" #0000ff 0 3 0 0 0>
  </Truth>
</Diagrams>
<Paintings>
</Paintings>
