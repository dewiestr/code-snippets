#!/usr/bin/python
import requests
import os
import sys
import argparse
try:
    import requests
except:
    print "Missing requests library"
 
import json

__all__ = []
__version__ = 0.1
__date__ = '2014-09-15'
__updated__ = __date__
__author__ = 'Rocky De Wiest'


#file in the api_url
api_url = ''
if api_url == '':
    print "Please fill in the necessary variable \"api_url\""
machine_url='/machines/list'
sandbox_url='tasks/create/file'


def luke_filewalker(Malware_bin):
    """takes all the files in the malware bin and extracts extension, returns list of files with extensions"""
    file_analyses=[]
    for (dirpath, dirname, filenames) in os.walk(Malware_bin):
        for f in filenames:
            file_analyses.append(os.path.join(Malware_bin,f))
            #print "Added : "+'\033[1m'+f+'\033[0m'
    return file_analyses

def get_machines():
    r = requests.get(api_url+machine_url)
    data = r.content
    js = json.loads(data)
    #return json.dumps(js, indent=4, sort_keys=True)
    machines=[]
    for mach in js['machines']:
        machines.append(mach['name'])
    return machines

def submit_to_cuckoo(filepath):
    machlist=get_machines()
    #logger.debug("#### Sandboxing")

    analyses_id=[]
    for mach in machlist:
        data={'machine':mach}
        #filepath=os.path.join()
        files={'file': open(filepath, 'rb')}
        url=os.path.join(api_url,sandbox_url)
        result=requests.post(url,data=data,files=files)
        js=json.loads(result.text)
        if (result.status_code==200):
            try:
                analyses_id.append(js['task_id'])
                pass
            except Exception as e:
                #logger.error(e)
                raise e
    #logger.debug("#### Sandboxed: '{filename}: {analyses_id}'".format(filename=filename,analyses_id=analyses_id))        
    return analyses_id

def run_engine(args):
    files = luke_filewalker(args.directory)
    ids=[]
    for f in files:
    	ids.extend(submit_to_cuckoo(f))
    print ids


def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--directory', help="directory to submit", action="store", required=True)
    args = parser.parse_args(arguments)
    run_engine(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
