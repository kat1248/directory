#!/bin/bash
sheet_id="1nh93bN34gIsu7FiBfPDHNZmQVQa-mIbTAO5_QtDUJlM"
email_id="659153823"
main_id="474791396"
panel_id="635467025"

fetch () {
    # fetch <sheet> <tab> <file> <escape>
    local tfile=$(mktemp /tmp/foo.XXXXXXXXX)
    curl -s -o $tfile "https://docs.google.com/spreadsheets/d/$1/export" --data-urlencode "format=csv" --data-urlencode "id=$1" --data-urlencode "gid=$2"
    if [ "$4" = true ]; then
        # escape &, _, #
        sed -e '2,$s/\([&_#]\)/\\\1/g' $tfile > $3
    else
        cp $tfile $3
    fi
    rm $tfile
}

fetch ${sheet_id} ${main_id} $1 true
fetch ${sheet_id} ${email_id} $2 false
