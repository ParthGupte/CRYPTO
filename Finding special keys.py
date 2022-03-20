import numpy as np
from modmatrices import *

ASCII = [chr(i) for i in range(128)]

# 'book' is a literal with some text, what the text is isn't important

book = '''
You received this message because you are subscribed to the Google Groups "students2020" group.
To unsubscribe from this group and stop receiving emails from it, send an email to students2020+unsubscribe@students.iiserpune.ac.in.
To view this discussion on the web visit
Flatland by Edwin A. Abbott

1884



  To
  The Inhabitance of SPACE IN GENERAL
  And H.C. IN PARTICULAR

In such a country, you will perceive at once that it is impossible that
there should be anything of what you call a "solid" kind; but I dare
say you will suppose that we could at least distinguish by sight the
Triangles, Squares, and other figures, moving about as I have described
them.  On the contrary, we could see nothing of the kind, not at least
so as to distinguish one figure from another.  Nothing was visible, nor
could be visible, to us, except Straight Lines; and the necessity of
this I will speedily demonstrate.

Place a penny on the middle of one of your tables in Space; and leaning
over it, look down upon it.  It will appear a circle.

But now, drawing back to the edge of the table, gradually lower your
eye (thus bringing yourself more and more into the condition of the
inhabitants of Flatland), and you will find the penny becoming more and
more oval to your view, and at last when you have placed your eye
exactly on the edge of the table (so that you are, as it were, actually
a Flatlander) the penny will then have ceased to appear oval at all,
and will have become, so far as you can see, a straight line.

The same thing would happen if you were to treat in the same way a
Triangle, or a Square, or any other figure cut out from pasteboard.  As
soon as you look at it with your eye on the edge of the table, you will
find that it ceases to appear to you as a figure, and that it becomes
in appearance a straight line.  Take for example an equilateral
Triangle--who represents with us a Tradesman of the respectable class.
Figure 1 represents the Tradesman as you would see him while you were
bending over him from above; figures 2 and 3 represent the Tradesman,
as you would see him if your eye were close to the level, or all but on
the level of the table; and if your eye were quite on the level of the
table (and that is how we see him in Flatland) you would see nothing
but a straight line.

When I was in Spaceland I heard that your sailors have very similar
experiences while they traverse your seas and discern some distant
island or coast lying on the horizon.  The far-off land may have bays,
forelands, angles in and out to any number and extent; yet at a
distance you see none of these (unless indeed your sun shines bright
upon them revealing the projections and retirements by means of light
and shade), nothing but a grey unbroken line upon the water.

Well, that is just what we see when one of our triangular or other
acquaintances comes towards us in Flatland.  As there is neither sun

Meanwhile my wife was under a cloud.  All pleasures palled upon me; all
sights tantalized and tempted me to outspoken treason, because I could
not compare what I saw in Two Dimensions with what it really was if
seen in Three, and could hardly refrain from making my comparisons
aloud.  I neglected my clients and my own business to give myself to
the contemplation of the mysteries which I had once beheld, yet which I
could impart to no one, and found daily more difficult to reproduce
even before my own mental vision.  One day, about eleven months after
my return from Spaceland, I tried to see a Cube with my eye closed, but
failed; and though I succeeded afterwards, I was not then quite certain
(nor have I been ever afterwards) that I had exactly realized the
original.  This made me more melancholy than before, and determined me
to take some step; yet what, I knew not.  I felt that I would have been
willing to sacrifice my life for the Cause, if thereby I could have
produced conviction.  But if I could not convince my Grandson, how
could I convince the highest and most developed Circles in the land?

And yet at times my spirit was too strong for me, and I gave vent to
dangerous utterances.  Already I was considered heterodox if not
treasonable, and I was keenly alive to the danger of my position;
nevertheless I could not at times refrain from bursting out into
suspicious or half-seditious utterances, even among the highest
Polygonal or Circular society.  When, for example, the question arose
about the treatment of those lunatics who said that they had received
the power of seeing the insides of things, I would quote the saying of
an ancient Circle, who declared that prophets and inspired people are
always considered by the majority to be mad; and I could not help
occasionally dropping such expressions as "the eye that discerns the
interiors of things," and "the all-seeing land"; once or twice I even
let fall the forbidden terms "the Third and Fourth Dimensions." At
last, to complete a series of minor indiscretions, at a meeting of our
Local Speculative Society held at the palace of the Prefect
himself,--some extremely silly person having read an elaborate paper
exhibiting the precise reasons why Providence has limited the number of
Dimensions to Two, and why the attribute of omnividence is assigned to
the Supreme alone--I so far forgot myself as to give an exact account
of the whole of my voyage with the Sphere into Space, and to the
Assembly Hall in our Metropolis, and then to Space again, and of my
return home, and of everything that I had seen and heard in fact or
vision.  At first, indeed, I pretended that I was describing the
imaginary experiences of a fictitious person; but my enthusiasm soon
forced me to throw off all disguise, and finally, in a fervent
peroration, I exhorted all my hearers to divest themselves of prejudice
and to become believers in the Third Dimension.

Need I say that I was at once arrested and taken before the Council?

Next morning, standing in the very place where but a very few months
ago the Sphere had stood in my company, I was allowed to begin and to
continue my narration unquestioned and uninterrupted.  But from the
first I foresaw my fate; for the President, noting that a guard of the
better sort of Policemen was in attendance, of angularity little, if at
all, under 55 degrees, ordered them to be relieved before I began my
defence, by an inferior class of 2 or 3 degrees.  I knew only too well
what that meant.  I was to be executed or imprisoned, and my story was
to be kept secret from the world by the simultaneous destruction of the
officials who had heard it; and, this being the case, the President
desired to substitute the cheaper for the more expensive victims.

After I had concluded my defence, the President, perhaps perceiving
that some of the junior Circles had been moved by evident earnestness,
asked me two questions:--

1.  Whether I could indicate the direction which I meant when I used
the words "Upward, not Northward"?

2.  Whether I could by any diagrams or descriptions (other than the
enumeration of imaginary sides and angles) indicate the Figure I was
pleased to call a Cube?

I declared that I could say nothing more, and that I must commit myself
to the Truth, whose cause would surely prevail in the end.

The President replied that he quite concurred in my sentiment, and that
I could not do better.  I must be sentenced to perpetual imprisonment;
but if the Truth intended that I should emerge from prison and
evangelize the world, the Truth might be trusted to bring that result
to pass.  Meanwhile I should be subjected to no discomfort that was not
necessary to preclude escape, and, unless I forfeited the privilege by
misconduct, I should be occasionally permitted to see my brother who
had preceded me to my prison.

Seven years have elapsed and I am still a prisoner, and--if I except
the occasional visits of my brother--debarred from all companionship
save that of my jailers.  My brother is one of the best of Squares,
just, sensible, cheerful, and not without fraternal affection; yet I
confess that my weekly interviews, at least in one respect, cause me
the bitterest pain.  He was present when the Sphere manifested himself
in the Council Chamber; he saw the Sphere's changing sections; he heard
the explanation of the phenomena then give to the Circles.  Since that
time, scarcely a week has passed during seven whole years, without his
hearing from me a repetition of the part I played in that
manifestation, together with ample descriptions of all the phenomena in
Spaceland, and the arguments for the existence of Solid things
derivable from Analogy.  Yet--I take shame to be forced to confess
it--my brother has not yet grasped the nature of Three Dimensions, and
frankly avows his disbelief in the existence of a Sphere.

Hence I am absolutely destitute of converts, and, for aught that I can
see, the millennial Revelation has been made to me for nothing.
Prometheus up in Spaceland was bound for bringing down fire for
mortals, but I--poor Flatland Prometheus--lie here in prison for
bringing down nothing to my countrymen.  Yet I existing the hope that
these memoirs, in some manner, I know not how, may find their way to
the minds of humanity in Some Dimension, and may stir up a race of
rebels who shall refuse to be confined to limited Dimensionality.

That is the hope of my brighter moments.  Alas, it is not always so.
Heavily weights on me at times the burdensome reflection that I cannot
honestly say I am confident as to the exact shape of the once-seen,
oft-regretted Cube; and in my nightly visions the mysterious precept,
"Upward, not Northward," haunts me like a soul-devouring Sphinx.  It is
part of the martyrdom which I endure for the cause of Truth that there
are seasons of mental weakness, when Cubes and Spheres flit away into
the background of scarce-possible existences; when the Land of Three
Dimensions seems almost as visionary as the Land of One or None; nay,
when even this hard wall that bars me from my freedom, these very
tablets on which I am writing, and all the substantial realities of
Flatland itself, appear no better than the offspring of a diseased
imagination, or the baseless fabric of a dream.


***


PREFACE TO THE SECOND AND REVISED EDITION, 1884.  BY THE EDITOR


If my poor Flatland friend retained the vigour of mind which he enjoyed
when he began to compose these Memoirs, I should not now need to
represent him in this preface, in which he desires, fully, to return
his thanks to his readers and critics in Spaceland, whose appreciation
has, with unexpected celerity, required a second edition of this work;
secondly, to apologize for certain errors and misprints (for which,
however, he is not entirely responsible); and, thirdly, to explain one
or two misconceptions.  But he is not the Square he once was.  Years of
imprisonment, and the still heavier burden of general incredulity and
mockery, have combined with the thoughts and notions, and much also of
the terminology, which he acquired during his short stay in spaceland.
He has, therefore, requested me to reply in his behalf to two special
objections, one of an intellectual, the other of a moral nature.

The first objection is, that a Flatlander, seeing a Line, sees
something that must be THICK to the eye as well as LONG to the eye
(otherwise it would not be visible, if it had not some thickness); and
consequently he ought (it is argued) to acknowledge that his countrymen
are not only long and broad, but also (though doubtless to a very
slight degree) THICK or HIGH.  This objection is plausible, and, to
Spacelanders, almost irresistible, so that, I confess, when I first
heard it, I knew not what to reply.  But my poor old friend's answer
appears to me completely to meet it.

"I admit," said he--when I mentioned to him this objection--"I admit
the truth of your critic's facts, but I deny his conclusions.  It is
true that we have really in Flatland a Third unrecognized Dimension
called 'height,' just as it also is true that you have really in
Spaceland a Fourth unrecognized Dimension, called by no name at
present, but which I will call 'extra-height.'  But we can no more take
cognizance of our 'height' than you can of your 'extra-height.'  Even
I--who have been in Spaceland, and have had the privilege of
understanding for twenty-four hours the meaning of 'height'--even I
cannot now comprehend it, nor realize it by the sense of sight or by
any process of reason; I can but apprehend it by faith.

"The reason is obvious.  Dimension implies direction, implies
measurement, implies the more and the less.  Now, all our lines are
EQUALLY and INFINITESIMALLY thick (or high, whichever you like);
consequently, there is nothing in them to lead our minds to the
conception of that Dimension.  No 'delicate micrometer'--as has been
suggested by one too hasty Spaceland critic--would in the least avail
us; for we should not know WHAT TO MEASURE, NOR IN WHAT DIRECTION.
When we see a Line, we see something that is long and BRIGHT;
BRIGHTNESS, as well as length, is necessary to the existence of a Line;
if the brightness vanishes, the Line is extinguished.  Hence, all my
Flatland friends--when I talk to them about the unrecognized Dimension
which is somehow visible in a Line--say, 'Ah, you mean BRIGHTNESS': and
when I reply, 'No, I mean a real Dimension,' they at once retort, 'Then
measure it, or tell us in what direction it extends'; and this silences
me, for I can do neither.  Only yesterday, when the Chief Circle (in
other words our High Priest) came to inspect the State Prison and paid
me his seventh annual visit, and when for the seventh time he put me
the question, 'Was I any better?'  I tried to prove to him that he was
'high,' as well as long and broad, although he did not know it.  But
what was his reply?  'You say I am "high"; measure my "high-ness" and I
will believe you.'  What could I do?  How could I meet his challenge?
I was crushed; and he left the room triumphant.

"Does this still seem strange to you?  Then put yourself in a similar
position.  Suppose a person of the Fourth Dimension, condescending to
visit you, were to say, 'Whenever you open your eyes, you see a Plane
(which is of Two Dimensions) and you INFER a Solid (which is of Three);
but in reality you also see (though you do not recognize) a Fourth
Dimension, which is not colour nor brightness nor anything of the kind,
but a true Dimension, although I cannot point out to you its direction,
nor can you possibly measure it.' What would you say to such a visitor?
Would not you have him locked up?  Well, that is my fate:  and it is as
natural for us Flatlanders to lock up a Square for preaching the Third
Dimension, as it is for you Spacelanders to lock up a Cube for
preaching the Fourth.  Alas, how strong a family likeness runs through
blind and persecuting humanity in all Dimensions!  Points, Lines,
Squares, Cubes, Extra-Cubes--we are all liable to the same errors, all
alike the Slaves of our respective Dimensional prejudices, as one of
our Spaceland poets has said--


     'One touch of Nature makes all worlds akin.'" (footnote 1)


On this point the defence of the Square seems to me to be impregnable.
I wish I could say that his answer to the second (or moral) objection
was equally clear and cogent.  It has been objected that he is a
woman-hater; and as this objection has been vehemently urged by those
whom Nature's decree has constituted the somewhat larger half of the
Spaceland race, I should like to remove it, so far as I can honestly do
so.  But the Square is so unaccustomed to the use of the moral
terminology of Spaceland that I should be doing him an injustice if I
were literally to transcribe his defence against this charge.  Acting,
therefore, as his interpreter and summarizer, I gather that in the
course of an imprisonment of seven years he has himself modified his
own personal views, both as regards Women and as regards the Isosceles
or Lower Classes.  Personally, he now inclines to the opinion of the
Sphere (see page 86) that the Straight Lines are in many important
respects superior to the Circles.  But, writing as a Historian, he has
identified himself (perhaps too closely) with the views generally
adopted by Flatland, and (as he has been informed) even by Spaceland,
Historians; in whose pages (until very recent times) the destinies of
Women and of the masses of mankind have seldom been deemed worthy of
mention and never of careful consideration.

In a still more obscure passage he now desires to disavow the Circular
or aristocratic tendencies with which some critics have naturally
credited him.  While doing justice to the intellectual power with which
a few Circles have for many generations maintained their supremacy over
immense multitudes of their countrymen, he believes that the facts of
Flatland, speaking for themselves without comment on his part, declare
that Revolutions cannot always be suppressed by slaughter, and that
Nature, in sentencing the Circles to infecundity, has condemned them to
ultimate failure--"and herein," he says, "I see a fulfilment of the
great Law of all worlds, that while the wisdom of Man thinks it is
working one thing, the wisdom of Nature constrains it to work another,
and quite a different and far better thing." For the rest, he begs his
readers not to suppose that every minute detail in the daily life of
Flatland must needs correspond to some other detail in Spaceland; and
yet he hopes that, taken as a whole, his work may prove suggestive as
well as amusing, to those Spacelanders of moderate and modest minds
who--speaking of that which is of the highest importance, but lies
beyond experience--decline to say on the one hand, "This can never be,"
and on the other hand, "It must needs be precisely thus, and we know
all about it."


Footnote 1.  The Author desires me to add, that the misconceptions of
some of his critics on this matter has induced him to insert (on pp.
74 and 92) in his dialogue with the Sphere, certain remarks which have
a bearing on the point in question and which he had previously omitted
as being tedious and unnecessary.








End of the Project Gutenberg EBook of Flatland, by Edwin A. Abbott

*** END OF THIS PROJECT GUTENBERG EBOOK FLATLAND ***

***** This file should be named 97.txt or 97.zip *****
This and all associated files of various formats will be found in:
        https://www.gutenberg.org/9/97/



Updated editions will replace the previous one--the old editions
will be renamed.

Creating the works from public domain print editions means that no
one owns a United States copyright in these works, so the Foundation
(and you!) can copy and distribute it in the United States without
permission and without paying copyright royalties.  Special rules,
set forth in the General Terms of Use part of this license, apply to
copying and distributing Project Gutenberg-tm electronic works to
protect the PROJECT GUTENBERG-tm concept and trademark.  Project
Gutenberg is a registered trademark, and may not be used if you
charge for the eBooks, unless you receive specific permission.  If you
do not charge anything for copies of this eBook, complying with the
rules is very easy.  You may use this eBook for nearly any purpose
such as creation of derivative works, reports, performances and
research.  They may be modified and printed and given away--you may do
practically ANYTHING with public domain eBooks.  Redistribution is
subject to the trademark license, especially commercial
redistribution.



*** START: FULL LICENSE ***

THE FULL PROJECT GUTENBERG LICENSE
PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg-tm mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase "Project
Gutenberg"), you agree to comply with all the terms of the Full Project
Gutenberg-tm License (available with this file or online at
https://gutenberg.org/license).


Section 1.  General Terms of Use and Redistributing Project Gutenberg-tm
electronic works

1.A.  By reading or using any part of this Project Gutenberg-tm
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement.  If you do not agree to abide by all
the terms of this agreement, you must cease using and return or destroy
all copies of Project Gutenberg-tm electronic works in your possession.

Professor Michael S. Hart was the originator of the Project Gutenberg-tm
concept of a library of electronic works that could be freely shared
with anyone.  For thirty years, he produced and distributed Project
Gutenberg-tm eBooks with only a loose network of volunteer support.


Project Gutenberg-tm eBooks are often created from several printed
editions, all of which are confirmed as Public Domain in the U.S.
unless a copyright notice is included.  Thus, we do not necessarily
keep eBooks in compliance with any particular paper edition.


Most people start at our Web site which has the main PG search facility:

     https://www.gutenberg.org

This Web site includes information about Project Gutenberg-tm,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
Gutenberg_Flatland_Ettubrute.txt
Displaying Gutenberg_Flatland_Ettubrute.txt.'''

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

