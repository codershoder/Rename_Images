#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 sony <sony@ubuntu>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import Image
import sys
import os
import glob
import imghdr
import pdb
import file_recursive
from ExifTags import TAGS
EXIF_FOR_DATE_AND_TIME = "DateTimeOriginal"

d ={
    '01' : 'jan',
    '02' : 'feb',
    '03' : 'mar',
    '04' : 'apr',
    '05' : 'may',
    '06' : 'jun',
    '07' : 'jul',
    '08' : 'aug',
    '09' : 'sep',
    '10' : 'oct',
    '11' : 'nov',
    '12' : 'dec'
    }
def rename_with_format(fn,only_path,value,format_choice,file_extension,prefix):
	print 'only_path=%s' % only_path
	file_delimiter = ""
	date_and_time = value.split(' ')
	(year,month,date) = date_and_time[0].split(':')
	(hour,minute,sec) = date_and_time[1].split(':')
	new_name = only_path+year + "_" + d[month] + "_" + date + "_" + hour + ":" + minute + ":" + sec + "." + file_extension
	print 'new_name=%s' % new_name
	if os.path.exists(new_name):
		print '%s already exists , keeping it as it was, not modifying' % (fn)
		return
	else:
		os.rename(fn,new_name)

		
			
		
	

def get_exif(dir_path,fileDelimiter,format_choice,prefix=""):
    ret = {}
    choice = ""
    only_images = []
    only_path = fileDelimiter
    all_files = file_recursive.get_file_list_recursively(dir_path)
    for f in all_files:
		if not os.path.isdir(f) and imghdr.what(f):
			only_images.append(f)
    #print only_images
    for fn in only_images:
		#print fn
		full_path_list = fn.split(fileDelimiter)
		only_path=fileDelimiter
		for i in range(len(full_path_list)-2):
			only_path += full_path_list[i+1]+fileDelimiter
		#print 'only_path=%s' % only_path
		file_name = full_path_list[len(full_path_list)-1]# filename might be needed later
		file_extension = file_name.partition('.')[2]
		#print 'file_name=%s' % file_name
		#print 'file_extension=%s' % file_extension
		i = Image.open(fn)
		print 'Processing %s' % (fn)
		info = i._getexif()
		if not info:
			print ' Done processing %s' % (fn)
			continue
		for tag, value in info.items():
			if (TAGS.get(tag, tag)==EXIF_FOR_DATE_AND_TIME):
				#print value
				#temp = value.replace(':','_')
				#print 'temp='
				#print temp
				#temp=temp.partition(' ')
				#print 'temp2 = '
				#print temp
				#print only_path+(prefix+"_"+temp[0]+"__"+temp[2]+"."+file_extension)
				#pdb.set_trace()
				"""if os.path.exists(only_path+(temp[0]+"__"+temp[2]+"."+file_extension)) or os.path.exists(only_path+(prefix+"_"+temp[0]+"__"+temp[2]+"."+file_extension)):
					print '%s has same information as %s' % (fn,only_path+(temp[0]+"__"+temp[2]+"."+file_extension))
					print ' What do you want to do? (R) Replace,(K) Keep both,(D) Do not do anything'
					choice = raw_input("Enter---> ")
					print choice
					continue"""
				"""if (prefix):
					#print 'fn=%s' % fn
					os.rename(fn,only_path+(prefix+"_"+temp[0]+"__"+temp[2]+"."+file_extension))
				else:
					#'fn2=%s' % fn
					os.rename(fn,only_path+(temp[0]+"__"+temp[2]+"."+file_extension))    """
				rename_with_format(fn,only_path,value,format_choice,file_extension,prefix)
		
		print ' Done processing %s' % (fn)
			  

def main():
	#for arg in sys.argv:
	#	print arg
	#print get_exif(sys.argv[1])
	if sys.platform != 'linux2':
		print 'No support yet for Windows'
		sys.exit(0)
	arg = sys.argv[1:]
	print """ Enter your choice
	          1) YYYY_MM_DD__Hours_Minutes_Seconds
	          2) YYYY_MM_DD_Hours:Minutes:Seconds
	          3) YYYY_MON_DD__Hours_Minutes_Seconds
	          4) YYYY_MON_DD_Hours:Minutes:Seconds
	          0) Keep default option : YYYY_MM_DD__Hours_Minutes_Seconds"""
	format_choice = raw_input("---> ")
	print """ Enter the Prefix if you want, e.g. IMG, DSC etc, Press Enter for No Prefix(Default)"""
	prefix_choice = raw_input("---> ")
	if prefix_choice=="":
		get_exif(sys.argv[1],'/',format_choice)
	else:
		get_exif(sys.argv[1],'/',format_choice,prefix_choice)
	return 0

if __name__ == '__main__':
	main()

