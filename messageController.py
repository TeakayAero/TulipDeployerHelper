import sys
import requests

testToken = ""
link = "https://tulip.slack.com/api/chat.postMessage?"

try:
    length = len(sys.argv) #7 if master #8 if branch
    message = ''
    master = False
    server = sys.argv[1]
    gitRepo = sys.argv[2]
    channel = '#' + sys.argv[3]
    branch = sys.argv[4]
    fn = ' (' + sys.argv[5] +')'
    serverRepo = server + ':' + gitRepo
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    if(length == 8 and sys.argv[7] != '&empty^_flag$'):
        message = '\n' + sys.argv[7].replace('*__*', ' ')
    elif(length == 7 and sys.argv[6] != '&empty^_flag$'):
        message = '\n' + sys.argv[6].replace('*__*', ' ')
        master = True

    if(master):
        msg = "Deploying master to " + serverRepo + fn + message
    elif(sys.argv[6] == 'done'):
        msg = serverRepo + " is free now" + fn + message
    else:
        msg = "Deploying " + branch + ' to ' + serverRepo + fn + message

    data = { 'token':testToken,
             'channel':channel,
             'text':msg,
             'as_user': True}
    response = requests.post(link, data, headers=headers).json()
    if(response['ok'] == False):
        print response['error']
    else:
        print 'message successfully delivered'
except:
    print "Unexpected Error"
