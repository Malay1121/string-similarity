# string-similarity

Finds degree of similarity between two strings, based on [Dice's Coefficient](https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient), which is mostly better than [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).

## 📄 Table of Contents

- [Usage](#🎮usage)

- [API](#📚api)

- [StringSimilarity.compareTwoStrings(string, otherString)](<#stringsimilarity.comparetwostrings(string,-otherstring)>)

- [Arguments](#arguments)

- [Returns](#returns)

- [Examples](#examples)

- [StringSimilarity.findBestMatch(string, targetStrings)](<#stringsimilarity.findbestmatch(string, targetstrings)>)

- [Arguments](#arguments-1)

- [Returns](#returns-1)

- [Examples](#examples-1)

- [Developer](#developer)

## 🎮 Usage

In your code:

```python

from  string_similarity  import  StringSimilarity



similarity = StringSimilarity.compareTwoStrings('french', 'quebec');



matches = StringSimilarity.findBestMatch('healed', ['edward', 'sealed', 'theatre']);

```

## 📚 API

### StringSimilarity.compareTwoStrings(string, otherString)

Returns a fraction between 0 and 1, which indicates the degree of similarity between the two strings. 0 indicates completely different strings, 1 indicates identical strings. The comparison is case and diacritic sensitive.

#### Arguments

- string (String): The first string
- otherString (String): The second string

Order does not make a difference.

#### Returns

(double): A fraction from 0 to 1, both inclusive. Higher number indicates more similarity.

#### Examples

```dart

StringSimilarity.compareTwoStrings('healed', 'sealed'); // → 0.8



StringSimilarity.compareTwoStrings('france', 'FrancE'); // → 0.6



StringSimilarity.compareTwoStrings('x', null); // → 0.0



StringSimilarity.compareTwoStrings('Olive-green table for sale, in extremely good condition.', 'For sale: table in very good condition, olive green in colour.'); // → 0.6060606060606061

```

### StringSimilarity.findBestMatch(string, targetStrings)

Compares `mainString` against each string in `targetStrings`.

#### Arguments

- string (String): The main string to compare the targetStrings
- targetStrings (List\<String\>): Each string in this array will be matched against the main string.

#### Returns

(BestMatch): An object with a `ratings` property, which gives a similarity rating for each target string, a `bestMatch` property, which specifies which target string was most similar to the main string, and a `bestMatchIndex` property, which specifies the index of the bestMatch in the targetStrings array.

#### Examples

```dart

StringSimilarity.findBestMatch('Olive-green table for sale, in extremely good condition.', [

'For sale: green Subaru Impreza, 210,000 miles',

'For sale: table in very good condition, olive green in colour.',

'Wanted: mountain bike with at least 21 gears.',

null

]);

// →

{ ratings:[

{ target: 'For sale: green Subaru Impreza, 210,000 miles', rating: 0.2558139534883721 },

{ target: 'For sale: table in very good condition, olive green in colour.', rating: 0.6060606060606061 },

{ target: 'Wanted: mountain bike with at least 21 gears.', rating: 0.1411764705882353 },

{ target: null, rating: 0.0 }

],

bestMatch: { target: 'For sale: table in very good condition, olive green in colour.', rating: 0.6060606060606061 },

bestMatchIndex: 1

}

```

## 🔮 Credit

**_based on 'string-similarity' Javascript project_** : [https://github.com/aceakash/string-similarity](https://github.com/aceakash/string-similarity)

## Developer

**Malay Patel**

<a href="https://github.com/Malay1121"><img src="https://avatars.githubusercontent.com/u/56907997?v=3" title="Malay1121" width="80" height="80"></a>

<a class="github-button" href="https://github.com/Malay1121" aria-label="Follow @Malay1121 on GitHub">Follow @Malay1121</a>

<a class="github-button" href="https://www.linkedin.com/malay-patel-dev/" aria-label="LinkedIn: malay-patel-dev">LinkedIn: @Malay Patel</a>
