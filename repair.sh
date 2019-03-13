#!/bin/bash
# escape &, _, #
sed -e '2,$s/\([&_#]\)/\\\1/g' $1 > $2