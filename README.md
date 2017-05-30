# Default Flask App
The New York Daily News' starter [flask](http://flask.pocoo.org/) app. Comes with flask plus tools for turning your flask app into flatfiles. Based on [The Denver Post's Bill Tracker flask app](https://github.com/denverpost/bill-tracker), which was based on [the Denver Crimes flask app](http://crime.denverpost.com/about/). 

## Usage

1. Check out the code,
2. Open up terminal, 
3. Create a virtualenv for your project (`pip install virtualenv` from anywhere in your terminal should work. [More here](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/))
    1. To get set up with virtual environments (Mac and *nix):
        1. `pip install virtualenv`
        2. `pip install virtualenvwrapper`
        3. `export WORKON_HOME=~/Envs`
        4. `source /usr/local/bin/virtualenvwrapper.sh`
        5. `cd path/to/your/repo`
        6. `mkvirtualenv REPONAME`
        7. Now back to the rest of the usage instructions below...
4. `pip install -r requirements.txt` from your terminal
5. `python runserver.py` gets you a webserver running on port 5000.
6. [http://localhost:5000](http://localhost:5000)

# License

The MIT License (MIT)

Copyright © 2017 New York Daily News

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
