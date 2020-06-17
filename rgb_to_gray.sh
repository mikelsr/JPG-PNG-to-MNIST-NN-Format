#!/bin/bash

height=28
width=28

if [ `ls test-images/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in test-images/*/*.jpg; do
    mv $file "${file}_rgb"
    convert "${file}_rgb" -colorspace Gray $file
    # file "$file" #uncomment for testing
    rm "${file}_rgb"
  done
fi

if [ `ls training-images/*/*.jpg 2> /dev/null | wc -l ` -gt 0 ]; then
  for file in training-images/*/*.jpg; do
    mv $file "${file}_rgb"
    convert "${file}_rgb" -colorspace Gray $file
    # file "$file" #uncomment for testing
    rm "${file}_rgb"
  done
fi
