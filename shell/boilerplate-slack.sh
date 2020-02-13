MESSAGE=$1
WEBHOOK='https://'
curl -X POST -H 'Content-type: application/json' --data '{"text":"'$MESSAGE'"}' $WEBHOOK
