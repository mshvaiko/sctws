# Screen to web-stream
###### This application captures the PC screen and streams into the web browser.

### How to setup
#### Clone repo:
>*git clone https://github.com/mshvaiko/sctws.git*

#### Move to dir:
>*cd screen_web_streamer*

#### Create venv:
>*python3 -m venv env*

#### Active venv:
>*source ./env/bin/activate*

#### Install python libs:
>*pip install -r requirements.txt*

#### Change hardcoded ip-address to your own
>*app.run(host="<your IP-address>", debug=True)

#### Run script:
>*python app.py*

#### Open web browser and type URL
>*http://<Your IP-address>:5000/*

##### Supported route path
>- */screen_0*