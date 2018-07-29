import os
os.popen("python pig.py")
os.popen("python music.py")
pyinstaller -F -w pig+.py -p pig.py -p music.py --hidden--import print --hidden--import music

pyinstaller -makespec  music.py

pyinstaller -F -w pig+.py  pig.py  music.py --noconsole

pyinstaller options..music.py

datas = [(r'D:/python workspace/venv', 'MARTY - Rainbow Song.mp3')]

pyinstaller [music] music.spec

pyinstaller -F -w pig+.py  pig.py  music.spec --noconsole

a.datas += Tree(r'D:/python workspace/venv/1.mp3', prefix='')

datas= [ (r'music/1.mp3', r'D:/python workspace/venv/dist/1.mp3','DATA' ) ],