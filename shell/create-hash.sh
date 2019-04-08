prompt='c69'
pass='caio'
h() {
  printf '%s' "$( openssl sha256 -hmac "$prompt" -hex | cut -d ' ' -f 2 )"
}

hash=$( printf '%s' "$pass" | h | h )
echo $prompt ':' $hash
