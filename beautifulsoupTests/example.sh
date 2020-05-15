#!/usr/bin/env bash

: '
this is a fucking comment
what the fuck
how can a man be so endlessly fucking disappointing
'
echo "Enter your lucky number"
read n
case $n in
101)
echo "1st prize" ;;
510)
echo "2nd prize" ;;
990)
echo "3rd prize" ;;
*)
echo "try for the next time" ;;
esac
