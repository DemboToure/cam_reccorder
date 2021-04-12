# cam_reccorder

## Install virtual environnement 
```shell
pip install virtualenv
```

## Create virtual env 
```
virtualenv env
```
## Active virtual env 
```
(win) source env/Script/activate
(Linux) source env/bin/activate
```

## Update pip

```
pip install --upgrade pip
```

## install all libs
```
pip install -r requirements.txt
```

## lauch project

```
python -m processing.process
```

# Folder Structure

* Conf
    * conf.json, configuration file, not used yet
* env, Virtual environement contain all libraries
* logger 
    * log.py , used to log application event or whatever you want
* output, folder to save data
* processing
    * process.py, Application entry point
* source_data , used for all external data that well be used in a project 
* utils
    * utils.py, contains some specific functions
* video_utils
    * video_utils.py, necessary functions for record webCam 