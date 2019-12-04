#!/bin/bash
cd ../project2
coverage run --source=. -m unittest
coverage report
coverage html
mv -f htmlcov ../..