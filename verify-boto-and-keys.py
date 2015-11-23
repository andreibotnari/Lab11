import urllib2
import string
import boto
print ("Boto Vrsion"+boto.Version)

req = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
req = req.read()
key = req.split(":")

print("ID:" +key[0])
print("\n" +key[1])