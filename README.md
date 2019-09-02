# Tao
A Slack bot for sharing the words of the Tao.

That's all it does. It's simple that way, get it?



**Motivation**

I need to get better at networked python programming, and also to learn to use APIs. It's not perfect, but it's a first API project. And I made something I actually enjoy using, that's always nice.  

**Configuration (Abridged)**

​	-Create a new slack bot, called tao, at api.slack.com. Collect some tokens for later. 

​	-Go to "Slash commands". Create one. Call it /tao. 

​	-Give it the request URL of, in my case, my home router and a chosen port, 8100.

​	-Forward the chosen port on my router to my laptop. (To be updated to a rasbperry pi I have later)

​	-Run the taobot.py on my laptop. Keep the secrets secret.

​	-say /tao in your slack channel. Recieve some tao.txt back. enjoy.

**Files**

`tao.txt` is the raw, copied-and-pasted tao.txt source.

`taocutter.py` is the python code I used to turn `tao.txt` into what's eventually used in the bot.

`formatted_tao.txt` holds that formatted text.  

`taobot.py` is the actual bot. It pulls from `formatted_tao.txt` when making a post. 



**Sources**

The primary source, of course, is [Ron Hogan's TAO.txt](http://www.beatrice.com/TAO.txt). I like this translation of the I Ching. I also love how fitting it is that it's a .text file; it adds to the simple feel of the whole thing. 

Some of the basic networking structure comes from the [Black Hat Python](https://nostarch.com/blackhatpython) book, like most of my networked python projects. 



**To Do**

-*Migrate to Pi*. I was having some issues getting the slack python library working on my raspberry pi for some unknown reason. I've been doing the development off my laptop in the meantime, but to get it working 24/7 it's got to go to the pi. 

-*Talk back to slack*. Currently, the bot "works", except that it also returns a timeout response to the user in the slack channeel. I have to make my bot talk back the right way to make that stop. 

-*[maybe]* Stick good taos together. My `taocutter.py` did a good job, but not perfect- some sections are split in half where they shouldn't be. That'll have to be done by hand- manually put contextually appropriate Taos together. 