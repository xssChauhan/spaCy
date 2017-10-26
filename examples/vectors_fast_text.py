#!/usr/bin/env python
# coding: utf8
"""Load vectors for a language trained using FastText
https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md
"""
from __future__ import unicode_literals
import plac
import numpy

import from spacy.language import Language


@plac.annotations(vectors_loc=("Path to vectors", "positional", None, str))
def main(vectors_loc):
    nlp = Language()

    with open(vectors_loc, 'rb') as file_:
        header = file_.readline()
        nr_row, nr_dim = header.split()
        nlp.vocab.clear_vectors(int(nr_dim))
        for line in file_:
            line = line.decode('utf8')
            pieces = line.split()
            word = pieces[0]
            vector = numpy.asarray([float(v) for v in pieces[1:]], dtype='f')
            nlp.vocab.set_vector(word, vector)
    doc = nlp(u'class colspan')
    print(doc[0].similarity(doc[1]))


if __name__ == '__main__':
    plac.call(main)
