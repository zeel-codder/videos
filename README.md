# Video fetcher

It is recommended to start developing in a virtualenv so that the system dependencies are not leaked into the source code of the project.

Step 1: Install the virtualenv package by runninng 
```bash
pip3 install virtualenv
```
Step 2: Create the virtualenv by runninng 
```bash
virtualenv -p python3 videos_venv
```
Step 3: Activate the virtualenv by runninng 
```bash
source videos_venv/bin/activate
```

Step 4: Deactivate the virtualenv by simply runninng 
```
deactivate
```

Step 5: Keep updating the requirements.txt if any new packages are installed by running 
```bash
pip freeze > requirements.txt
```

To resume development post new pulls, always run **pip install -r /path/to/requirements.txt** to install the latest requirements.