# asciifarts

ASCII Art Farts  is an [epic archive](http://www.asciiartfarts.com/index.html) of over five thousand pieces of ASCII art from 1996-2014. This is a bare bones script that grabs and prints a random ASCII from the collection. 

## Install

**NOTE:** If your system uses Python 3.5 and older, use the asciifarts3.5.py script instead.

This example is for `irssi` - but it shouldn't be too different for other
clients. The path `~/.irssi/` is totally arbitrary: copy the script wherever
you want, as long as you have the correct permissions.

```bash
[pump@linux ~]$ git clone https://github.com/m0n73/asciifarts.git
[pump@linux ~]$ cp asciifarts/asciifarts.py ~/.irssi/ 
[pump@linux ~]$ chmod +x ~/.irssi/asciifarts.py
```
In your client:

`/alias randomascii exec -o ~/.irssi/asciifarts.py 2>> ~/.irssi/asciifarts.log`

DGAF about logs? Substitute `2>> ...` with `2> /dev/null`.

If you got problems/requests submit them via `/server notice m0nt3 <your message here>` on EFNet.
