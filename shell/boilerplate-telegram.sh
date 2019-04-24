#!/bin/bash

TOKEN='YOUR-BOT-TOKEN'
CHAT_ID='YOUR-CHAT-ID'
MESSAGE='MESSAGE'
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$CHAT_ID -d text="$MESSAGE"
