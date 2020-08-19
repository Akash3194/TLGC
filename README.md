# TLGC
A script to get list of all forks of any github user and option to follow those forks. 

A Landin page where we can see all forks users of a gihtub rep and can follow them. It is very simple to use tool and which is build on python flask.
Make sure Python3 and virtualenv is installed on your sysytem.

* To install Virtualenv open your terminal or cmd and run the code below
 ``` pip install virtualenv ```

# [Steps to use it]
* Now git clone this project on your local system using
```git clone https://github.com/Akash3194/TLGC.git```

* Change your directory to projects directory using
``` cd TLGC ```

* Create a Virtual Environment in the folder and activate it, Code below is creating virtual env with tlgc name, you can choose any name
``` virtualenv tlgc```

* if you are on windows activate is by
 ``` .\tlgc\Scripts\activate ```
 
 * if you are on linux you can activate it by
 ``` source tlgc/bin/activate 
    or
    source tlgc/Scripts/activate
```

* now install python required libraries using
``` pip install -r requirements.txt ```

* run localhost server using
``` python main.py ```

[Your Server must be running now, you can check it on browser by typing [https://127.0.0.1:5000](https://127.0.0.1:5000) and hitting enter]
* A list of all fork users will be coming with a follow button
* Before following someone Make Sure to add your correct username and password in config.py file in the folder.
* you can also change repository or target user from the config,py file
