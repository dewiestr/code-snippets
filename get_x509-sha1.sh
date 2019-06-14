#!/bin/bash

FPRINT=`echo -n | openssl s_client -connect $1:443 2>/dev/null| openssl x509  -noout -fingerprint | cut -f2 -d'='`

if [ "$2" = "$FPRINT" ]; then
    exit 0
  else
    exit 1
fi
