from replit import *
import base64  # I formatted this import block 
import datetime
import os
import re
import threading
import time
from os import error
from bs4 import BeautifulSoup
import bottle
from bottle import response
from tqdm import tqdm
from pathlib import Path
import requests
import url_finder
import console_colors as cc
import banners as banner
os.system('pip3 install filetype')
import filetype
import __main__

Notice = ['''
Outputs from server have been silenced.
&*^&^&You really thought it was that easy&(&^*)
''']

V = 0
total_phases = 6
phases = [
    "Initializing", "Starting host", "Configuring", "Server online!",
    "Starting timed ping", "Ready"
]

progress_bar = tqdm(total=total_phases, desc="Server", unit=" Stages")
banner_icon = banner.set(False)


def n(c):
  time.sleep(0)
  os.system("clear")
  cc.p.text(Notice[0], bg_color="black", c="white")
  cc.p.text(banner_icon, bg_color="black", c="magenta")
  progress_bar.set_description(f"Boot: {phases[c]}")
  progress_bar.update(1)


n(V)
time.sleep(0.1)
n(V)

#########################################################

prev = 'example.com'
base = 'https://proxyportal.figs4pigs.repl.co/'


def KPO():
  #Keep the Portal Open, ProxPort
  W = 4  # every 4 minutes
  time.sleep(W * 60)
  z = str(os.system("Test-NetConnection proxport.figs4pigs.repl.co -Port 443"))
  z = z  # idk.... ###theo###, why
  z = str("")  #why

class log:
  @staticmethod
  def __init__(url):
    file = open('LOGS/req.log', 'a')
    file.write('\n' + url)
    file.close()

  @staticmethod
  def site(url, addr):
    site = findsite(url)
    file = open('sites.log', 'a')
    file.write('\n.reqst|' + site + '|' + addr + '|' + str(time.time()))
    file.close()

def findsite(url):
  return ('/' + url.lstrip('/')).split('/')[1]

def load(file):
  file = open('ifiles/' + file, 'r')
  trt = file.read()
  file.close()

  return trt


def load404(url):
  file = open('site/404.html', 'r')
  error = file.read()
  file.close()

  return error
  
  
  

class trout:
  @staticmethod
  def load(lid):
    file = open('trout/' + lid, 'r')
    trt = file.read()
    file.close()
  
    return trt
  
  @staticmethod
  def apnd(lid, data):
    if lid in os.listdir('trout'):
      file = open('trout/' + lid, 'a')
      file.write('\n' + data)
      file.close()
  
      return 'success.'
    else:
      return 'file non-existant.'


def get(site):
  try:
    req = requests.get(f'https://{site}')
    return req.content, req.headers[
        'content-type'] if 'content-type' in req.headers else (
            req.headers['Content-Type'] if 'Content-Type' in req.headers else
            (req.headers['CONTENT-TYPE']
             if 'CONTENT-TYPE' in req.headers else 'text/html'))
  except:
    return load404(site), 'text/html'


############### END OF DEFINITIONS######################


@bottle.route('/prportal/ifiles/<file>')
def ifiles(file):
  try:
    return load(file)
  except:
    return 'invalid filename.'


@bottle.route("/prportal/headers")
def headerget():
  headers = dict(request.headers)
  url = headers.get("url", "")  # Read URL from headers
  proto = headers.get("proto", "")  # Read proto from headers
  if not url:
    return "No URL provided in headers."

  try:
    x = requests.get(f"{proto}://{url}")
    response.status = x.status_code
    response.content_type = "text/html"  # Set content type to HTML
    return x.text  # Return HTML content
  except requests.RequestException as e:
    return f"Error: {e}"


@bottle.route('/prportal/trout/load/<logid>')
def load_trout(logid):
  response.content_type = 'text/plain'
  return trout.load(logid)


@bottle.route('/prportal/trout/apnd/<logid>/<data>')
def load_trout2(logid, data):  # I added the 2 bc it was a dupe name
  response.content_type = 'text/plain'
  return trout.apnd(logid, data)


@bottle.route('/<path:path>')
def load_site(path):
  global prev
  log.site(path, bottle.request.environ['REMOTE_ADDR'])
  html, ctyp = get(path)
  log(path)
  hurl = '/' + path
  webs = hurl.split('/')[1]

  response.content_type = ctyp

  log(ctyp)
  if ctyp == 'text/html':
    #html = html.decode()
    if '.' in webs:
      fixh = url_finder.fix_urls_in_html(
          html, base + '/' + '/'.join(hurl.split('/')[:-1]))
      prev = webs
    else:
      bottle.redirect(f'/{prev}{hurl}')

    return fixh
  else:
    if '.' in webs:
      prev = webs
    else:
      bottle.redirect(f'/{prev}{hurl}')

    return html


#assainging website to path
# the reason why i have if is because i want to turn it into a functions but i can't yet.

