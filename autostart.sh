#!/bin/sh

. ~/pywal-venv/bin/activate &&
	wal -R &&
	picom --daemon
