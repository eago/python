from bs4 import BeautifulSoup, element

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "lxml")

# print(soup.prettify())

# print(soup.title)

# print(soup.head)

# print(soup.a)

# print(soup.p)

# print(type(soup.a))
# print(soup.name)
# print(soup.head.name)

#attributs
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.get('class'))
# soup.p['class']="newClass"
# print(soup.p)

# del(soup.p['class'])
# print(soup.p)

# print(soup.p.string)
# print(type(soup.p.string))

# print(type(soup.name))
# print(soup.name)
# print(soup.attrs)

# print(soup.a)
# print(soup.a.string)
# print(type(soup.a.string))

# if (type(soup.a.string) == element.Comment):
#     print(soup.a.string)

# print(soup.head.contents[0])
# print(soup.head.children)
# for child in soup.body.children:
#     print(child)

# for child in soup.descendants:
#     print(child)

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

print(soup.find_all(has_class_but_no_id))