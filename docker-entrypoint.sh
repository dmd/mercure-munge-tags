#!/usr/bin/env bash
set -Eeo pipefail
echo "-- Starting tag munger module..."
python munge.py $MERCURE_IN_DIR $MERCURE_OUT_DIR
echo "-- Done."
