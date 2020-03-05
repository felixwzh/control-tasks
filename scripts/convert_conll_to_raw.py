"""
Embarassingly simple (should I have written it in bash?) script
for turning conll-formatted files to sentence-per-line
whitespace-tokenized files.

Takes the filepath at sys.argv[1]; writes to stdout
"""

import argparse
import sys
argp = argparse.ArgumentParser()
argp.add_argument('input_conll_filepath')
args = argp.parse_args()

buf = []

for line in open(args.input_conll_filepath):
  if line.startswith('#'):
    continue
  if not line.strip():
    sys.stdout.write(' '.join(buf) + '\n')
    buf = []
  else:
    buf.append(line.split('\t')[1])
if buf:
    sys.stdout.write(' '.join(buf) + '\n')


# python scripts/convert_conll_to_raw.py ./example/data/en_ewt-ud/en_ewt-ud-test.conllu > ./example/data/en_ewt-ud/en_ewt-ud-test.txt
# python scripts/convert_conll_to_raw.py ./example/data/en_ewt-ud/en_ewt-ud-dev.conllu > ./example/data/en_ewt-ud/en_ewt-ud-dev.txt
# python scripts/convert_conll_to_raw.py ./example/data/en_ewt-ud/en_ewt-ud-train.conllu > ./example/data/en_ewt-ud/en_ewt-ud-train.txt