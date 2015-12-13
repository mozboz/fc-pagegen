# fc-pagegen

Written for use in the first-contact.org websites, generates HTML by reading values from a Google Sheet which are then passed into a handlebars template. 

Maintains the simplicity of handlebars for templating, and flexibility of Google Sheets for recording information in different formats.

Requires python2 to render, apache2 & php to serve. If you're not using apache, you'll need to do some URL rewriting in your chosen httpd according to the mod_rewrite rules in www/.htaccess

```
sudo apt-get install python-dev
sudo apt-get install libffi-dev

pip install -r requirements.txt
```

For web server setup, ensure mod_rewrite is on and 'AllowOverride' is allowed for your web directory.

To test first see the notes in at the end of rundmc.py about how to create an oauth2 token and configure any paths. You'll need to carry out this process which should result in a .json file, put that file in the same directory as the python script, and update the variable 'credentialsFileName' to reflect the file name.

Then, you need a copy of a Google Sheet that looks like this: https://docs.google.com/spreadsheets/d/1LbppGU5e4NbpnHn9vGRe0Z4QpatdCIg9Bygf3RQjas0/edit#gid=0

The sheet is referenced by its **title**. Ensure that the variable sheetTitle contains the name of a sheet accessible by the OAuth user.

When all setup, to generate all static files, run:

    python rundmc.py
    
Or, ensure all the above dependencies are installed on a LAMP server, and call recompile.php?recompile=go via a browser.

All output goes to the www directory. Copy it to your web server and browse to the root!