p1_ = '''I do not, of course, mean that there are not battles,
conspiracies, tumults, factions, and all those other phenomena which
are supposed to make History interesting; nor would I deny that the
strange mixture of the problems of life and the problems of
Mathematics, continually inducing conjecture and giving an opportunity
of immediate verification, imparts to our existence a zest which you in
Spaceland can hardly comprehend.'''

p1 = space_remove(p1_)

# len(p1) = 360

p2_ = '''Man, woman, child, thing--each as a
Point to the eye of a Linelander.  Only by the sound of the voice could
sex or age be distinguished.  Moreover, as each individual occupied the
whole of the narrow path, so to speak, which constituted his Universe,
and no one could move to the right or left to make way for passers by,
it followed that no Linelander could ever pass another.  Once
neighbours, always neighbours.  Neighbourhood with them was like
marriage with us.'''

p2 = space_remove(p2_)

# len(p2) = 382

p3_ = '''Stranger.  But not easily proved, you mean.  But I mean to prove mine.

When I descended here, I saw your four Sons, the Pentagons, each in his
apartment, and your two Grandsons the Hexagons; I saw your youngest
Hexagon remain a while with you and then retire to his room, leaving
you and your Wife alone.  I saw your Isosceles servants, three in
number, in the kitchen at supper, and the little Page in the scullery.
Then I came here, and how do you think I came?

I.  Through the roof, I suppose.'''

