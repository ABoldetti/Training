#!/bin/bash

VIDEO="$1"
THRESHOLD="$2"   # in dB, e.g. -35
MIN_DURATION="0.5" # minimum duration in seconds to keep

if [ -z "$VIDEO" ] || [ -z "$THRESHOLD" ]; then
    echo "Usage: $0 <video_file> <threshold_db>"
    exit 1
fi

AUDIO_LOG=$(mktemp)
TMPDIR=$(mktemp -d)
BASENAME=$(basename "$VIDEO" .mp4)
OUTFILE="${BASENAME}_filtered.mp4"

# Step 1: Detect silent parts
echo "Detecting silence..."
ffmpeg -i "$VIDEO" -af "silencedetect=n=${THRESHOLD}dB:d=${MIN_DURATION}" -f null - 2> "$AUDIO_LOG"

# Step 2: Parse loud segments from log
DURATION=$(ffprobe -i "$VIDEO" -show_entries format=duration -v quiet -of csv="p=0")
STARTS=(0)
ENDS=()
while IFS= read -r line; do
    if echo "$line" | grep -q "silence_start"; then
        t=$(echo "$line" | sed -n 's/.*silence_start: //p')
        ENDS+=("$t")
    elif echo "$line" | grep -q "silence_end"; then
        t=$(echo "$line" | sed -n 's/.*silence_end: //p' | cut -d ' ' -f 1)
        STARTS+=("$t")
    fi
done < "$AUDIO_LOG"
ENDS+=("$DURATION")

# Step 3: Extract loud segments
CLIPS=()
for i in "${!STARTS[@]}"; do
    start="${STARTS[$i]}"
    end="${ENDS[$i]}"
    dur=$(echo "$end - $start" | bc)
    if (( $(echo "$dur >= $MIN_DURATION" | bc -l) )); then
        clip="$TMPDIR/clip_$i.mp4"
        echo "Extracting loud segment: $start to $end"
        ffmpeg -y -ss "$start" -i "$VIDEO" -t "$dur" -c copy "$clip"
        CLIPS+=("file '$clip'")
    fi
done

# Step 4: Create file list for concat
LISTFILE="$TMPDIR/concat_list.txt"
printf "%s\n" "${CLIPS[@]}" > "$LISTFILE"

# Step 5: Concatenate clips
if [ ${#CLIPS[@]} -eq 0 ]; then
    echo "No loud segments found above threshold."
    exit 1
fi

echo "Concatenating clips..."
ffmpeg -f concat -safe 0 -i "$LISTFILE" -c copy "$OUTFILE"

echo "Done. Output saved to $OUTFILE"

# Cleanup
rm -rf "$TMPDIR" "$AUDIO_LOG"
