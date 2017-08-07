#!/bin/bash
case $1 in
    start)
        echo "Starting log server."
        go run serve.go &
        ;;
    stop)
        echo "Stopping log server."
        sudo kill $(sudo lsof -t -i:5000)
        ;;
    *)
        echo "jec-dev bot logging server."
        echo $"Usage $0 {start|stop}"
        exit 1
esac
exit 0
