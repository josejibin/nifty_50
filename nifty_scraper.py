import requests
import json
import redis

# connect to redis
redis_connection = redis.StrictRedis(host='localhost', port=6379, db=0)


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
    except Exception as er:
        print('Error updating results: {}'.format(er))



def read_from_redis():
    time = redis_connection.get('time')
    data = redis_connection.get('data')
    if not time and not data:
        # todo
        # do we neet to wait
        write_to_redis(redis_connection)
    else:
        time = time.decode("utf-8")
        data = json.loads(data.decode("utf-8"))
    return time, data