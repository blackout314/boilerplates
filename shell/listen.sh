#!/bin/bash
while [ true ]
do
  nc -l localhost 1337 >> data.txt
  # netcat -vv -lp 1337 >> data.txt
done

## send from osx
# $ echo "data" | nc localhost 1337
#
