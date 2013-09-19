<h1>naoqi Sublime Text 2 plugin package</h1>

A plug-in package for Sublime Text 2 (http://www.sublimetext.com/) for writing NAOqi Python API code for Aldebaran Robotics NAO robot (http://www.aldebaran-robotics.com/). Allows you to write NAOqi Python on Mac OS X, Linux and Windows in a very clean and fast text editor. Can then be used in Choregraph or run directly on NAO.

<h2>Functionality</h2>
The plug-in provides the following functionality:
<ol>
<li>Python syntax color formatting via the Command Palette.</li>
<li>Basic NAOqi Python code snippets via the completions list.</li>
<li>Auto-complete of NAOqi methods via the completions list.</li>
<li>Search for relevant NAOqi classes, methods and 'frameworks' (Core, Motion, Audio, Vision, Sensors, Trackers, ConnectionManager) via the completions list.</li>
<li>Tabbed completion of method arguments after a method with arguments selected.</li>
<li>Currently for NAOqi v1.14, but there is a Python documentation crawler included if you want to build completions for another version of NAOqi.</li>
</ol>

<h2>Installation:</h2>
<ol>
<li>Download naoqi_v*-*.sublime-package</li>
<li>Copy naoqi_v*-*.sublime-package to ~/Library/Application Support/Sublime Text 2/Installed Packages on Mac OS X. There are Linux and Windows installation instructions at http://docs.sublimetext.info/en/latest/extensibility/packages.html</li>
<li>Start Sublime Text and the package should auto-install.</li>
</ol>
There are a few ways to check this, the easiest is to open the Command Palette and type 'syntax' and look for 'naoqi' in the list.
Once the code is a bit better I will get it registered to install with the excellent Package Control (http://wbond.net/sublime_packages/package_control) 

<h2>Usage</h2>
Once naoqi syntax selected from the Command Palette. The main naoqi functionality is in the methods, classes and 'frameworks' completion list.
<ol>
<li>To auto-complete a method, class or snippet, start typing a method name, class name or code snippet name using lower case and access the completions list with CTRL+spacebar. Each argument within a method can be jumped between with the TAB key.</li>
<li>To search for all the methods and classes within a 'framework' (Core, Motion, Audio, Vision, Sensors, Trackers, ConnectionManager), start typing a 'framework' name in UPPER case e.g. 'VISION' will list all the commands related to the Vision APIs.</li>
</ol>

<h2>To create your own completions</h2>
<ol>
<li>If you wish to make your own completions file e.g. for older or newer versions of NAOqi.</li>
<li>My crawler may not be robust enough yet until re-written and tested on other versions of the documentation.</li>
<li>Download the version of the documentation you need. (It's just a bit quicker than a web crawl.)</li>
<li>Get 'naoqi_documentation_crawler.py' from my Github page https://github.com/mikemcfarlane/naoqi_sublime_text_plugin</li>
<li>You will need Beautiful Soup 4 library http://www.crummy.com/software/BeautifulSoup/</li>
<li>Edit the 'PATH' variable in the function 'get_html_file_list' in naoqi_documentation_crawler.py, it should point to the folder 'naoqi' within the downloaded folder.</li>
<li>In the terminal run 'python naoqi_documentation_crawler.py'.</li>
<li>Move the resulting 'naoqi.sublime-completions' file into the Sublime Text plugin directory from above.</li>
<li>Go code:-)</li>
</ol>

<h2>Versions:</h2>
<ul>
<li>0.1 - getting something working, using NAOqi v1.14.</li>
</ul>

<h2>To do:</h2>
<ol>
<li>Current snippets are standard Python ones, so they need checked.</li>
<li>More NAOqi snippets needed, the only one currently is 'Choregraph box'. Email me any you want included.</li>
<li>Documentation crawler needs re-written to be more robust using Beautiful Soup.</li>
<li>Needs to highlight or remove deprecated methods.</li>
<li>Add events, proxies ....</li>
</ol>

<h2>Bugs:</h2>
Report to 'mike >-at-< mikemcfarlane >-dot-< co >-dot-< uk' or discuss on Aldebaran forum thread.
<ol>
<li>Not showing arguments for some methods. - fixed tbc</li>
</ol>


<h2>Attribution:</h2>
<ol>
<li>Uses standard Sublime Text Python package and snippets as a base.</li>
<li>Uses NAOqi documentation created by Aldebaran Robotics.</li>
</ol>

<h2>License:</h2>
MIT

