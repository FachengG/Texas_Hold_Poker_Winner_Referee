## Purpose
This script is designed for the purpose: fingerprint players' cards and use them to determine who is the winner.
## Feature
1. Use fingerprint to characterize player's cards.
2. Independent: does not require any python library. (random library is only used for test purpose. )
## Tech Details
1. The cards are defined as numbers from 0 to 51. 0 is the smallest card 2, and 12 is the largest card A. 
2. Transfer each player's card + public cards to a fingerprint "[Royal Flush, Straight Flush, Four of a kind, full house, flush, straight,three of a kind, two pair, one pair, high card]"
3. Compare the fingerprint to find the winner.
## Run the code:
```
python3 Referee.py
```
