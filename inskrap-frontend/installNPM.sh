#!/bin/sh
set -e

npm install || (echo "Initial npm install failed. Retrying..." && rm -rf node_modules package-lock.json && npm install)
