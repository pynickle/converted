from subprocess import Popen
Popen("wget https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-linux.tar.gz").wait()
Popen("tar -xzvf pandoc-2.7.3-linux.tar.gz").wait()
Popen("cd pandoc-2.7.3-linux.tar.gz").wait()
Popen("./configure").wait()
Popen("make").wait()
Popen("make install").wait()