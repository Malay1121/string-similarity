import string_similarity


class StringExtensions(str):
    def similarityTo(string1, string2):
        return string_similarity.StringSimilarity.compareTwoStrings(string1, string2)

    def bestMatch(string1, targetStrings):
        return string_similarity.StringSimilarity.findBestMatch(string1, targetStrings)
    

