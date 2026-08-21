# MTG Pauper Deck Analysis

The purpose of this project is to analyze game statistics from a Pauper Magic: The Gathering event using Paupergeddon 2026. More specifically, to figure out which cards either over performed, or under performed at the tournament. In order to do this, the cards in a players deck are assigned a score, the total score is averaged across all copies of the card. This final score is the relative win rate for the card itself, showing whether it is associated more with over-performing or under-performing decks.  

First, a class object "Deck_winrate" is created which will stores the cards in the deck as well as the win rate of the deck. The cards in the deck are then assigned a value based on the players record and averaged against the total number of copies in circulation.  

The first challenge involves playtime. Since players are able to drop the tournament at anytime, what we see is the players often with the worst win rates drop the tournament, while players with good win rates stay in. This means that the strongest decks are going to have the most playtime. In order to compare players, I use a "player score" which is simply wins minus losses. Draws are ignored since they don't help in calculating which cards are better or worse than other ones. For example, a player with a record of 5 - 0 - 1 (5 wins, 1 loss, 0 draws) would be +5, while something like 0 - 2- 3 (0 wins, 2 losses, 3 draws) would be -2. 

A sample of 20 decks were selected. In order to get a wide variety of levels, since there were around 1000 entries, I sampled the deck every 50 entries, so 1, 50, 150, 200, etc. 

In order to ignore outliers, I also ignored any cards who had <10 copies, since the sample size was not large enough the get enough value. 

Looking at the top of the results:

 Rel Val  Copies   Total Pts  Card Name
-------------------------------------------------------
    4.75      16x          76  Drossforge Bridge
    4.64      11x          51  Krark-Clan Shaman
    4.33      12x          52  Twisted Landscape
    4.33      12x          52  Slagwoods Bridge
    4.33      12x          52  Cleansing Wildfire
    4.00      16x          64  Fanatical Offering
    3.73      15x          56  Duress
    3.60      20x          72  Refurbished Familiar

We see cards like "Drossforge Bridge", "Krark-Clan Shaman" which are used in artifact type decks, which performed very well for being an answer to go-wide stye decks and a sacrifice outlet for their artifacts.

At the bottom of the list is:

Rel Val  Copies  Total Pts  Card Name
-1.07    15x     -16        Thraben Charm
-1.29    14x     -18        Prismatic Strands
-1.54    13x     -20        Faithless Looting
-1.75    16x     -28        Lightning Bolt
-1.84    55x     -101       Mountain
-2.03    32x     -65        Plains
-2.33    12x     -28        Voldaren Epicure
-2.60    10x     -26        Candy Trail

  Which suggests that monowhite decks struggled at the tournament, with staples like Plains, Thraben Charm, and Prismatic Strands. 

  Interestingly, monocolor decks run significantly more basic lands than multicolor decks, which explains why the nonbasic lands have a high point value rating, while the basic lands have a low rating.  



