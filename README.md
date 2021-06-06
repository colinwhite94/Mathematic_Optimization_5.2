# Mathematic_Optimization_5.2
My Genetic Algorithm works, but then gets stuck in an infinite loop (which you will see when you run it) that I was never able to fully debug.

My Genetic Algorithm works, but then gets stuck in an infinite loop (which you will see when
you run it) that I was never able to fully debug.
My code works by first having a set search area with an upper and lower bound. Then my code
makes and initial array of guesses (parents) inside that search area. The objective function is
called and the parent coordinates are evaluated with the objective function. Each of those
function evaluations are evaluated for the “fitness” or for which one is closest to the minimum.
That array of corresponding finesses is then normalized. The next step is spacing those finesse’s
out in a “Roulette wheel” where they are sequentially summed up, creating spacing between 0
and 1. These form the divisions on the roulette wheel. The rou() function “spins the roulette
wheel” by making a random number between 0 and 1, selecting the corresponding value on the
wheel, and adding the corresponding parent coordinate to a “mating pool array”. This array of
the matting pool then produces children with a weighted linear crossover. This array of children
is then mutated slightly to create serendipity in the system. This new, mutated child array set as
the new parent array and is fed back into the start of the Genetic Algorithm. This algorithm is
supposed to repeat a set number of times, but gets stuck in an infinite loop as mentioned before.
While looking at the infinitely scrolling output, the population does seem to converge at the
correct X* temporarily, but then usually shoots far off. I believe this may be due to the crude
nature of my mutation syntax.
I heavily commented my code for your convenience in deciding how much of 5.2 I completed. I
am 95% confident that I completed between 85-95% of the code to make a GA work flawlessly.