runs = 0
orgin_direc= None
def assignweb(direc, prompt=""):
  if direc[-1] == '/':
    if direc[0] == '/':
      direc = direc[1:-1]
    elif direc[0:1] == './':
      direc = direc[2:-1]
    else:
      direc = direc[:-1]

  elif direc[0] == '/':
    direc = direc[1:]
    
  if prompt !='':
    if prompt[0] == '/' and prompt[-1] == '/':
      prompt = prompt[1:-1]
  
    elif prompt[0] == '/':
      prompt = prompt[1:]
  
    elif prompt[-1] == '/':
      prompt = prompt[:-1]

  
  global orgin_direc
  global runs
  orgin_direc = direc if runs == 0 else orgin_direc
  
  runs +=1
  if prompt !='':
    prompt = f'/{prompt}'
  h_direc = direc.replace(orgin_direc, prompt)
  log(h_direc)
  
  classamount = len(h_direc.split("/"))-1
  exec_class=""
  classprefix=""
  for i in h_direc.split("/")[1:]:
    exec_class += f" class {i}:"
    classprefix += f"{i}."
  classprefix= classprefix[:-1]
  
  exec(exec_class[1:]+" pass" if len(h_direc.split("/")) > 1 else "")
  
  exec(f"globals()[classprefix] = {classprefix}" if len(h_direc.split("/")) > 1 else "")
  
  
  
  regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
  for i in os.listdir(direc):
    #repeats twice for both ext_func and func
    for j in range(2):
      try:
        name = i[::-1].split('.')[1][::-1]
        ext = i[::-1].split('.')[0][::-1]
        
      except:
        name = i
        ext = "None"

      func_name = name if i[0].isalpha() and j == 0 else f"{ext}_{name}"
      while regex.search(name) != None:
        for i in tuple('[@!#$%^&*()<>?/\|}{~:]'):
          func_name = func_name.replace(i, '') if i in func_name else func_name
      func_name = func_name.replace(' ', "_")

      if Path(f'./{direc}/{i}').is_file():
        #with extension
        defintion_ext = f'''\
@bottle.route('{h_direc}/{i}')
def {func_name}():
  return bottle.static_file("{i}", root="./{direc}/")

{f'{classprefix}.{func_name}' if classprefix != "" else f"globals()['{func_name}']"} = {func_name}
''' 
        #without extension
        defintion = f'''\
@bottle.route('{h_direc}/{name}')
def {func_name}():
  return bottle.static_file("{i}", root="./{direc}/")
''' if ext=='html' or ext=='htm' else ''
        
        #adds index.html as /
        defintion_index = f'''
@bottle.route('{h_direc}/')
def {func_name}():
  return bottle.static_file("{i}", root="./{direc}/")
  
@staticmethod
def init(): 
  return None

@staticmethod
def repr():
  return repr(bottle.static_file("index.html", root="./site/hi/"))
  
# THEO LOOK HERE: cloud.digitalocean.com LOGING WITH THE figs4pigs GOOGLE ACCOUNT and pass is M-SYSTEM123123M NOW. BEFORE I ACHRIVE THIS REPL. IF you migrate i wont archive this repl :)

{f'{classprefix}.__init__' if classprefix != "" else f"globals()['{func_name}']"} = init

{f'{classprefix}.__repr__' if classprefix != "" else f"globals()['{func_name}']"} = repr
''' if i == 'index.html' else ''

        #adds 404 error
        defintion_err = f'''
@bottle.error({name})
def {func_name}():
  return html_404()
''' if name == '404' else ''

      else:
        defintion=''
        defintion_ext=''
        defintion_index=''
        defintion_err=''
      
      #test to see if it is a directory
      fileordir = Path(f'./{direc}/{i}')
      isdir = fileordir.is_dir()
      isfile = fileordir.is_file()
      
      if isfile:
        exec(defintion)
        exec(defintion_ext)
        exec(defintion_index)
        exec(defintion_err)

      else:
        assignweb(f'{direc}/{i}', prompt)


assignweb('site')


'''
with this code everything in the website folder will get a directory. Maybe you could use nicepage to desing. My code also checks if the first character is a letter because func need to start with letter.
'''
class proxyportal:
  @staticmethod
  def __init__(ip='0.0.0.0', port=80):
    global V
    import time
    V += 1
    n(V)
    KPO_thread = threading.Thread(target=KPO)
    KPO_thread.start()
    V += 1
    n(V)
    time.sleep(0.5)
    V += 1
    n(V)
    
    V += 1
    n(V)
    
    th = threading.Thread(target=lambda: bottle.run(
        host=ip, port=port, server='paste', quiet=True))
    bottle_res = th.start()
    import time
  
    if 1:
      session_time = 0
      while 1:
        # stay'in alive
        session_time += 1
        log(str(session_time))
        time.sleep(1)
    
    V += 1
    n(V)
  
  # <img class="u-back-image u-expanded" src="https://proxyportal.figs4pigs.repl.co/figs4pigs.comimages/starship.png">

  
if __name__ == '__main__':
  proxyportal()

'''
alive = threading.Thread(target=lambda: keepalive())
a= alive.start()
  
'''

