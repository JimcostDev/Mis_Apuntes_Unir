<Qucs Schematic 0.0.18>
<Properties>
  <View=0,0,930,800,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-d.dat>
  <DataDisplay=punto-d.dpl>
  <OpenDisplay=1>
  <Script=punto-d.m>
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
  <DigiSource S1 1 90 120 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 90 220 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 90 340 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <Inv Y1 1 190 120 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <AND Y2 1 350 170 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <OR Y3 1 450 330 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y4 1 590 320 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 110 420 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
</Components>
<Wires>
  <90 120 160 120 "" 0 0 0 "">
  <220 120 220 160 "" 0 0 0 "">
  <220 160 320 160 "" 0 0 0 "">
  <90 340 290 340 "" 0 0 0 "">
  <290 180 290 340 "" 0 0 0 "">
  <290 180 320 180 "" 0 0 0 "">
  <380 170 380 320 "" 0 0 0 "">
  <380 320 420 320 "" 0 0 0 "">
  <90 220 240 220 "" 0 0 0 "">
  <240 220 240 360 "" 0 0 0 "">
  <240 360 380 360 "" 0 0 0 "">
  <380 340 380 360 "" 0 0 0 "">
  <380 340 420 340 "" 0 0 0 "">
  <480 320 480 330 "" 0 0 0 "">
  <480 320 560 320 "" 0 0 0 "">
  <90 120 90 120 "W" 120 90 0 "">
  <90 220 90 220 "X" 120 190 0 "">
  <90 340 90 340 "Z" 120 310 0 "">
  <620 320 620 320 "i" 650 290 0 "">
</Wires>
<Diagrams>
  <Truth 490 250 218 190 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 1 315 0 225 "" "" "">
	<"w.X" #0000ff 0 3 0 0 0>
	<"x.X" #0000ff 0 3 0 0 0>
	<"z.X" #0000ff 0 3 0 0 0>
	<"i.X" #0000ff 0 3 0 0 0>
  </Truth>
</Diagrams>
<Paintings>
</Paintings>
