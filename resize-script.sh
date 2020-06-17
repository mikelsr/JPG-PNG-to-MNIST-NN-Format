#!/bin/bash

height=28
width=28

if [ `ls test-images/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in test-images/*/*.png; do
    convert "$file" -resize "${width}x${height}"\! "${file%.*}.jpg"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

if [ `ls training-images/*/*.png 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in training-images/*/*.png; do
    convert "$file" -resize "${width}x${height}"\! "${file%.*}.jpg"
    file "$file" #uncomment for testing
    rm "$file"
  done
fi

