#!/bin/sh

while read p; do
  VERB=`echo $p | awk -F' ' '{print $1}'`
  URL=`echo $p | awk -F' ' '{print $2}'`
  RESULT=`curl -s -o /dev/null -w "%{http_code}" $1$URL`

  if [ "$RESULT" == "200" ] || [ "$RESULT" == "403" ]; then
    echo " >>> $URL $RESULT"
  else
    echo " ... $URL $RESULT"
  fi
done <scanner.txt
