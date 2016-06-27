# DogeGen

This is a doge meme generator. It is, obviously, very important.

## License

This project uses the [MIT License](LICENSE).

## Requirements

The following packages are required:

* Python 2.7.x
* Pillow and PIL
* nltk

All things other than Python can be installed with pip.
When nltk is installed, please run the following via terminal:

```
python -m nltk.downloader treebank maxent_treebank_pos_tagger wordnet wordnet_ic
```

## Execution

Run the following from within the project root:

```
python dogegen.py "input_text" "image/output/path.jpg" max_phrases
```

An image will be generated with Doge quotes pertaining to your text, scraped from webpages with Bing.

eg.

```
python dogegen.py "Hello there, my good friend." "../images/result.jpg" 5
```

## Contribution

please not, such independent, wow
