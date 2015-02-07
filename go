#!/usr/bin/env bash
URL=$(./get-url.py)
OUTPUT=${BROWSER:-echo}
$OUTPUT $URL
