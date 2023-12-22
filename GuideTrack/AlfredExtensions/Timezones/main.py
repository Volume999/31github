import random
import sys
import json
import string
import secrets
import argparse
import os
from dotenv import load_dotenv
from icecream import ic
from enum import Enum
import re

# MODE = "RUN"
MODE = "TEST"
DEBUG = True

ic.disable()
load_dotenv()

class TimezoneConverter:
    def __init__(self, datetime, timezone1):
        self.datetime = datetime
        self.timezone1 = timezone1

    def convert(self, timezone2):
        pass

class QueryType(Enum):
    CONVERSION = 1
    DIFFERENCE = 2

class ConversionQuery:
    datetime = None
    src_timezone = None
    dst_timezone = None

    def __init__(self, datetime, src_timezone, dst_timezone):
        self.datetime = datetime
        self.src_timezone = src_timezone
        self.dst_timezone = dst_timezone

class DifferenceQuery:
    src_datetime = None
    add_datetime = None

    def __init__(self, src_datetime, add_datetime):
        self.src_datetime = src_datetime
        self.add_datetime = add_datetime

# Examples:
# I am not sure if keyword is needed but let's try with it first
# (tz) {datetime/time/date} (from)* {timezone} (to)* {timezone} - Straight converter
# 01-01-2001 12:55 PM from CET to ET
# (tz) {datetime/time/date} in {timezone} - Convert from local timezone to another
# 13:20 in CET
# (tz) (datetime/time/date) from {timezone} - Convert from another timezone to local
# 13:20 from CET
# (tz) (datetime/time/date) (+,-) (datetime/time/date) - Find time difference between 


def wrap_error(error):
    return {
        "items": [
            {
                "title": "Error",
                "subtitle": error,
            }   
        ]
    }

def wrap_results(passwords):
    results = []
    for i, password in enumerate(passwords):
        results.append({
            "arg": password,
            "title": password,
            "subtitle": f"Press Enter to copy password {i+1}"
        })
    result = {"items": results}
    return result

parser = argparse.ArgumentParser(description="Timezone converter")
parser.add_argument("query", type=str, help="Query to parse")

def parse_parameters(query):
    convert_pattern = r"((?P<date>\d{1,4}[-\/]\d{1,2}[-\/]\d{1,4})\s*)?((?P<time>\d{1,2}:\d{1,2})\s*(?P<part>AM|PM)?\s*)?((?:(?:From|from|in)\s+)?(?P<srctz>\w+)\s*)?((:?to\s+|To\s+)?(?P<dsttz>\w+)\s*)?"
    difference_pattern = r"(?P<datetime1>[\d\-\:\s\w]+)\s+(?P<op>[+,-])\s+(?P<datetime2>[\d\-\:\s\w]+)"
    ic(query)
    res = None
    convert_match = ic(re.match(convert_pattern, query))
    if convert_match:
        res = ic(convert_match.groupdict())
    difference_match = ic(re.match(difference_pattern, query))
    if difference_match:
        res = ic(difference_match.groupdict())
    if res:
        return res
    raise Exception("Invalid query")

def parse_env_vars():
    pass 

def perform_operation(operation):
    pass

def main():
    try:
        args = ic(parser.parse_args())
        operations = parse_parameters(args.query)
        results = map(perform_operation, operations)
        print(json.dumps(wrap_results(results)))
    except Exception as e:
        print(json.dumps(wrap_error(str(e))))

def test():
    # Test regex patterns
    conversion_queries = [
        "01-01-2001 12:55 PM from CET to ET",
        "13:20 in CET",
        "13:20 from CET",
        "2001-12-01 23:00 PM CPH to China",
    ]

    difference_queries = [
        "13:20 + 14:20",
        "2023-02-10 - 10 days",
        "2023-01-01 + 1 month",
        "13:20:15 + 20 minutes"
    ]

    combined_queries = [
        "13:20"
    ]

    for query in conversion_queries:
        res = parse_parameters(query)
    
    for query in difference_queries:
        res = parse_parameters(query)
    
    # Test converter 
    print("Initial time: 01-01-2001 12:55 PM CET")
    t = TimezoneConverter("01-01-2001 12:55 PM", "CET")
    print(f"Convert to CET: {t.convert('ET')}")
    print(f"Convert to UTC: {t.convert('UTC')}")

if __name__ == "__main__":
    if DEBUG:
        ic.enable()
    if MODE == "RUN": main()
    elif MODE == "TEST": test()