#!/usr/bin/env python3
# txt_generator.py

import logging

from titantv.config import TARGET_CHANNELS


def generate_txt(data, output_path):
    logging.info("Generating TXT file...")

    # Filter channels based on TARGET_CHANNELS
    filtered_channels = [
        ch
        for ch in data["channels"]
        if f"{ch['majorChannel']}.{ch['minorChannel']}" in TARGET_CHANNELS
    ]

    # Prepare text output
    lines = []
    lines.append("Lineup Information:")
    lines.append(f"Name: {data['lineup']['lineupName']}")
    lines.append(f"TimeZone: {data['lineup']['timezone']}")
    lines.append(f"UTCOffset: {data['lineup']['utcOffset']}")
    lines.append(f"Observes DST: {data['lineup']['observesDst']}")
    lines.append("")

    lines.append("Channels:")
    for ch in filtered_channels:
        lines.append(f"Channel ID: {ch['channelId']}")
        lines.append(f"CallSign: {ch['callSign']}")
        lines.append(f"Name: {ch['network']}")
        lines.append(f"Description: {ch['description']}")
        lines.append(f"HD Capable: {ch['hdCapable']}")
        lines.append(f"Major Channel: {ch['majorChannel']}")
        lines.append(f"Minor Channel: {ch['minorChannel']}")
        lines.append("")

    lines.append("Programs:")
    for prog in data["schedule"]:
        if str(prog["channelId"]) in [ch["channelId"] for ch in filtered_channels]:
            lines.append(f"Program ID: {prog['eventId']}")
            lines.append(f"Title: {prog['title']}")
            lines.append(f"Description: {prog['description']}")
            lines.append(f"StartTime: {prog['startTime']}")
            lines.append(f"EndTime: {prog['endTime']}")
            lines.append(f"Program Type: {prog['programType']}")
            lines.append(f"TV Rating: {prog.get('tvRating', '')}")
            lines.append("")

    # Ensure the output path is platform-agnostic
    output_file_path = output_path  # Use output_path directly

    # Write to file
    with open(output_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("\n".join(lines))

    logging.info(f"TXT file written to {output_file_path}")
