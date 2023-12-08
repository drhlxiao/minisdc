import numpy  as np
import pandas as pd
from datetime import timedelta
from flask import Flask, Blueprint, render_template, request, jsonify
import random
example = Blueprint('example', __name__, template_folder='templates')





def get_dummy_flare_list(start_utc, end_utc, num=10):
    """
    replace the code below with your own implementation
    """
    random_time_ranges=generate_random_utc_time_ranges(start_utc,end_utc, num)
    result=[]
    keys=['_id','start','end','link']
    i=0
    for start, end in random_time_ranges:
        result.append({'_id': i,
            'start':start,
            'flare_id':i+100,
            'end':end,
            'link':'<a href="#">FITS</a>'
            })
        i+=1
    return result






def generate_random_utc_time_ranges(start_time_str, end_time_str, num_times):
    # Convert start and end time strings to pandas datetime objects
    start_time = pd.to_datetime(start_time_str)
    end_time = pd.to_datetime(end_time_str)

    # Calculate the time range
    time_range = end_time - start_time

    # Generate random UTC times within the specified range
    random_utc_times = [start_time + timedelta(seconds=random.uniform(0, time_range.total_seconds())) for _ in range(num_times)]
    random_utc_times_end=[x + timedelta(seconds=random.uniform(0,3600)) for x in random_utc_times]
    result=[[a.isoformat(),b.isoformat()] for a, b in zip(random_utc_times,random_utc_times_end)]
    return result


#route example
@example.route("/")
def render_example_paper():
    return render_template('index.html')

@example.route("/api/flare/query", methods=['POST'])
def get_flare_list_from_database():
    start = request.form['start']
    end = request.form['end']
    """
        add your python code to query database here
    """
    result = get_dummy_flare_list(start,end)

    return jsonify(result)


