#!/bin/bash
tfile=$(mktemp /tmp/foo.XXXXXXXXX)
curl -s -o $tfile https://docs.google.com/spreadsheets/d/1nh93bN34gIsu7FiBfPDHNZmQVQa-mIbTAO5_QtDUJlM/export?format=csv&id=1nh93bN34gIsu7FiBfPDHNZmQVQa-mIbTAO5_QtDUJlM&gid=474791396
sleep 5
# escape &, _, #
sed -e '2,$s/\([&_#]\)/\\\1/g' $tfile > $1
rm $tfile