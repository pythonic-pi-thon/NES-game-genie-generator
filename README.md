# NES-game-genie-generator
This is a utility made to generate "educated guesses" of game genie
codes that might produce interesting effects in NES games given a 
list of known, working codes as inputs. This is accomplished by 
splicing two codes together, decoding the result into an address
and value, then replacing the value with something random and 
re-encoding it. (please note that gamegenie.py -- obtainable from 
this repository (https://github.com/Jarhmander/gamegenie) -- is 
used to perform the decoding and encoding steps. It was not made
by me and is reused under MIT license. Refer to the "dependencies" 
section of this readme for more info). 

There are two main scripts: NES_game_genie_generator and 
NES_game_genie_list_gen. The one you choose to run will depend on 
whether you want to generate a few codes in random order or an 
exhaustive-ish, sorted, duplicate free text file containing the 
codes. Both of these are available as a .py file that can be run 
from the command line and as a .ipynb file that can be used with 
Jupyter notebook, based on your preferences. More about each one
follows:

NES_game_genie_generator is a script that generates NES codes for a 
game based on input of existing codes for that game. By default, it 
will read these from the file "source.txt", in which you should type 
your game genie codes one-to-a-line.

save as a text file, and put in your python root directory (most
installations will use C:/Users/(your name) by default).Once 
started, it will ask how many codes you wish to generate. This 
can be any postive integer, and they will be printed out after you 
press Enter. 

A sample "source.txt" file is provided that contains ~200 codes for
SMB1. These are all well-known codes that were compiled from various 
sites (mainly, https://themushroomkingdom.net/smb_ggcodes.shtml and 
https://www.consoledatabase.com/cheats/nes/supermariobros/) following
a Google search for "Super mario bros. Game Genie codes", and
allows for demonstration/evaluation without the need to compile one's
own list as well as documenting the codes that were used for 
development and testing.

NES_game_genie_list_gen is similar to NES_game_genie_generator with
one exception: it will run NES_game_genie_generator in a loop many 
times (the default is 300,000 times the number of codes in 
source.txt), remove duplicates, sort the list, and print the codes
alphabetically to the file "output.txt" (beware that if you already
have a file named output.txt in your python directory, it will 
REPLACE it, so be sure to move it elsewhere prior to running this).
This process will take several minutes but don't worry, it prints 
out its progress at regular intervals. This can be handy if you don't
want to run NES_game_genie_generator repeatedly and simply want a 
large list of most or all possible codes that you can search or pick
randomly from. 

Again, a sample "output.txt" is provided based on ~2 billion runs using 
the included "source.txt" file, and should provide both an idea of what 
such a result should look like as well as a searchable list of (untested) 
NES game genie codes for SMB1. 

==========================================================================

About Python: 
Please not that you'll need python installed to run this. If you
don't already have a python environment, I recommend
Anaconda/Jupyter notebook which can be obtained and used 
for free (https://www.anaconda.com/products/distribution).
 
Simply install it and move 
NES_game_genie_generator.ipynb, NES_game_genie_list_gen, and
gamegenie.py to your root directory (it'll use C:/Users/(your name) 
by default), open Jupyter notebook, click 
the name of whichever one you'd like to run, then click "run" at the 
top to start it.

===========================================================================

Dependencies: 
Please also note the part of this program that converts game genie codes 
to a memory address and value/vice versa was not made by me. This 
is carried out by the game genie decoding/encoding 
utility gamegenie.py (reused under MIT  license), which is required
as a dependency. Please esure it is present in python's root directory.
If not included with this script, you can download it here: 
(https://github.com/Jarhmander/gamegenie) just remember to change the 
"xrange" in line 16 to "range" if you wish for it to work in Python 3.
You may also wish to delete lines 56 - 58 as they raise an error that 
appears quite frequently but can be safely ignored. The copy of 
gamegenie.py included with this script has had these changes made in 
advance. 
