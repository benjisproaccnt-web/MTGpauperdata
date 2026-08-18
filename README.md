# MTGpauperdata

The purpose of this project is to analyze game statistics from a Pauper Magic: The Gathering event using Paupergeddon 2026. More specifically, to figure out which cards either over performed, or under performed at the tournament. In order to do this,  

This involves: creating a class object "Deck_winrate" which will stores the cards in the deck as well as the winrate of the deck. The cards in the deck are then assigned a value based on the players record and averaged against the total number of copies in circulation.  

The first challenge involves playtime. Since players are able to drop the tournament at anytime, what we see is the players often with the worst winrates drop the tournament, while players with good winrates stay in. This means that the strongest decks are going to have the most playtime. In order to compare players, I use a "player score" which is simply wins - losses. Draws are ignored since they don't help in calculating which cards are better or worse than other ones. For example, a player with a record of 5 - 1 - 0 (5 wins, 1 draw, 0 losses) would be +5, while something like 0 - 2- 3 (0 wins, 1 draw, 3 losses) would be -3. 

A sample of 20 decks were selected. In order to get a wide variety of levels, since there were around 1000 entries, I sampled the deck every 50 entries, so 1, 50, 150, 200, etc. 

