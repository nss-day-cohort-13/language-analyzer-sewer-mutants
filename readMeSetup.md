Alt-H1 SETUP

Click the link below and fork the repo, make sure you are signed into GitHub. If you do not have an account you will need to create one.

‘’'<https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants>```


Go into your terminal and clone down the forked repo into your destination folder of choice.

git clone https://github.com/nss-day-cohort-13/language-analyzer-sewer-mutants.git
In your terminal run the commands listed below:

Check to see if Python is installed 

```which python```
Check which version is installed. Most likely it will be version 2.7.x.

```python -version```
Once have confirmed that Python is installed and your machine is running the latest version, you will then need to install NLTK(Natural Language Toolkit).
``` Pip install nltk ```

If your machine is NOT running the latest version of python, please refer to the Installing Python section below.
Installing Python:

Windows Users:

Windows does not come with Python installed. You need to visit the Python downloads site and grab version 3.3.6 and install it. It will get installed to the C:\Python33 directory.

After it is installed, you must add C:\Python to your system path. Here's how.

Press your Windows key.
Start typing Control.
The search results should have the Windows Control Panel as the first result. Press enter.
When the control panel screen appears, start typing in environment in the search bar in the upper right corner.
Select the option to change environment variables. If you are presented with two options, choosing either one is fine.
When the screen appears, click the button at the bottom for environment variables.
Next, click on the PATH variable and choose to edit it.
Go to the end of the string, and enter a semi-colon, and the new path entry. ;C:\Python33

 Osx/Pyenv:

OSX users, you should have Homebrew installed at this point. If you don't, do it now. Then run these commands in order.

```brew install pyenv
pyenv install 3.3.6
```
After Pyenv is installed, you can make version 3.3.6 the new, globally accepted version by typing the following.

```pyenv global 3.3.6```
Now, when you check the version of Python with the command below, it should return 3.3.6.

```python —version```

NLTK:

Once you have confirmed that Python is installed and your machine is running the latest version, you will then need to install NLTK(Natural Language Toolkit).

``` Pip install nltk ```

