#28. Write a function to group words by their first letter using a dictionary.
'''{
    'a': ['apple', 'apricot'],
    'b': ['banana', 'blueberry']
}
'''
def group_by_first_letter(words):
    grouped = {}
    for word in words:
        first_letter = word[0]
        grouped.setdefault(first_letter, []).append(word)
    return grouped
