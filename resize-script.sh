#!/bin/bash

height=96
width=96

if [ `ls test-images/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in test-images/*/*.png; do
    sips -z $height $width -s format jpeg "$file" --out "${file%.*}.jpg"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

if [ `ls training-images/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  echo hi
  for file in training-images/*/*.png; do
    sips -z $height $width -s format jpeg "$file" --out "${file%.*}.jpg"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi
