#!/usr/bin/env python3
# txt_generator.py

import logging

from titantv.config import TARGET_CHANNELS


def generate_txt(data, output_path):
    logging.info("Generating TXT file...")

    # Collect all channel IDs present in the schedule
    schedule_ids = {int(p["channelId"]) for p in data["schedule"]}
    logging.info(f"Schedule channel IDs: {schedule_ids}")

    # Filter channels based on TARGET_CHANNELS (major.minor format)
    filtered_channels = [
        ch
        for ch in data["channels"]
        if f"{ch['majorChannel']}.{ch['minorChannel']}" in TARGET_CHANNELS
    ]

    # Create a set of allowed channelIds (int) for fast lookup
    allowed_channel_ids = {int(ch["channelId"]) for ch in filtered_channels}

    # Debug logging to verify
    logging.info(f"Filtered channels count: {len(filtered_channels)}")
    logging.info(f"Allowed channel IDs: {allowed_channel_ids}")
    logging.info(f"Total programs in schedule: {len(data['schedule'])}")

    # Log any schedule entries with channel IDs not in allowed channels
    mismatched_channel_ids = schedule_ids - allowed_channel_ids
    if mismatched_channel_ids:
        logging.warning(
            f"Schedule contains programs for channel IDs not in allowed channels: {mismatched_channel_ids}"
        )
        for prog in data["schedule"]:
            if int(prog["channelId"]) in mismatched_channel_ids:
                logging.warning(
                    f"Program with ID {prog['eventId']} assigned to unknown channel ID {prog['channelId']} "
                    f"title: {prog['title']}"
                )

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
    program_count = 0
    for prog in data["schedule"]:
        if int(prog["channelId"]) in allowed_channel_ids:
            program_count += 1
            # Find the channel for additional info (like call sign)
            ch = next(
                (
                    c
                    for c in filtered_channels
                    if int(c["channelId"]) == int(prog["channelId"])
                ),
                None,
            )
            if ch:
                lines.append(
                    f"Channel: {ch['callSign']} ({ch['majorChannel']}.{ch['minorChannel']})"
                )
            lines.append(f"Program ID: {prog['eventId']}")
            lines.append(f"Title: {prog['title']}")
            lines.append(f"Description: {prog['description']}")
            lines.append(f"StartTime: {prog['startTime']}")
            lines.append(f"EndTime: {prog['endTime']}")
            lines.append(f"Program Type: {prog['programType']}")
            lines.append(f"TV Rating: {prog.get('tvRating', '')}")
            lines.append("")

    logging.info(f"Total programs written: {program_count}")

    # Write to file
    with open(output_path, "w", encoding="utf-8") as txt_file:
        txt_file.write("\n".join(lines))

    logging.info(f"TXT file written to {output_path}")
