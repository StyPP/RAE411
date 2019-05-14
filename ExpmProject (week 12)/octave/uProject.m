#parameters
nbcol_lines = 2;
step = 0.01;
begin = 0;
endm = 200;
color = "red";

a = [-12 12; 3 -3];

#-------------------------------------------------------------------------------

#points
vect = cell(nbcol_lines, nbcol_lines);

for i = begin:step:endm
    m = expm(a*i);
    cpt = 1;
    for j = 1:1:nbcol_lines
        for k = 1:1:nbcol_lines
            vect{cpt} = [vect{cpt} m(j, k)];
            cpt = cpt + 1;
        endfor
    endfor
endfor

x = begin:step:endm;

#-------------------------------------------------------------------------------

#display
h = figure();
plot(x, vect{1}, 'r');

for i = 2:1:(nbcol_lines * nbcol_lines)
    line(x, vect{i}, "color", "r");
endfor

xlabel ("Time");
ylabel ("Probability");
title ("Micro project 1");
xlim([0, 10])

saveas(h, "graph.pdf")
saveas(h, "graph.jpg")