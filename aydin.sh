#!/bin/bash          

OUTPUT=$(python aydin.py) # output received from the py script
# echo $OUTPUT # debugging purposes
echo "Hello world file ran successfully"
notify-send "Aydin Word Of The Day:" \ "$OUTPUT" # sentence printed as a notification
