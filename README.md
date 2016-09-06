# DogeGen

This is a doge meme generator. It is, obviously, very important.

## License

This project uses the [MIT License](LICENSE).

## Requirements

The following packages are required:

* Python 2.7.x
* PIL
* Flask
* nltk

To install all requirements, please run the following:

```
pip install -r requirements.txt
python -m nltk.downloader averaged_perceptron_tagger treebank maxent_treebank_pos_tagger wordnet wordnet_ic
```

You must also go into the dogegen/translate.py file and change the
NLTK_PATH variable to wherever your nltk files are stored.

## Execution

Run the following from within the project root:

```
python dogegen.py "input_text" "image/output/path.jpg" "path/to/resources" max_phrases
```

An image will be generated with Doge phrases interpreted and translated from your text.

eg.

```
python dogegen.py "Hello there, my good friend." "../images/result.jpg" "./resources" 5
```

Generally, the resources directory can just be left as "./resources" if
you are inside the root of the project directory.

## Running as a server

Because ntlk must load over 10mb of language data into memory when initialized, running a server and sending it many requests is also possible. Run the following:

```
python dogegen.py --server-start "path/to/resources" "host.name" port
```

The server will then run on http://"host.name"/"port". On another terminal / process, run:

```
curl
<your_host>:<your_path>/makememe/<escaped_inp_text>/<escaped_out_dir>/<escaped_max_phrases>
```

replacing content within <>'s appropriately.

The first meme will be slow to generate due to nltk initialization, but the rest should take under half a second.

To close the server, run

```
curl -X POST <your_host>:<your_port>/shutdown
```

## Running as a Unix service

To run as a systemd service, put the dogegen.service file in the /etc/systemd/system directory.
Then, copy the contents of this repository into /usr/local/bin/DogeGen.

After this, you can run

```
sudo systemctl start dogegen.service
```

using start, stop, restart and status commands as needed.

This will start the server, and it can be used as described above.
(Sending the shutdown POST request will now kill the service.)

## Contribution

please not, such independent, wow
