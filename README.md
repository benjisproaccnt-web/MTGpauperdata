# MTG Pauper Deck Analysis

The purpose of this project is to analyze game statistics from a Pauper Magic: The Gathering event using Paupergeddon 2026. More specifically, to figure out which cards either over performed, or under performed at the tournament. In order to do this, the cards in a players deck are assigned a score, the total score is averaged across all copies of the card. This final score is the relative win rate for the card itself, showing whether it is associated more with over-performing or under-performing decks.  

First, a class object "Deck_winrate" is created which will stores the cards in the deck as well as the win rate of the deck. The cards in the deck are then assigned a value based on the players record and averaged against the total number of copies in circulation.  

The first challenge involves playtime. Since players are able to drop the tournament at anytime, what we see is the players often with the worst win rates drop the tournament, while players with good win rates stay in. This means that the strongest decks are going to have the most playtime. In order to compare players, I use a "player score" which is simply wins minus losses. Draws are ignored since they don't help in calculating which cards are better or worse than other ones. For example, a player with a record of 5 - 0 - 1 (5 wins, 1 loss, 0 draws) would be +5, while something like 0 - 2- 3 (0 wins, 2 losses, 3 draws) would be -2. 

A sample of 20 decks were selected. In order to get a wide variety of levels, since there were around 1000 entries, I sampled the deck every 50 entries, so 1, 50, 150, 200, etc. 

In order to ignore outliers, I also ignored any cards who had <10 copies, since the sample size was not large enough the get enough value. 



