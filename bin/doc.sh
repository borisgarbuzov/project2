#!/bin/bash
cd ..
echo "Doing git pull..."
git checkout
git pull
cd docs
make clean
echo "Collecting documentation from modules..."
sphinx-apidoc -o rst ../project2/
echo "Make html page..."
make html
echo "Done!"