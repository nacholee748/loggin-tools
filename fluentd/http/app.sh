#!/bin/sh
var=0
while true
do
	echo "Sending logs to FluentD"
  	curl -X POST -d 'json={"foo":"bar '$var'"}' http://fluentd:9880/http-myapp.log
	sleep 5
	var=$((var + 1))
done