#FaceUnlock

This program shows how to unlock something with your face.

You may want to read the tutorial [here](http://www.jianshu.com/p/3e3b295e0e98):)

It need opencv2, requests installed, and add config in `Lib/facepp.json` to run.

You can get the api_key and api_secret through register and create a application in [face++](http://www.faceplusplus.com.cn/).
```python
# You should set your account first
python SetAccount.py

# Then you can check login
python Login.py
```

You need to set your face samples once before use it to unlock.
