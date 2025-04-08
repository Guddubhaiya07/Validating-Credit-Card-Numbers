n = int(input())
allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']

for _ in range(n):
    digit_count = 0
    repeat_count = 1
    is_invalid = False
    card_number = input()

    # Step 1: Starts with 4, 5, or 6
    if card_number[0] not in ['4', '5', '6']:
        print('Invalid')
        continue

    # Step 2: Contains only digits or hyphens
    for ch in card_number:
        if ch not in allowed_characters:
            is_invalid = True
            break
        if ch != '-':
            digit_count += 1

    if is_invalid or digit_count != 16:
        print('Invalid')
        continue

    # Step 3: If hyphens are present, check format of groups
    if '-' in card_number:
        groups = card_number.split('-')
        if any(len(group) != 4 for group in groups):
            print('Invalid')
            continue
        card_number = ''.join(groups)  # Remove hyphens for repeat check

    # Step 4: Check for 4 or more repeated digits
    for i in range(len(card_number) - 1):
        if card_number[i] == card_number[i + 1]:
            repeat_count += 1
            if repeat_count == 4:
                is_invalid = True
                break
        else:
            repeat_count = 1

    if is_invalid:
        print('Invalid')
    else:
        print('Valid')
