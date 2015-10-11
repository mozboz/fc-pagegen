# fc-pagegen

Written for use in the first-contact.org websites, generates HTML by reading values from a Google Sheet which are then passed into a handlebars template. 

Maintains the simplicity of handlebars for templating, and flexibility of Google Sheets for recording information in different formats.

Requires python2

```
sudo pip install oauth2client
sudo pip install pymeta
sudo apt-get install python-dev
sudo apt-get install libffi-dev
sudo pip install PyOpenSSL
```

To test first see the notes in loadNameValueDataFromSheet in rundmc.py about how to create an oauth2 token. You'll need to carry out this process which should result in a .json file, put that file in the same directory as the python script, and update the variable 'credentialsFileName' with its file name.

Then, you need a copy of a Google Sheet that looks like this: https://docs.google.com/spreadsheets/d/1LbppGU5e4NbpnHn9vGRe0Z4QpatdCIg9Bygf3RQjas0/edit#gid=0

The sheet is referenced by its **title**. Ensure that the variable sheetTitle contains the name of a sheet accessible by the OAuth user.

Two columns, which correspond to variable names and values should be available in the sheet, and you can change the range in the code correspondingly.

When all setup, run:

    python rundmc.py
    
Or, ensure all the above dependencies are installed on a LAMP server, and call recompile.php?recompile=go via a browser.

