#! /bin/bash

# virtualenv must be installed on your system, install with e.g.
# pip install virtualenv

scripts=$(dirname "$0")
base=$scripts/..

python $scripts/plot.py \
    $base/models/deen_transformer_pre/baseline.log \
    $base/models/deen_transformer_prenorm/train.log