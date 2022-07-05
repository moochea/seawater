#!/usr/bin/env bash

python3 -m venv ./venv
cd venv/bin
source activate
cd ../../
pip install -r requirements.txt
