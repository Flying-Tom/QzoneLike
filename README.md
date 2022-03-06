# QzoneLike

基于Selenium实现的QQ空间点赞脚本(使用二维码登录)


## 使用

先安装`selenium`和`undetected_chromedriver`包

```
pip install selenium undetected_chromedriver
```

然后将脚本在后台挂机, 脚本会自动安装`chrome`
```
nohup python like.py > log/like.log 2>&1 &
```

二维码在`log`文件夹下中的`screenshot.png`中，扫码登录即可