#!/usr/bin/env bash

rm -rf japanese_conjugation.ankiaddon japanese_conjugation.ankiaddon.zip
mkdir japanese_conjugation.ankiaddon
cp doc/config.md japanese_conjugation.ankiaddon/
pushd japanese_conjugation
    cp -r * ../japanese_conjugation.ankiaddon/
    
    find ../japanese_conjugation.ankiaddon -name "__pycache__" -type d -exec rm -r "{}" \;
    find ../japanese_conjugation.ankiaddon -type d -name "*egg-info" -exec rm -r "{}" \;
    find ../japanese_conjugation.ankiaddon -type f -name "*.pyc" -delete
    zip -r ../japanese_conjugation.ankiaddon.zip *
popd

