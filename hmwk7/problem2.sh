#!/usr/bin/env bash

outFile="${OUTFILE}.out"
echo $outFile
outError="${OUTFILE}.err"
echo $outError

cat $INFILE | ./cmd1 | ./cmd3 2>$outError 1>$outFile
