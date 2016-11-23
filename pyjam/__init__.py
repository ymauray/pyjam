import subprocess
import json
import sys
import ymatools


def main():
    """Entry point for PyJam"""
    options = ymatools.parse_config("c:", ["config=", "jamendo-client-id="])
    url = 'https://api.jamendo.com/v3.0/tracks/?client_id=%s&format=json&include=stats&limit=200&order=releasedate_desc' % options['jamendo']['client-id']
    proc = subprocess.Popen(['curl', '-s', '-X', 'GET', url], stdout=subprocess.PIPE)
    (out, _) = proc.communicate()
    out_json = json.loads(out.decode('utf-8'))
    status = out_json['headers']['status']
    if status != 'success':
        print("Error returned by Jamendo")
        sys.exit(-1)
    result_count = out_json['headers']['results_count']
    for i in range(result_count):
        result = out_json['results'][i]
        print("%s, %s, %s" % (result['id'], result['stats']['rate_downloads_total'], result['stats']['rate_listened_total']))