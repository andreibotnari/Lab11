# This script created a queue
#
# Author - Paul Doyle Aug 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import urllib2

import sys
sys.path.append('/data')
keypart1 = urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read()
access_key_id, secret_access_key = keypart1.split(':')

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

rs = conn.get_all_queues()
for q in rs:
	print q.id
