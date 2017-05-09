import os
import json

import requests
import redis


# todo
# seperate settings for development and production
# connect to redis
# redis_connection = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_connection = redis.from_url(os.environ.get("REDIS_URL"))


def get_data():
    url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
    response = requests.get(url)
    # todo
    # check for errors
    response_dict = response.json()
    time, data = response_dict['time'], response_dict['data']
    return time, data


def write_to_redis():
    try:
        time, data = get_data()
        redis_connection.set('time', time)
        # redis storing as byte
        serialized_data = json.dumps(data)
        redis_connection.set('data', serialized_data)
        print('<<<<>>>>Data for time {} wrote to redis'.format(time))
    except Exception as e:
        print('<<<<>>>>Error when writing to redis: {}'.format(e))



def read_from_redis():
    time = redis_connection.get('time')
    data = redis_connection.get('data')
    if not time and not data:
        # todo
        # do we neet to wait
        write_to_redis()
    else:
        time = time.decode("utf-8")
        data = json.loads(data.decode("utf-8"))
    return time, data