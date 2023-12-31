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
from datetime import datetime, timedelta
import pytz
from tzlocal import get_localzone
from zoneinfo import ZoneInfo, available_timezones
import collections
import pycountry

# MODE = "RUN"
MODE = "MVP"
DEBUG = True

ic.disable()
load_dotenv()

class TimezoneService:
    country_timezones = None
    timezones = None
    abbreviations = None

    def __init__(self):
        self.country_timezones = self.get_country_timezones()
        self.timezones, self.abbreviations = self.get_timezone_codes()

    def get_timezone_codes():
        tzones = collections.defaultdict(set)
        abbrevs = collections.defaultdict(set)

        for name in pytz.all_timezones:
            tzone = pytz.timezone(name)
            for utcoffset, dstoffset, tzabbrev in getattr(
                    tzone, '_transition_info', [[None, None, datetime.now(tzone).tzname()]]):
                tzones[tzabbrev].add(name)
                abbrevs[name].add(tzabbrev)
        return tzones, abbrevs
    
    def get_timezone_from_country(code):
        country_timezones = pytz.country_timezones
        return country_timezones(code)  

class RegionService:
    countries = None

    def __init__(self):
          self.countries = pycountry.countries
        
    def get_country_from_code(self, code):
        return self.countries.get(alpha_2=code)
    
class ConversionQuery:
    datetime = None
    src_timezone = None
    dst_timezone = None

    def __init__(self, datetime, src_timezone, dst_timezone):
        self.datetime = datetime
        self.src_timezone = src_timezone
        self.dst_timezone = dst_timezone
    
    def resolve(self):
        ic(self.datetime, self.src_timezone, self.dst_timezone)
        ic("Datetime original timezone:", self.datetime.tzinfo)
        aware = self.datetime.replace(tzinfo=pytz.timezone(self.src_timezone))
        ic("Source timezone aware", self.datetime.tzinfo)
        converted = aware.astimezone(pytz.timezone(self.dst_timezone))
        ic("Destination timezone aware", self.datetime.tzinfo)
        return converted


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

def wrap_results(outputs):
    results = []
    for i, output in enumerate(outputs):
        results.append({
            "arg": output,
            "title": output,
        })
    result = {"items": results}
    return result

parser = argparse.ArgumentParser(description="Timezone converter")
parser.add_argument("query", type=str, help="Query to parse")


def parse_datetime(date, time, part):
    if not date and not time:
        return datetime.now()
    resDate = None
    if date:
        for fmt in ["%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"]:
            try:
                resDate = datetime.strptime(date, fmt)
                break
            except:
                pass
    if date and not resDate:
        raise ValueError(f"Invalid date format: {date}")
    resTime = None
    if time:
        try:
            if part:
                resTime = datetime.strptime(time + part, "%I:%M%p")
            else:
                resTime = datetime.strptime(time, "%H:%M")
        except:
            raise ValueError(f"Invalid time format: {time}")
    ic(resDate, resTime, part)
    if resDate and resTime:
        dt = datetime.combine(resDate, resTime.time())
    elif resDate:
        dt = resDate
    elif resTime:
        dt = resTime
    else:
        raise ValueError(f"Invalid date/time values: {resDate}, {resTime}, {part}")
    return dt

def parse_timezones(srctz, dsttz):
    if not srctz and not dsttz:
        return None, None
    if not srctz:
        srctz = get_local_timezone()
    if not dsttz:
        dsttz = get_local_timezone()
    return srctz, dsttz

def get_local_timezone():
    return get_localzone()

def parse_parameters(query):
    convert_pattern = r"((?P<date>\d{1,4}[-\/]\d{1,2}[-\/]\d{1,4})\s*)?((?P<time>\d{1,2}:\d{1,2})\s*(?P<part>AM|PM)?\s*)?((?:(?:From|from|in)\s+)?(?P<srctz>\w+)\s*)?((:?to\s+|To\s+)?(?P<dsttz>\w+)\s*)?"
    ic(query)
    res = [] 
    convert_match = ic(re.match(convert_pattern, query))
    if convert_match:
        q = ic(convert_match.groupdict())
        srctz, dsttz = parse_timezones(q['srctz'], q['dsttz'])
        dt = parse_datetime(q['date'], q['time'], q['part'])
        ic(dt)
        res.append(ConversionQuery(dt, srctz, dsttz))
    if res:
        return res
    raise Exception("Invalid query")

def parse_env_vars():
    pass 

def perform_operation(operation):
    pass

def main():
    try:
        timezone_service = TimezoneService()
        args = ic(parser.parse_args())
        operations = parse_parameters(args.query, timezone_service)
        results = map(lambda k: k.resolve(), operations)
        ic(results)
        print(json.dumps(wrap_results(results)))
    except Exception as e:
        print(json.dumps(wrap_error(str(e))))

def test():
    # Test regex patterns
    conversion_queries = [
        "01-01-2001 12:55 PM from CET to ET",
        "13:20 in CET",
        "13:20 from CET"
    ]

    conversion_from_contry_queries = [
        "01-01-2001 12:55 PM from France to Germany",
        "13:20 from France",
        "13:20 from France to Germany",
        "22:00 in Germany",
        "10:00 PM from Germany to France",
    ]

    conversion_from_city_queries = [
        "01-01-2001 12:55 PM from Paris to Berlin",
        "13:20 from Paris",
        "13:20 from Paris to Berlin",
        "22:00 in Berlin",
        "10:00 PM from Berlin to Paris",
    ]

    for query in conversion_queries:
        res = parse_parameters(query)
    
    # Test converter 
    res = map(lambda k: k.resolve(), res)
    for r in res:
        print(r)

def mvp():
    res = wrap_results(["2023-01-01 17:55 PM"])
    print(json.dumps(res))

if __name__ == "__main__":
    if DEBUG:
        ic.enable()
    if MODE == "RUN": main()
    elif MODE == "TEST": test()
    elif MODE == "MVP": mvp()