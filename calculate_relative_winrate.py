import glob
import os
import pandas as pd
from collections import Counter
from deck_class_with_winrate import Deck_winrate

# 1. Load decks from directory
deck_names = glob.glob("manual decks/*.txt")
deck_library = []

for filename in deck_names:
    with open(filename, 'r', encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    # Extract metadata from header lines
    player_name = lines[0].split(":", 1)[1].strip()

    # record: 14-2-1 -> wins: 14, losses: 1
    wins, losses, _ = lines[1].split(":", 1)[1].strip().split("-")
    wins = int(wins)
    losses = int(losses)
    player_score = wins - losses

    standing = int(lines[2].split(":", 1)[1].strip())
    
    # Parse card lines into (quantity, card_name) tuples
    card_tuples = []
    for card_line in lines[3:]:
        parts = card_line.split(' ', 1)
        # Check if line starts with a digit to skip section headers ("MainDeck", "Sideboard")
        if parts[0].isdigit():
            quantity = int(parts[0])
            card_name = parts[1]
            card_tuples.append((quantity, card_name))
            
    # Create Deck instance
    new_deck = Deck_winrate(
        name=player_name, 
        cards=card_tuples,
        wins=wins,
        losses=losses,
        player_score=player_score
    )
    deck_library.append(new_deck)

print(f"Loaded {len(deck_library)} decks into memory!\n")

# 2. Track total scores and total copies across all decks
card_scores = Counter()
card_counts = Counter()

for deck in deck_library:
    for quantity, card_name in deck.cards:
        card_scores[card_name] += (quantity * deck.player_score)
        card_counts[card_name] += quantity

# 3. Calculate Relative Point Values and filter out outliers (3 copies or less)
data = []
for card_name, total_score in card_scores.items():
    total_copies = card_counts[card_name]
    
    # Skip cards with 3 or fewer copies
    if total_copies <= 9:
        continue
        
    relative_value = round(total_score / total_copies, 2)
    data.append({
        "Card Name": card_name,
        "Total Copies": total_copies,
        "Total Score": total_score,
        "Relative Value": relative_value
    })

# Convert to pandas DataFrame and sort by Relative Value
df_cards = pd.DataFrame(data)
df_cards = df_cards.sort_values(by="Relative Value", ascending=False).reset_index(drop=True)

print("=== CARD RELATIVE VALUES (Filtered: >3 Copies) ===")
print(df_cards)

# 4. Ensure output directory exists and write to text file
os.makedirs("manualdecksoutput", exist_ok=True)
output_filepath = "manualdecksoutput/master_card_relative_scores.txt"

with open(output_filepath, "w", encoding="utf-8") as file:
    file.write("=== MASTER CARD RELATIVE SCORES (Filtered: >3 Copies) ===\n")
    file.write(f"Total Unique Cards (after filtering): {len(df_cards)}\n")
    file.write("=" * 55 + "\n\n")
    file.write(f"{'Rel Val':>8}  {'Copies':>6}  {'Total Pts':>10}  {'Card Name'}\n")
    file.write("-" * 55 + "\n")
    
    for _, row in df_cards.iterrows():
        file.write(
            f"{row['Relative Value']:>8.2f}  "
            f"{row['Total Copies']:>6}x  "
            f"{row['Total Score']:>10}  "
            f"{row['Card Name']}\n"
        )

print(f"\nSuccessfully saved filtered master relative card scores to {output_filepath}!")