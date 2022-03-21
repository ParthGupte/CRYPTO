import numpy as np
from inverse import mod_inverse
from modmatrices import *
import copy

ASCII = [chr(i) for i in range(128)]

q = 127

def convert(str) :
    converted = []
    
    for char in str :
        converted.append(ASCII.index(char))
    
    return converted

def reverse_convert(indices) :
    converted = ""

    for code in indices :
        converted += ASCII[code]

    return converted

def space_remove(str) :
    edited = ""

    for char in str :
        if not(char == " " or char == "\n") :
            edited += char

    return edited

p1 = '''Figure 1 represents the Tradesman as you would see him while you were
bending over him from above; figures 2 and 3 represent the Tradesman,
as you would see him if your eye were close to the level, or all but on
the level of the table; and if your eye were quite on the level of the
table (and that is how we see him in Flatland) you would see'''

# len(p1) = 343

p2 = '''Only by the sound of the voice could
sex or age be distinguished.  Moreover, as each individual occupied the
whole of the narrow path, so to speak, which constituted his Universe,
and no one could move to the right or left to make way for passers by,
it followed that no Linelander could ever pass another.  Once
neighbours, always neighbours.'''

# len(p2) = 343

p3 = '''I descended here, I saw your four Sons, the Pentagons, each in his
apartment, and your two Grandsons the Hexagons; I saw your youngest
Hexagon remain a while with you and then retire to his room, leaving
you and your Wife alone.  I saw your Isosceles servants, three in
number, in the kitchen at supper, and the little Page in the scullery.'''

# len(p3) = 340

p4 = '''No, no, my Lord; we Squares
are better advised, and are as well aware of your Lordship that a
Woman, though popularly called a Straight Line, is, really and
scientifically, a very thin Parallelogram, possessing Two Dimensions,
like the rest of us, viz., length and breadth (or thickness).

Stranger.  But the very fact that a Line'''

# len(p4) = 330

p5 = '''The rough diagram given above will make it
clear to any Spaceland child that the Sphere, ascending in the three
positions indicated there, must needs have manifested himself to me, or
to any Flatlander, as a Circle, at first of full size, then small, and
at last very small indeed, approaching to a Point.  But to me, although
I saw the facts before'''

# len(p5) = 349

p6 = '''It was in vain.  I brought my hardest right angle into violent
collision with the Stranger, pressing on him with a force sufficient to
have destroyed any ordinary Circle:  but I could feel him slowly and
unarrestably slipping from my contact; not edging to the right nor to
the left, but moving somehow out of the world, and vanishing into
nothing.'''

# len(p6) = 348

p7 = '''shall be set down without alteration
of an iota; and let my Readers judge between me and Destiny.

The Sphere would willingly have continued his lessons by indoctrinating
me in the conformation of all regular Solids, Cylinders, Cones,
Pyramids, Pentahedrons, Hexahedrons, Dodecahedrons, and Spheres:  but I
ventured to interrupt him.'''

# len(p7) = 333

p8 = '''Monarch
could neither turn to left nor right to discern it, and just as there
WAS close at hand, and touching my frame, the land of Three Dimensions,
though I, blind senseless wretch, had no power to touch it, no eye in
my interior to discern it, so of a surety there is a Fourth Dimension,
which my Lord perceives with the inner eye of thought.'''

# len(p8) = 345

p_list = [p1,p2,p3,p4,p5,p6,p7,p8]

def padder(str) :
    converted = convert(str)
    n = len(converted)

    if n%361 == 0:
        return converted

    else :
        return np.array(converted + [ q-1 for i in range(361 - (n%361)) ])

def blocks(str) :
    padded = padder(str)
    n = len(padded)//19
    return np.array([[padded[i*n+j] for j in range(19)] for i in range(n)] , dtype='int64')

def key_maker(p_,t_) :
    p = blocks(p_)
    t = blocks(t_)
    m = np.transpose(copy.deepcopy(t))
    b = np.transpose(copy.deepcopy(p))
    M = ModMatix(m,q)
    B = ModMatix(b,q)
    B.inv()
    B.multiply(M)
    return np.array(B.array , dtype='int64')

cypher = '''You're screwed. You might think that you're smart and you can figure it out, but you're royally screwed. The very fact that the cypher is this essay I wrote to tell you how screwed you are should be enough to convince you that you're screwed. No amount of brute-forcing will get you the answer because, you guessed it, we screwed you.
-Sincerely, Encryptosuarus'''
# len(cypher) = 361

key_list = [key_maker(p_list[i],cypher) for i in range(8)] # Final list of special keys
print(key_list)
