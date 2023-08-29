####################################################
####################################################
'''####################################################

Stop
loofpdkodklsolo
This code is outdated.

   ####################################################'''
####################################################
####################################################

from bs4 import BeautifulSoup
import re

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
    
    # Find URLs in background-image style attributes
    for element in soup.find_all(style=True):
        fix_style_url(element, 'style', target_url)
    
    return soup.prettify(formatter='html')

def fix_url(tag, attr, target_url):
    url = tag.get(attr, '')
    if url and not url.startswith(('http://', 'https://')):
        # Join the relative URL with the target URL and remove quotes
        fixed_url = target_url + url.replace('"', '')
        tag[attr] = fixed_url

def fix_style_url(tag, attr, target_url):
    style_content = tag.get(attr, '')
    matches = re.findall(r'url\((.*?)\)', style_content)
    for match in matches:
        fixed_url = target_url + match.replace('"', '')
        style_content = style_content.replace(match, fixed_url)
    tag[attr] = style_content


# Example HTML content
example_html = '''
<!DOCTYPE html>
<html>
  <head>
  <link rel="icon" href="home/images/favicon.png">
  <!--Start of Tawk.to Script
  
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/6455c179ad80445890eb6555/1gvnfnhi2';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
</script>

   End of Tawk.to Script-->
   
  <script>
    function checkMaintenance() {
      fetch('./API/maintenance.txt', { cache: 'no-cache' })
        .then(response => response.text())
        .then(data => {
          if (data.trim().toLowerCase() === 'false') {
            window.location.href = './home/';
          }
        })
        .catch(error => {
          console.error('Error loading maintenance file:', error);
          // Handle the error condition here
        });
    }

    setInterval(checkMaintenance, 1500);
  </script>


<style>
body {
  background-image: url('./bruh.png');
  background-repeat: repeat;
  background-size: 1560px;
}
</style>

<h2> 
Hello there. <br>
The website is currently in maintenance mode as you have most likly noticed by now, for one of the following reasons:<br>
-   API failure<br>
-   Mass update<br>
-   Lag<br>
-   Other....<br>
</p>

</h2>

<button><a href="./home/" disabled >Continue to Website</a></button>

<p>A note for people using this as part of FireBird - all services remain online. This take-down only affects the games part of the network, and the actuall FireBird parts remain online & updated. </p>
  </body>
</html>
'''

# Example target URL
target_url = 'https://example.com/'

# Fix URLs in the example HTML content
fixed_html = fix_urls_in_html(example_html, target_url)

# Print the fixed HTML content
print(fixed_html)
