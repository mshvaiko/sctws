# Screen to web-stream
###### This application captures the PC screen and streams into the web browser.

### How to setup
#### Clone repo:
>*git clone https://github.com/mshvaiko/sctws.git*

#### Move to dir:
>*cd sctws*

#### Create venv:
>*python3 -m venv env*

#### Active venv:
>*source ./env/bin/activate*

#### Install python libs:
>*pip install -r requirements.txt*

#### Change hardcoded ip-address to your own
>*app.run(host="\<your IP-address\>", debug=True)

#### Run script:
>*python app.py*

#### Open web browser and type URL
>*http://\<Your IP-address>:5000/*
>*Example: http://192.168.31.38:5000/*

##### Supported route path
>- *http://\<Your IP-address\>:5000/screen_0*
