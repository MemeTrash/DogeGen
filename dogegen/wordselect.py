from collections import defaultdict


def choose_words(words, num_words=10):
    """
    Choose a set of words from scraped word list.

    Args:
        words (list[str]): List of words to choose from.
        num_words (int): Number of words to choose.

    Returns:
        list[str]: List of chosen words.
    """
    big_words = remove_small_words(words)
    freq_dict = get_word_frequencies(big_words)
    freq_words = sorted(freq_dict.items(), key=lambda p: p[1])
    chosen_words = [w for (w, freq) in freq_words[-num_words:]]
    return chosen_words


def remove_small_words(words, min_length=-1):
    """
    Remove all words below a length - mean word length if not specified.

    Args:
        words (list[str]): List of words to choose from.
        min_length (int): Minimum length of word. Uses median length if not specified.

    Returns:
        list[str]: List of words above a length.
    """
    if min_length == -1:
        lengths = [len(x) for x in words]
        min_length = sum(lengths) / float(len(lengths))
    return [w for w in words if len(w) > min_length]


def get_word_frequencies(words):
    """
    Get a dictionary of words and their frequencies.

    Args:
        words (list[str]): List of words.

    Returns:
        dict: Dictionary of words as keys for their frequencies.
    """
    # FIXME
    result = defaultdict(int)
    for word in words:
        result[word] += 1
    return result
