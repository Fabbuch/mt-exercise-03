#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

python $scripts/plot.py \
    $base/models/deen_transformer_pre/baseline.log \
    $base/models/deen_transformer_prenorm/train.log \
    $base/models/deen_transformer_postnorm/train.log