p3 = space_remove(p3_)

# len(p3) = 400

p4_ = '''I.  Your Lordship would treat me as if I were one of the vulgar who,
being ignorant of Mathematics, suppose that a Woman is really a
Straight Line, and only of One Dimension.  No, no, my Lord; we Squares
are better advised, and are as well aware of your Lordship that a
Woman, though popularly called a Straight Line, is, really and
scientifically, a very thin Parallelogram, possessing Two Dimensions,
like the rest of us, viz., length and breadth (or thickness).'''

p4 = space_remove(p4_)

#len(p4) = 382

p5_ = '''But to me, proficient though I was in Flatland Mathematics, it was by no
means a simple matter.  The rough diagram given above will make it
clear to any Spaceland child that the Sphere, ascending in the three
positions indicated there, must needs have manifested himself to me, or
to any Flatlander, as a Circle, at first of full size, then small, and
at last very small indeed, approaching to a Point.  But to me, although
I saw the facts before me, the causes were as dark as ever.'''

p5 = space_remove(p5_)

#len(p5) = 393

p6_ = '''It was in vain.  I brought my hardest right angle into violent
collision with the Stranger, pressing on him with a force sufficient to
have destroyed any ordinary Circle:  but I could feel him slowly and
unarrestably slipping from my contact; not edging to the right nor to
the left, but moving somehow out of the world, and vanishing into
nothing.  Soon there was a blank.  But still I heard the Intruder's
voice.

Sphere.  Why will you refuse to listen to reason?'''

