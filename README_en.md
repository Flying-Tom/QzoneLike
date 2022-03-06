# QzoneLike

A script to automatically click "like" at Qzone implemented on the basis of Selenium.

Supported login method: QRcode.


## Usage

First execute the following command to install `selenium` and `undetected_chromedriver` package.

```
pip install selenium undetected_chromedriver
```

Then you can hang the script on the background, the program will install `chrome` a few moments later.

```
nohup python like.py > log/like.log 2>&1 &
```

Scan the QRcode `screenshot.pnt` in directory `log/` to log in.