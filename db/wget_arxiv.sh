#!/usr/bin/env bash

wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1vv4ygooLBSkOOrWqWZcPyaOLde8NhKCx' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1vv4ygooLBSkOOrWqWZcPyaOLde8NhKCx" -O arxiv.tar.gz && rm -rf /tmp/cookies.txt
