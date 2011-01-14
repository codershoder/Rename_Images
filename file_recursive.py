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

import os, glob
ret = []
def get_file_list_recursively(path):
    for currentFile in glob.glob( os.path.join(path, '*') ):
        if os.path.isdir(currentFile):
            ret.append(currentFile)
            get_file_list_recursively(currentFile)
        ret.append(currentFile)
    return ret


def main():
	''' Returns list of all files recursively , takes path as an argument'''
	print get_file_list_recursively('/media/Elements/New Folder/torrentssss/The Most Relaxing Classical Music in the Universe/The Most Relaxing Classical Music in the Universe')
	return 0

if __name__ == '__main__':
	main()