p6 = space_remove(p6_)

#len(p6)  = 378

p7_ = '''The exact facts, the exact words,--and
they are burnt in upon my brain,--shall be set down without alteration
of an iota; and let my Readers judge between me and Destiny.

The Sphere would willingly have continued his lessons by indoctrinating
me in the conformation of all regular Solids, Cylinders, Cones,
Pyramids, Pentahedrons, Hexahedrons, Dodecahedrons, and Spheres:  but I
ventured to interrupt him.  Not that I was wearied of knowledge.'''

p7 = space_remove(p7_)

#len(p7) = 373

p8_ = '''But, just as
there WAS the realm of Flatland, though that poor puny Lineland Monarch
could neither turn to left nor right to discern it, and just as there
WAS close at hand, and touching my frame, the land of Three Dimensions,
though I, blind senseless wretch, had no power to touch it, no eye in
my interior to discern it, so of a surety there is a Fourth Dimension,
which my Lord perceives with the inner eye of thought.  And that it
must exist my Lord himself has taught me.'''

p8 = space_remove(p8_)

#len(p8) = 386

def padder(str) :
    converted = convert(str)
    n = len(converted)

    if n%400 == 0:
        return converted

    else :
        return np.array(converted + [ q-1 for i in range(400 - (n%400)) ])

def blocks(str) :
    padded = padder(str)
    n = len(padded)/400
    return [np.array([padded[i*n+j] for j in range(400)] for i in range(n))]

def key_maker(p_,t_) :
    p = padder(p_)
    t = padder(t_)
    BOOK = convert(book)
    m = np.transpose(np.array([t]+[[1-np.sign(i-j)**2 for j in range(400)] for i in range(1,400)] , dtype='int64'))
    b = np.array(np.identity(400) , dtype='int64')
    M = ModMatix(m,q)
    B = ModMatix(b,q)
    M.div(B)
    B.multiply(M)
    return B.array

K1 = key_maker(p1 , reverse_convert([1] + [0 for i in range(399)])) # Computation of K1 is where error is happening

# print(K1)



    

