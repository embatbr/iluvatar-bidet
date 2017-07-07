#!/bin/bash


export PROJECT_ROOT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd $PROJECT_ROOT_PATH


export EXECUTION_DATETIME="`date -u +%Y_%m_%d_%H_%M_%S`"

python $PROJECT_ROOT_PATH/src/main.py
