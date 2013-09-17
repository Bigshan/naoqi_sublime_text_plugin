#!/usr/bin/python
# -*- coding: utf-8 -*-

# parse the naoqi documentation and creates a text file suitable for creating a Sublime Text plugin
# Mike McFarlane
# v0-1: 23 Aug 2013, crawl docs and build a list of methods, classes and frameworks
# TODO: BeautifulSoup - done
# TODO: check for deprecated APIs

"""look for <dl class="function"> for the start of each method """
""" then get everything between <dt and </dt> """
"""look for first instance of <a class="reference internal" href="../stdtypes.html# then title=" for return type """
"""look for <tt class="descclassname"> for class """
"""look for <tt class="descname"> for methods """
"""look for second instance of <a class="reference internal" for arguments """

import fnmatch
import os
from bs4 import BeautifulSoup

def get_html_file_list():
	"""finds all the HTML API docs in a defined folder"""
	"""returns the list of html files as a list and writes them to a file"""

	PATH = '/Users/mikemcfarlane/Desktop/NAO_doc/doc-release-1.14-public/naoqi'
	pattern = '*api*.html'

	f = open("html_list.txt", "w")
	html_list = []
	 
	for root, dirs, files in os.walk(PATH):
	    for filename in fnmatch.filter(files, pattern):
	        #print (os.path.join(root, filename))
	        f.write((os.path.join(root, filename)) + "\n")
	        html_list.append((os.path.join(root, filename)))
	f.close()
	return html_list

def find_methods(html_list):
	"""crawl all the html api docs and create a list with all the methods in"""
	"""returns the methods list still in html tagged form"""

	file_dump = open("file_dump.txt", "w")

	methods_html = []
	for api_file in html_list:
		try:
			f = open(api_file, "r")			
		except:
			print "Error finding: " + api_file
			return None
		file_contents = f.read()
		index = 0
		while True:
			start_method = file_contents.find("""<dl class="function">""", index)
			if start_method == -1:
				break
			else:
				start_dt_tag = file_contents.find("<dt", start_method)
				end_dt_tag = file_contents.find("</dt>", start_dt_tag)
				method_info = file_contents[start_dt_tag + 4:end_dt_tag]
				methods_html.append("--" + api_file + "--" + method_info)
				index = end_dt_tag
				#file_dump.write(api_file +  "\n")
				file_dump.write("--" + api_file + "--" + method_info + "\n\n")				
		f.close()
	file_dump.close()
	return methods_html

def find_arguments(arg_string):
	#find the arguments and tidy them up
	#returns a list of the arguments
	start_string = arg_string.find("(") + 1
	end_string = arg_string.find(")")
	arg_string = arg_string[start_string:end_string]
	#remove ampersand chars
	arg_string = arg_string.replace("&", "")
	arg_list = []
	while True:
		comma_position = arg_string.find(",", 0)
		if comma_position == -1:
			arg_list.append(str(arg_string))
			break
		else:
			arg_list.append(str(arg_string[:comma_position]))
			arg_string = arg_string[comma_position+2:]
	return arg_list

def build_methods_dictionary(methods_html):
	"""build a dictionary of relevant info for each method"""
	"""return a dictionary"""
	methods_dictionary = {}
	
	for i in methods_html:		
		#find framework name
		start_framework = i.find("/naoqi/", 0) + len('/naoqi/')
		end_framework = i.find("/", start_framework)
		framework = i[start_framework:end_framework].upper()
		#find return type, class, method and arguments
		#need to remove the space in 'reference internal' or not recognised as class by beautiful soup
		j = i.replace("reference internal", "referenceinternal")
		soup = BeautifulSoup(j)
		first_internal_index = 0
		for i in soup.select(".referenceinternal"):
			if first_internal_index == 0:
				print "return: " + i.string
				first_internal_index = 1
			nao_arg_list = find_arguments(soup.get_text())
		for i in soup.select(".descclassname"):
			nao_class = i.string
		for i in soup.select(".descname"):
			nao_method = i.string + "\n"
		print "Framework: " + framework
		print "Class: " + nao_class
		print "Method: " + nao_method
		for i in nao_arg_list:
			print "Argument: " + i
		print "\n"

		
html_list = get_html_file_list()
methods_html = find_methods(html_list)
build_methods_dictionary(methods_html)







