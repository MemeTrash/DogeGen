"""
Methods to translate English to dogespeak.

Author: Jack Romo <sharrackor@gmail.com>
"""

import nltk
from nltk.stem.wordnet import WordNetLemmatizer
import random
import string
from collections import defaultdict

MUCH = 'much'
MANY = 'many'
SUCH = 'such'
VERY = 'very'
SO = 'so'
WOW = 'wow'
AMAZE = 'amaze'

class Translator(object):
    def __init__(self):
        self._lemmatizer = WordNetLemmatizer()
        self._lemmatizer.lemmatize('foo', pos='n') # initialize the memmatizer

    def dogeify_text(self, eng_text, wow_density, amaze_density, max_phrases):
        """
        Translate body of text to Doge form.
        Output can be directly fed into 'make_doge_image' function.

        Args:
            eng_text (str): Piece of english text to translate from.
            wow_density (float): Number of wow's per doge phrase. Must be > 0.
            amaze_density (float): Number of amaze's per doge phrase. Must be > 0.
            max_phrases (int): Max number of non-(wow/amaze) phrases.

        Returns:
            list[str]: List of Doge phrases, translated from eng_text.
        """
        word_ls = self._get_base_doge_words(eng_text)
        word_freqs = defaultdict(int)
        for word in word_ls:
            word_freqs[word] += 1
        sorted_words = sorted(word_ls, key=lambda s: word_freqs[s])[::-1]
        desc_ls = self._get_doge_descriptors(sorted_words)
        doge_phrases = [desc_ls[i] + ' ' + sorted_words[i] for (i, _) in enumerate(word_ls)]
        if len(doge_phrases) >= max_phrases:
            doge_phrases = doge_phrases[:max_phrases]
        else:
            while len(doge_phrases) < max_phrases:
                doge_phrases.append(random.choice([WOW, AMAZE]))
        # add extra wow's and amaze's
        doge_phrases = self._add_extra_phrase(doge_phrases, WOW, wow_density)
        doge_phrases = self._add_extra_phrase(doge_phrases, AMAZE, amaze_density)
        return doge_phrases


    def _get_base_doge_words(self, eng_text):
        """
        Get all base words from text to make doge phrases from.
        eg. 'Hello there, I am happy' -> ['hello', 'are', 'happy']

        Args:
            eng_text (str): Text to get words from.

        Returns:
            list[str]: List of lower case words to use from text.
        """
        phrase_no_punct = eng_text.translate(None, string.punctuation)
        tagged_words = nltk.pos_tag([w.lower() for w in phrase_no_punct.split(' ') if w.isalpha()])
        chosen_words = []
        for word, tag in tagged_words:
            if tag[0] in ['N', 'V', 'J']:
                # make noun singular
                if tag[0] == 'N':
                    word = self._lemmatizer.lemmatize(word, pos='n')
                # make verb infinitive
                elif tag[0] == 'V':
                    word = self._lemmatizer.lemmatize(word, pos='v')
                chosen_words.append(word.encode('ascii', 'ignore'))  # lemmatize makes word unicode
        return list(set(chosen_words))


    def _get_doge_descriptors(self, word_ls):
        """
        Get descriptors for a set of doge words.
        eg. ['person', 'run'] -> ['much', 'very']

        Args:
            word_ls (list[str]): List of words to use.

        Returns:
            list[str]: List of doge descriptors, eg. 'much', 'very', in order.
        """
        tagged_words = nltk.pos_tag(word_ls)
        chosen_descriptors = []
        for word, tag in tagged_words:
            possible_descs = [MUCH, MANY, SUCH, SO, VERY]
            if tag[0] == 'J':
                possible_descs.remove(VERY)
                possible_descs.remove(SO)
            if len(chosen_descriptors) >= 2:
                allowed_descriptors = [s for s in possible_descs if s not in chosen_descriptors[-2:]]
            else:
                allowed_descriptors = [s for s in possible_descs if s not in chosen_descriptors]
            chosen_descriptors.append(random.choice(allowed_descriptors))
        return chosen_descriptors


    def _add_extra_phrase(self, phrases_ls, phrase, phrase_density):
        """
        Add extra phrase, such as 'wow' or 'amaze', to phrase list.

        Args:
            phrases_ls (list[str]): List of current phrases.
            phrase (str): Phrase to add.
            phrase_density(float): Number of new phrases per original doge phrase. Must be > 0.
        """
        if phrases_ls.count(phrase) < (len(phrases_ls) * phrase_density):
            num_of_phrase = int(len(phrases_ls) * phrase_density)
        else:
            num_of_phrase = 0
        phrases_ls.extend([phrase]*num_of_phrase)
        return phrases_ls
