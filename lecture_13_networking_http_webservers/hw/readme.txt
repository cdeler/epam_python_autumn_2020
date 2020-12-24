NO HOMEWORK for this topic, enjoy the lab.


If you still want to know something about webservers and try running webserver by yourself,

I'd recommend taking BOTH:

 - django official tutorial located at https://docs.djangoproject.com/en/3.1/intro/tutorial01/
 - flask tutorial from habr (https://habr.com/ru/post/346306/)


why it's important to do both? to understand similarities and differences on how webservers are handled in python.

Next step would be trying to DEPLOY and RUN your webserver in internet. Buy a cheap virtual server from one of the numerous providers,
they cost around 10$ per month, and play with that. You will have to learn about SSH and linux command line a bit to make it work.

Linux command line and ssh tutorial can be found here:
    
  - Command line: https://ubuntu.com/tutorials/command-line-for-beginners#1-overview

To put webserver code into remote server
  - You can install git on the server and use git to PULL your webserver code from github repository (recommended way)
  OR
  - You may use ssh and copy files to remote machine: https://www.pragmaticlinux.com/2020/07/how-to-copy-files-via-ssh/

Also there's a commander-style terminal program that works in SSH terminals: midnight commander (mc) that you may find useful.
Try playing with it as well.

- start deploying your server by running your application only by using built-in server (like django runserver command). Be sure to disable debug mode.
- add gunicorn on top of your application to be able to serve more than 1 request at once
- you may add nginx on top of gunicorn to serve static files if your web framework does not support that
- you may add supervisord to keep your webserver running in case of reboots or errors

If you will need a database or cache server, you can run mariadb or postgresql on the same machine.
This will cover your basic needs if you'd want to run a website by yourself.
