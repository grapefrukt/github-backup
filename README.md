github backup
=============================

A tiny python script to automatically clone/pull all your github repositories

Seeing as no service is immune to outages and/or catastrophic failures, it's always wise to have a local copy of all your work. I have many repositories, neither of them are all on one computer. 

This script can be run once or on a schedule and will clone/pull all your repositories, public as well as private. 

Configuration
--------------

The script will read your username and API key from github-backup.cfg, a template is supplied. Generate your API key here: https://github.com/settings/tokens/new


Dependencies
-------------

You will need pygithub3 to run this script. Install it thusly:

    pip install pygithub3