import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)

    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # <img> element for the comic image is inside a <div> element with the id attribute set to comic
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        '''
        You join this name with the name of your xkcd folder using os.path.join() so that your program uses backslashes (\)
        on Windows and forward slashes (/) on macOS and Linux,  write binary'''
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        print('saving image to ' + imageFile.name)
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    '''
    he selector 'a[rel="prev"]' identifies the <a> element with the rel attribute set to prev, and you can use this <a> element’s href attribute to get the previous comic’s URL,'''
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done.')
