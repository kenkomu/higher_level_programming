#!/bin/bash
# displays all HTTP methods the server will accept.
curl -sX POST -d "email=hr@test@gmail.comsubject=I%20will%20always%20be%20here%20for%20PLD" "$1"
