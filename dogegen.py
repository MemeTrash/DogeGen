import sys
import dogegen


def main(args):
    out_dir_str = args[1]
    text_inp = args[2]
    api_key = args[3]
    similar_words = dogegen.Scraper(api_key).get_words_for(text_inp)
    # TODO


if __name__ == "__main__":
    main(sys.argv)
