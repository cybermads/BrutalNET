# Author: cybermad
# BrutalNET network denial-of-service through ARP Spoofing.

import os

h = "\033[38;5;118m"
c = "\033[91m"
b = "\033[41m"
g = "\033[92m"
r = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
{c}
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
      
{r}    
    {g}[*]{r}      {h}ARP Attack Tool.{r}                 {g}[*]{r} 
    {g}[*]{r}      {h}Version : 1.0{r}                    {g}[*]{r} 
    {g}[*]{r}      {h}Created :{c} {c}cybermad{r}               {g}[*]{r}
    {g}[*]{r}      {h}github  : github.com/cybermads{r}   {g}[*]{r}
    {g}[*]{r}      {h}youtube : youtube.com/@cybermads{r} {g}[*]{r}
            
    {c}network device discovery.{r}

          """)
def scan():
    banner()
    iface = input(f"[{c}+{r}] interface{c}:{r} ")
    os.system(f"arp-scan -l -I {iface}")

    input(f"[{c}+{r}] Finish{c}...{r}")


