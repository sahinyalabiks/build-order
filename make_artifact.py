"""Builds artifact.html (the phone-ready page that gets published) from index.html."""
import re
s = open('index.html').read()
style = re.search(r'<style>.*?</style>', s, re.S).group(0)
body = re.search(r'<body>(.*)</body>', s, re.S).group(1)
head = '<title>Build Order</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
open('artifact.html', 'w').write(head + style + '\n<script>window.FORCE_BARE=1</script>' + body)
print('artifact.html written')
