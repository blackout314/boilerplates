#!/bin/sh

echo '[+] LINT'
php -l $1

echo '[+] GREP'
cat $1 | grep -P "(passthru|exec|eval|shell_exec|assert|str_rot13|system|phpinfo|base64_decode|chmod|mkdir|fopen|fclose|readfile) *\("
