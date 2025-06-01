#!/usr/bin/env python3
# processor.py


def process_lineup_data(lineup_data):
    lineup = lineup_data["lineups"][0]
    return {
        "lineupId": lineup["lineupId"],
        "lineupName": lineup["lineupName"],
        "timezone": lineup["timeZone"],
        "utcOffset": lineup["utcOffset"],
        "observesDst": lineup["observesDst"],
    }


def process_channels_data(channels_data):
    return [
        {
            "channelId": c["channelId"],
            "callSign": c["callSign"],
            "network": c["network"],
            "description": c["description"],
            "hdCapable": c["hdCapable"],
            "logo": c["logo"],
            "sortOrder": c["sortOrder"],
            "majorChannel": c["majorChannel"],
            "minorChannel": c["minorChannel"],
        }
        for c in channels_data.get("channels", [])
    ]


def process_schedule_data(schedule_data):

    import logging
    logging.info(f"schedule_data type: {type(schedule_data)}")
    logging.info(f"first item type: {type(schedule_data[0]) if schedule_data else 'empty'}")

    schedule = []
    for event in schedule_data:
        schedule.append(
            {
                "channelId": event["channelId"],
                "eventId": event["eventId"],
                "startTime": event["startTime"],
                "endTime": event["endTime"],
                "title": event["title"],
                "description": event["description"],
                "programType": event.get("programType", ""),
                "tvRating": event.get("tvRating", ""),
                "showCard": event.get("showCard", ""),
            }
        )
    return schedule

