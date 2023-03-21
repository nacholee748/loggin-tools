#!/bin/sh
var=0
while true
do
    echo "Writing log to a file"
    echo '{"app":"file-myapp '$var'"}' >> /app/example-log.log
    sleep 5
    var=$((var + 1))
done
