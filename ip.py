import android
import urllib
import urllib2
import re
import subprocess

droid = android.Android()
internalip = ''
externalip = ''

title = 'Getting IP Addresses'
message = 'Please Stand By.'
droid.dialogCreateSpinnerProgress(title, message)
droid.dialogShow()

url_increment = 0
url_list = ['http://checkip.dyndns.org', 'http://automation.whatismyip.com/n09230945.asp']

def get_external_ip(url):
    global url_increment
    global url_list
    htmlstring = ''
    ip = ''
    try:
        response = urllib2.urlopen(url)
        htmlstring = response.read()
    except:
        pass
    if htmlstring != '' and len(re.findall(r"\d{1,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}", htmlstring)) > 0:
        ip = re.findall(r"\d{1,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}", htmlstring)[0]
    else:
        if url_increment < len(url_list):
            url_increment=url_increment+1
            ip = get_external_ip(url_list[url_increment])
    if ip == '':
        ip = "Not Found"
    return ip

externalip=get_external_ip(url_list[url_increment])

term = subprocess.Popen('netcfg', shell=False, stdout=subprocess.PIPE).communicate()[0]

for line in term.split('\n'):
    try: 
        if "UP" in line and not "127.0.0.1" in line and not "0.0.0.0" in line:
            internalip = line.split()[2]
    except:
        pass


droid.dialogDismiss()
title = 'IP'
if internalip == externalip:
  message = 'IP: '+ externalip
else:
  message = 'Internal IP: ' + internalip + '\nExternal IP: '+ externalip 

print message
droid.dialogCreateAlert(title, message)
droid.dialogSetPositiveButtonText('Continue')
droid.dialogShow()