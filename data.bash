#!/bin/bash
set -euxo pipefail

DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)"

mkdir $DIR/tmp
cp $DIR/sql/* $DIR/tmp
cd $DIR/tmp

wget -O sde.bz2 https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
bunzip2 sde.bz2
sqlite3 sde < system.sql > $DIR/unchaind/data/system.txt
sqlite3 sde < connection.sql > $DIR/unchaind/data/connection.txt
sqlite3 sde < ships.sql > $DIR/unchaind/data/ships.txt
rm -rf $DIR/tmp
