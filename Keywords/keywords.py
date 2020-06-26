""" Python 3.8.2

Written by Tomas Jelinek (tomas.jeilnek@ysoft.com).

(c) Copyright YSoft Corporation, a.s., All Rights Reserved.

"""
import argparse
import sys
from datetime import datetime


def parse_bin(data):
    test_str = data.replace(' ', '')
    letter_nums = list()

    # Get the index between the word definition and word letters
    try:
        word_count = int(test_str[:8])
    except ValueError:
        return False

    letter_index = word_count * 4 + 8

    # Get letter counts for each word in the definition
    num_str, word_letters = test_str[8:letter_index], test_str[letter_index:]
    while word_count > 0:
        letter_nums.append(int(num_str[:4]))
        num_str = num_str[4:]
        word_count -= 1

    if len(num_str) > 0 or not len(word_letters) == sum(letter_nums):
        print('Binary file parsing error. Either words and letters part does'
              ' not match the word definition part counts or vice versa.')
        sys.exit(4)

    return letter_nums, word_letters


def bin_processor(letter_nums, word_letters):
    words = []

    for letter_count in letter_nums:
        index = letter_count
        words.append(word_letters[:index])
        word_letters = word_letters[index:]

    return sort_keys(words)


def text_processor(data):
    words = []
    lines = data.splitlines()

    for item in lines:
        item = item.split(',')
        for word in item:
            word = word.strip(' .,:!?"\' ')
            words.append(word.lower()) if len(word) > 0 else False
    return sort_keys(words)


def sort_keys(words):
    keywords = dict()

    for word in words:
        keywords.setdefault(word)

    final_values = ''
    for keyword in sorted(keywords.keys()):
        final_values = final_values + keyword + '\n'

    return final_values


def save_output(data, outfile):
    try:
        with open(outfile, 'a+', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError:
        print("Saving failed.")
        sys.exit(3)


# Specify the current date and time into a string
start_time = datetime.now()
str_time = str(start_time).replace(':', '-').replace(' ', '-').split('.')[0]


# Start processing - 3 arguments expected
parser = argparse.ArgumentParser(
    description='Example: python keywords.py input.txt T output.txt')
parser.add_argument("input", type=str,
                    help='specifies the binary or text file with keywords to be'
                         ' processed')
parser.add_argument("format", type=str,
                    help='specifies the format of an input file. Either T for'
                         'text file or B for binary file')
parser.add_argument("output", type=str,
                    help='specifies the output file with sorted result')
parser.add_argument("-t", "--time", action="store_true",
                    help='if specified it adds timestamp as a prefix to the'
                         'output file')
args = parser.parse_args()


# Digest arguments and store them as variables
try:
    with open(args.input, 'r', encoding='utf-8') as file:
        file_content = file.read()
        file.close()
except FileNotFoundError:
    print("File not found, please check the file.")
    sys.exit(1)

if args.time:
    output = str_time + '-' + args.output
else:
    output = args.output
input_format = args.format.lower()


# Binary or Text processing if correct format argument was given
if input_format == 't' and file_content.count(',') > 2:
    sorted_keys = text_processor(file_content)
elif input_format == 'b' and parse_bin(file_content):
    sorted_keys = bin_processor(*parse_bin(file_content))
else:
    print('Invalid input format specified (only B or T accepted) or',
          'invalid file content.')
    sys.exit(2)


# Save values for numbers into a file and finish
save_output(sorted_keys, output)

# Successful finish
print("Keywords processing has finished.")
sys.exit(0)
