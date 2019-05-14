#import
library(Matrix)

#-------------------------------------------------------------------------------

#parameters
nbccol_lines <- 2
step <- 0.01
begin <- 0
end <- 200
color <- "red"

a <- matrix(c(-12, 12, 3, -3), nbccol_lines, nbccol_lines)

#-------------------------------------------------------------------------------

#points
vect <- matrix(list(), nrow = 1, ncol = (nbccol_lines*nbccol_lines))

for (i in seq(begin, end, by = step))
{
    m <- Matrix::expm(a*i)
    cpt <- 1
    
    for (j in 1:nbccol_lines)
    {
        for (k in 1:nbccol_lines)
        {
            vect[[1, cpt]] <- c(vect[[1, cpt]], m[j, k])
            cpt <- cpt + 1
        }
    }
}

x <- seq(begin, end, by = step)

#-------------------------------------------------------------------------------

#display
jpeg("graph.jpg")
plot(x, vect[[1, 1]], main = "Micro Project 1", "l", col = color, xlab = "Time",
    ylab = "Probability", xlim = c(begin, end*step), ylim = c(0,1))

for (i in 2:(nbccol_lines*nbccol_lines))
{
    lines(x, vect[[1, i]], col = color)
}

abline(v = 0:10,  lty = 2, col = "grey")
abline(h = 0:10,  lty = 2, col = "grey")
