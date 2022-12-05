import secrets

DICE_COUNT = 5
words = 5
dice_rolls = []
word_list = []
#dictionary_ = { "11111": "a", "11112": "b", "11113":"c", ...}

for _ in range(words):
    dice = ''.join(str(secrets.randbelow(6) + 1) for _ in range(DICE_COUNT))
    dice_rolls.append(dice)

for i in dice_rolls:
    for k, v in dictionary_.items():
        if i == k:
            word_list.append(v)

final_passphrase = " ".join(word_list).replace(" ", "")