#!/bin/sh

while read p; do
  VERB=`echo $p | awk -F' ' '{print $1}'`
  URL=`echo $p | awk -F' ' '{print $2}'`
  RESULT=`curl -A "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" -s -o /dev/null -w "%{http_code}" $1$URL`

  if [ "$RESULT" == "200" ] || [ "$RESULT" == "403" ]; then
    echo " >>> $URL $RESULT"
  else
    echo " ... $URL $RESULT"
  fi
done <scanner.txt
