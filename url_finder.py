from bs4 import BeautifulSoup
import re


def log(url):
  file = open('LOGS\img.log', 'a')
  file.write('\n' + url)
  file.close()


# hi
# ok


def fix_urls_in_html(html_content, target_url):
  soup = BeautifulSoup(html_content, 'html.parser')

  # Find all URLs in href attributes of <a> tags
  for a_tag in soup.find_all('a', href=True):
    fix_url(a_tag, 'href', target_url)

  # Find all file locations in src attributes of <img> tags
  for img_tag in soup.find_all('img', src=True):
    fix_url(img_tag, 'src', target_url)

  for iframe_tag in soup.find_all('iframe', src=True):
    fix_url(iframe_tag, 'src', target_url)

  for embed_tag in soup.find_all('embed', src=True):
    fix_url(embed_tag, 'src', target_url)

  for script_tag in soup.find_all('script', src=True):
    fix_url(script_tag, 'src', target_url)

  for style_tag in soup.find_all('style', src=True):
    fix_url(style_tag, 'src', target_url)

  for source_tag in soup.find_all('source', src=True):
    fix_url(source_tag, 'src', target_url)

  for link_tag in soup.find_all('link', src=True):
    fix_url(link_tag, 'src', target_url)

  # Find URLs in background-image style attribute
  for element in soup.find_all(style=True):
    fix_style_url(element, 'style', target_url)

  return soup.prettify(formatter='html')


def fix_url(tag, attr, target_url):
  url = tag.get(attr, '')
  if url and not url.startswith(('http://', 'https://')) and not url[0] == '#':
    # Join the relative URL with the target URL and remove quotes
    fixed_url = target_url + '/' + url.replace('"', '')
    log(fixed_url)
    tag[attr] = fixed_url
  elif url and url.startswith(('http://', 'https://')) and not url[0] == '#':
    fixed_url = target_url + '/' + url.replace(
        '"', '').lstrip('https://').lstrip('http://')
    log(fixed_url)
    tag[attr] = fixed_url


def fix_style_url(tag, attr, target_url):
  style_content = tag.get(attr, '')
  matches = re.findall(r'url\((.*?)\)', style_content)
  for match in matches:
    fixed_url = target_url + match.replace('"', '')
    style_content = style_content.replace(match, fixed_url)
  tag[attr] = style_content


"""
# Example HTML content
example_html = '''
<body class="u-body u-image u-image-tiles u-xl-mode" data-lang="en" style="background-position: 50% 50%; background-image: url(&quot;images/2wallpapersden.com_colorful-curves_1920x10801.jpg&quot;);">
    <section class="u-clearfix u-image u-section-1" id="sec-f8bd" data-image-width="1920" data-image-height="1280">
</body>
'''

# Example target URL
target_url = 'https://example.com/'

# Fix URLs in the example HTML content
fixed_html = fix_urls_in_html(example_html, target_url)

# Print the fixed HTML content
print(fixed_html)
"""
