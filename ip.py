import android
import urllib
import urllib2
import subprocess

droid = android.Android()
internalip = ''
externalip = ''

title = 'Getting IP Addresses'
message = 'Please Stand By.'
droid.dialogCreateSpinnerProgress(title, message)
droid.dialogShow()

url = 'http://automation.whatismyip.com/n09230945.asp'
try:
  response = urllib2.urlopen(url)
  externalip = response.read()
except:
  pass

term = subprocess.Popen('netcfg', shell=False, stdout=subprocess.PIPE).communicate()[0]

for line in term.split('\n'):
	try: 
		if "UP" in line and not "127.0.0.1" in line and not "0.0.0.0" in line:
			internalip = line.split()[2]
	except:
		pass

droid.dialogDismiss()
title = 'IP'
message = 'Internal IP: ' + internalip + '\nExternal IP: '+ externalip
droid.dialogCreateAlert(title, message)
droid.dialogSetPositiveButtonText('Continue')
droid.dialogShow()