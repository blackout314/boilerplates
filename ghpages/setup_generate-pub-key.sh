# generate pub key 
ssh-keygen -t rsa -b 4096 -C "me@carlodenaro.com"

# xclip -sel clip < deploy_key.pub
# paste in: https://github.com/<your name>/<your repo>/settings/keys
# travis encrypt-file deploy_key --add
