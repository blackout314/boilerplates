#!/bin/bash

MYDIR="."
FILES=`ls -l $MYDIR | awk '{print $10}'`

for FILE in $FILES
do
  echo "[>] FILE : ${FILE}"
done
