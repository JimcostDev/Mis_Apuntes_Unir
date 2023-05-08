<Qucs Schematic 0.0.18>
<Properties>
  <View=0,-38,1062,596,1,0,0>
  <Grid=10,10,1>
  <DataSet=punto-a.dat>
  <DataDisplay=punto-a.dpl>
  <OpenDisplay=1>
  <Script=punto-a.m>
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
  <DigiSource S1 1 130 90 -35 16 0 0 "1" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S2 1 130 210 -35 16 0 0 "2" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S3 1 120 340 -35 16 0 0 "3" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <DigiSource S4 1 120 470 -35 16 0 0 "4" 1 "low" 0 "1ns; 1ns" 0 "1 V" 0>
  <OR Y2 1 270 410 -26 27 0 0 "2" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <.Digi Digi1 1 670 70 0 63 0 0 "TruthTable" 1 "10 ns" 0 "VHDL" 0>
  <AND Y1 1 320 130 -26 37 0 0 "3" 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
  <Inv Y4 1 470 140 -26 27 0 0 "1 V" 0 "0" 0 "10" 0 "old" 0>
</Components>
<Wires>
  <120 340 120 400 "" 0 0 0 "">
  <120 400 240 400 "" 0 0 0 "">
  <120 420 120 470 "" 0 0 0 "">
  <120 420 240 420 "" 0 0 0 "">
  <130 90 130 110 "" 0 0 0 "">
  <130 110 290 110 "" 0 0 0 "">
  <130 130 130 210 "" 0 0 0 "">
  <130 130 290 130 "" 0 0 0 "">
  <300 190 300 410 "" 0 0 0 "">
  <280 190 300 190 "" 0 0 0 "">
  <280 150 280 190 "" 0 0 0 "">
  <280 150 290 150 "" 0 0 0 "">
  <350 130 350 140 "" 0 0 0 "">
  <350 140 440 140 "" 0 0 0 "">
  <130 90 130 90 "X" 170 60 0 "">
  <130 210 130 210 "Y" 160 180 0 "">
  <120 340 120 340 "Z" 150 310 0 "">
  <120 470 120 470 "W" 150 440 0 "">
  <300 410 300 410 "ZorW" 330 380 0 "">
  <350 130 350 130 "XandYandZW" 380 100 0 "">
  <500 140 500 140 "F" 530 110 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
