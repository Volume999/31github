import random
import sys
import json
import string
import secrets
import argparse
import os
from dotenv import load_dotenv
from icecream import ic

ic.disable()
load_dotenv()

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

def parse_parameters():
    pass

def parse_env_vars():
    pass 


def main():
    # TODO: env variables
    pass

if __name__ == "__main__":
    main()