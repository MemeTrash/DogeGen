# DogeGen

This is a doge meme generator. It is, obviously, very important.

## License

This project uses the [MIT License](LICENSE).

## Requirements

The following packages are required:

* Python 2.7.x
* PIL
* Pyro
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

An image will be generated with Doge phrases interpreted and translated from your text.

eg.

```
python dogegen.py "Hello there, my good friend." "../images/result.jpg" 5
```

Because ntlk must load over 10mb of language data into memory when initialized, running a daemon and sending it many requests is also possible. Run the following:

```
python dogegen.py --daemon-start
```

A uri will be printed. Copy this and, in another terminal / process, run:

```
python dogegen.py --with-daemon "copied_uri" "input_text" "output_dir.jpg" max_phrases
```

The first meme will be slow to generate due to nltk initialization, but the rest should take under half a second.

## Contribution

please not, such independent, wow
