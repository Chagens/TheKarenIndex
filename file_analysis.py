# Program to take in reviews from the webscraper, analyze and score each review on the various categories, and send them to the 
# storage system

# List of categories
#   Anger
#   Incomprehensible (misspells)
#   Length
#   Likliness of scams

import re
import word_library
import reviewscraper
from spellchecker import SpellChecker

class Analyzer():
    def __init__(self) -> None:
        pass

    # This currently assumes the reviews are split into an array 
    def analyze_review(self, review, stars):
        
        # Words that will score higher for the angry category
        angry = word_library.angry

        # Words that will score for general angry category
        negative = word_library.negative_words

        # Words that will score for the likelihood of scam category
        scam = word_library.scam

        # Words that should be avoided when calculating any particular category because they are acronyms associated with a company
        acronyms = ["UPS"]
        parsed_review = ""
        
        spell = SpellChecker()
        num_reviews = 0

        num_angry_words = 0
        num_misspells = 0
        num_scam_words = 0
        num_caps = 0
        total_words = 0
        num_reviews += 1

        words_found = []
        review_scores = []

        # Removing all symbols that could interfere with string analysis, i.e. the following symbols:
        # . , ( ) $ \ / " # ? ! * - &
        for word in review.split():
            word = re.sub(r"\(|\)|\.|\,|\$|\"|\/|\\|\#|\?|\!|\*", "", word)
            word = re.sub(r"\-|\&", " ", word)
            parsed_review += word
            parsed_review += " "

        # Finding misspelled words
        misspelled = spell.unknown(parsed_review.split())
        for misspelled_word in misspelled:
            num_misspells += 1

        # Finding angry words
        for word in angry:
            if word in parsed_review:
                num_angry_words += 2
                words_found.append(word)

        # Finding generally negative words
        for word in negative:
            if word in parsed_review:
                num_angry_words += 1
                words_found.append(word)

        # Finding words that could indicate a scam
        for word in scam:
            if word in parsed_review:
                num_scam_words += 1
                words_found.append(word)

        # Finding words that consist of all capital letters 
        for word in parsed_review.split():
            total_words += 1
            if word.isupper() and word != "I" and word not in acronyms:
                words_found.append(word)
                num_caps += 1

        # Beginning of scoring process, will probably expanded upon/moved into a separate function later
        angry_score = num_angry_words/total_words * 500
        scam_score = num_scam_words/total_words * 500
        misspell_score = num_misspells/total_words * 500
        length_score = 0

        if (stars == "1.0"):
            angry_score += 2

        if (stars == "2.0"):
            angry_score += 1
        
        if len(review) <= 200:
            scam_score += 1
        if len(review) >= 2000 and len(review) < 5000:
            angry_score += 1
            length_score += 2
        if len(review) >= 5000 and len(review) < 10000:
            angry_score += 2
            length_score += 3
        if len(review) >= 10000:
            angry_score += 3
            length_score += 7

        if angry_score > 10:
            angry_score = 10

        if scam_score > 10:
            scam_score = 10

        if misspell_score > 10:
            misspell_score = 10

        # Testing score calculations
        # print(f"review {num_reviews}:")
        # print("Words found to calculate score:")
        # for word in words_found:
        #     print(word)
        # print(f"anger score: {angry_score}")
        # print(f"scam score: {scam_score}")
        # print(f"misspell score: {misspell_score}")
        # print(f"length score: {length_score}")


        # Dictionary of review score arrays
        # The dictionary will be keyed on review1, review2, etc.
        # Each dictionary entry will be an array
        # Each array will the review scores organized thusly:
        # angry score, scam score, misspell score, length score
        review_scores.append(angry_score)
        review_scores.append(scam_score)
        review_scores.append(misspell_score)
        review_scores.append(length_score)

        return review_scores





