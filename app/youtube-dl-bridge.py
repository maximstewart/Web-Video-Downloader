#!/usr/bin/env python

import sys
import json
import struct
import subprocess

# Python 2.x version (if sys.stdin.buffer is not defined)
# Read a message from stdin and decode it.
def getMessage():
    rawLength = sys.stdin.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack('@I', rawLength)[0]
    message = sys.stdin.read(messageLength)
    return json.loads(message)

while True:
    receivedMessage = getMessage()

    if receivedMessage:
        command = "cd ~/Downloads && youtube-dl " + receivedMessage;
        subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
