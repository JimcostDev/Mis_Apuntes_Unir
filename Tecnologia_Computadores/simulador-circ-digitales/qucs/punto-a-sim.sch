<Qucs Schematic 0.0.18>
<Properties>
  <View=0,-178,999,680,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-a-sim.dat>
  <DataDisplay=punto-a-sim.dpl>
  <OpenDisplay=1>
  <Script=punto-a-sim.m>
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
  <DigiSource S1 1 120 -110 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 110 0 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 110 100 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S4 1 110 210 -35 16 0 0 "4" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <Inv Y1 1 260 -110 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y2 1 250 0 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y3 1 250 100 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y4 1 240 210 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 700 -120 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
  <OR Y5 1 430 -70 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <OR Y7 1 530 50 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <AND Y8 1 430 140 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
</Components>
<Wires>
  <120 -110 230 -110 "" 0 0 0 "">
  <110 0 220 0 "" 0 0 0 "">
  <110 100 220 100 "" 0 0 0 "">
  <110 210 210 210 "" 0 0 0 "">
  <290 -110 290 -80 "" 0 0 0 "">
  <290 -80 400 -80 "" 0 0 0 "">
  <280 -60 280 0 "" 0 0 0 "">
  <280 -60 400 -60 "" 0 0 0 "">
  <460 -70 460 40 "" 0 0 0 "">
  <460 40 500 40 "" 0 0 0 "">
  <280 100 280 130 "" 0 0 0 "">
  <280 130 400 130 "" 0 0 0 "">
  <270 150 270 210 "" 0 0 0 "">
  <270 150 400 150 "" 0 0 0 "">
  <460 60 460 140 "" 0 0 0 "">
  <460 60 500 60 "" 0 0 0 "">
  <120 -110 120 -110 "X" 150 -140 0 "">
  <110 0 110 0 "Y" 140 -30 0 "">
  <110 100 110 100 "W" 140 70 0 "">
  <110 210 110 210 "Z" 150 180 0 "">
  <290 -110 290 -110 "Xnot" 320 -140 0 "">
  <280 0 280 0 "Ynot" 310 -30 0 "">
  <280 100 280 100 "Wnot" 310 70 0 "">
  <270 210 270 210 "Znot" 310 180 0 "">
  <560 50 560 50 "F" 590 20 0 "">
</Wires>
<Diagrams>
  <Truth 630 354 280 354 3 #c0c0c0 1 00 1 0 1 1 1 0 1 1 1 0 1 16 315 0 225 "" "" "">
	<"x.X" #0000ff 0 3 0 0 0>
	<"y.X" #0000ff 0 3 0 0 0>
	<"w.X" #0000ff 0 3 0 0 0>
	<"z.X" #0000ff 0 3 0 0 0>
	<"f.X" #0000ff 0 3 0 0 0>
  </Truth>
</Diagrams>
<Paintings>
</Paintings>