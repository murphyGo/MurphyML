import random


def generate_random_text(size_in_kb):
    # Define characters for different byte sizes in UTF-8
    one_byte_chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    two_byte_chars = list("¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿")
    three_byte_chars = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん")
    four_byte_chars = list("😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚😜😝😛🤑🤗🤔🤐🤨😐😑😶😏😒😞😔😟😕🙁☹️")

    # Calculate the number of characters needed
    target_size = size_in_kb * 1024  # Convert KB to Bytes
    current_size = 0
    result = []

    while current_size < target_size:
        char_type = random.choice([1, 2, 3, 4])

        if char_type == 1:
            char = random.choice(one_byte_chars)
        elif char_type == 2:
            char = random.choice(two_byte_chars)
        elif char_type == 3:
            char = random.choice(three_byte_chars)
        elif char_type == 4:
            char = random.choice(four_byte_chars)

        char_size = len(char.encode('utf-8'))

        if current_size + char_size <= target_size:
            result.append(char)
            current_size += char_size

    return ''.join(result)


# Generate 512KB of random text
random_text = generate_random_text(512)

# Write to a file (optional)
with open('random_text_512kb.txt', 'w', encoding='utf-8') as file:
    file.write(random_text)

print(f"Generated text size: {len(random_text.encode('utf-8')) / 1024} KB")