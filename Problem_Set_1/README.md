## Problem Set I - Regex

1. Write a regex to extract all the numbers with orange color background
from the below text in italics (Output should be a list).
{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or anobject that implements Countable (153)"}]}

## Overview

This Python script extracts all numbers from a JSON-like string using regular expressions and stores them in a list. The string contains order IDs and error messages, and the script retrieves all numeric values from this data.

## Requirements

- Python 3.11.7

## Usage

1. Clone or download the repository.
2. Ensure you have Python 3.x installed on your system.
3. Run the script using the command: python ExtractNum.py