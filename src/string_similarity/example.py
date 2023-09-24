from string_similarity import StringSimilarity

stringSimilarity = StringSimilarity()

print(StringSimilarity.compareTwoStrings('aha', 'hah'))
print(stringSimilarity.findBestMatch('aha', ['haha', 'hoooo', 'yo', 'aha', 'hehehe']))