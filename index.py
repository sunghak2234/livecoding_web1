#!C:\Users\doch2\AppData\Local\Programs\Python\Python38\python.exe
print("content-type: text/html; charset=utf8\n")

import cgi

if pageId:
    form = cgi.FieldStorage()
    pageId = form['id'].value

else:
    pageId = 'welcome'

print("""
<!doctype html>
<html>
<head>
<title>abcd</title>
<meta charset="utf-8">
</head>


<body>

    <h1> <a href="index.py"> WEB - welcome </a> </h1>

<ul>
<li><a href="index.py?id=HTML1">html</a></li>
<li><a href="index.py?id=CSS1">css</a></li>
<li><a href="index.py?id=JavaScript">JavaScript</a></li>
</ul>


<h2>{title}</h2>

<p>

The World Wide Web (WWW), commonly known as the Web, is an information system where documents and other web resources are identified by Uniform Resource Locators (URLs, such as https://example.com/), which may be interlinked by hyperlinks, and are accessible over the Internet.[1][2] The resources of the Web are transferred via the Hypertext Transfer Protocol (HTTP), may be accessed by users by a software application called a web browser, and are published by a software application called a web server. The World Wide Web is not synonymous with the Internet, which pre-dated the Web in some form by over two decades and upon the technologies of which the Web is built.

</p>

</body>
</html>



""".format(title=pageId))
