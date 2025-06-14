#!/usr/bin/env python3
# config.py

import os

# Use os.path.join() to ensure platform-agnostic paths
CONFIG = {
    "debug_mode": True,
    "log_to_console": True,
    "log_to_file": True,
    "log_level": "INFO",
    "data_folder": os.path.join("data"),
    "logs_folder": os.path.join("logs"),
    "output_json": os.path.join("data", "api_output.json"),
    "output_txt": os.path.join("data", "listings.txt"),
    "log_file": "titantv.log",  # The log file will be handled by the logger setup
}

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",  # noqa: E501
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
]

# Channels to include in the output (major.minor format)
TARGET_CHANNELS = [
    "2.1",
    "4.1",
    "6.1",
    "7.1",
    "34.1",
    "28.1"
]