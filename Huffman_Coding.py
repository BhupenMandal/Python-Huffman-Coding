import sys
global huff


def huffman_encoding(data):
    global huff
    huff = dict()
    for letter in data:
        huff[letter] = huff.get(letter, 0) + 1
    huff_tree = dict()
    temp_str = "1"
    sorted_huff_items = sorted(huff.items(), key=lambda x: x[1])
    for i in sorted_huff_items:
        huff_tree[i[0]] = temp_str
        temp_str = "0" + temp_str

    encode = str()
    for i in data:
        encode += huff_tree[i]
    return encode, huff_tree


def huffman_decoding(data, huff_tree):
    huff_dict = dict()
    for letter in huff_tree:
        huff_dict[tree[letter]] = letter
    # print(huff)
    temp = str()
    decode = str()
    for i in data:
        if i == "1":
            decode += huff_dict[temp + i]
            temp = str()
        else:
            temp += i
    return decode


if __name__ == "__main__":
    print("\nTest Case 1")
    a_great_sentence = "The bird is the word"

    print(f"Size: {sys.getsizeof(a_great_sentence)}")
    print(f"Content: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(f"Size of the encoded data: {sys.getsizeof(int(encoded_data, 2))}")
    print(f"Content of the encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the decoded data: {decoded_data}")

    print("\nTest Case 2")
    tongue_twister = "she sells seashells on the seashore"

    print(f"The size: {sys.getsizeof(tongue_twister)}")
    print(f"The content: {tongue_twister}")

    encoded_data, tree = huffman_encoding(tongue_twister)

    print(f"Size of the encoded data: {sys.getsizeof(int(encoded_data, 2))}")
    print(f"Content of the encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the decoded data: {decoded_data}")

    print("\nTest Case 3")
    empty_string = " "

    print(f"The size: {sys.getsizeof(empty_string)}")
    print(f"The content: {empty_string}")

    encoded_data, tree = huffman_encoding(empty_string)

    print(f"Size of the encoded data: {sys.getsizeof(int(encoded_data, 2))}")
    print(f"Content of the encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the decoded data: {decoded_data}")

    print("\nTest Case 4")
    same_letter_string = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"

    print(f"Size: {sys.getsizeof(same_letter_string)}")
    print(f"Content: {same_letter_string}")

    encoded_data, tree = huffman_encoding(same_letter_string)

    print(f"Size of the encoded data: {sys.getsizeof(int(encoded_data, 2))}")
    print(f"Content of the encoded data: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"Size of the decoded data: {sys.getsizeof(decoded_data)}")
    print(f"Content of the decoded data: {decoded_data}")
