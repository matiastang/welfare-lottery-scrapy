<!--
 * @Author: matiastang
 * @Date: 2022-08-09 15:14:58
 * @LastEditors: matiastang
 * @LastEditTime: 2023-03-02 01:02:00
 * @FilePath: /welfare-lottery-scrapy/README.md
 * @Description: README
-->
# welfare-lottery-scrapy

测试

## 安装Scrapy

直接使用`pip3`安装`Scrapy`：
```
$ pip3 install Scrapy -i https://pypi.douban.com/simple
```
然后，使用`scrapy startproject welfareLottery`创建新项目时，可能就会报下面错误：
```
$ scrapy startproject welfareLottery 
Traceback (most recent call last):
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/bin/scrapy", line 5, in <module>
    from scrapy.cmdline import execute
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/scrapy/__init__.py", line 12, in <module>
    from scrapy.spiders import Spider
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/scrapy/spiders/__init__.py", line 10, in <module>
    from scrapy.http import Request
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/scrapy/http/__init__.py", line 11, in <module>
    from scrapy.http.request.form import FormRequest
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/scrapy/http/request/form.py", line 11, in <module>
    from lxml.html import FormElement, HtmlElement, HTMLParser, SelectElement
  File "/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/lxml/html/__init__.py", line 53, in <module>
    from .. import etree
ImportError: dlopen(/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/lxml/etree.cpython-310-darwin.so, 0x0002): tried: '/Users/matias/.gvm/pkgsets/go1.17.1/global/overlay/lib/etree.cpython-310-darwin.so' (no such file), '/etree.cpython-310-darwin.so' (no such file), '/Users/matias/.local/share/virtualenvs/welfare-lottery-scrapy-Qkb1Kj8J/lib/python3.10/site-packages/lxml/etree.cpython-310-darwin.so' (mach-o file, but is an incompatible architecture (have (x86_64), need (arm64e)))
```
这是因为我们直接使用`pip install`安装的`scrapy`依赖`lxml`包不是`arm64e`版本的，那怎么办呢？其实，很简单，我们使用`conda install`安装`lxml`就搞定了：
```
$ conda install -c conda-forge lxml
```
安装完毕就可以正常使用了。
如果上述方法还是不行则使用下面的方法更新`lxml`
```
pip3 uninstall lxml  
Found existing installation: lxml 4.9.1
Uninstalling lxml-4.9.1:
  Would remove:
    /Users/matias/.pyenv/versions/3.10.5/lib/python3.10/site-packages/lxml-4.9.1-py3.10.egg-info
    /Users/matias/.pyenv/versions/3.10.5/lib/python3.10/site-packages/lxml/*
Proceed (Y/n)? y
  Successfully uninstalled lxml-4.9.1
(mt_scrapy)  ~/matias/MT/MTGithub/scrapy/welfare-lottery-scrapy   main ±  arch -arm64e pip3 install lxml -i https://pypi.douban.com/simple
Looking in indexes: https://pypi.douban.com/simple
Collecting lxml
  Downloading https://pypi.doubanio.com/packages/70/bb/7a2c7b4f8f434aa1ee801704bf08f1e53d7b5feba3d5313ab17003477808/lxml-4.9.1.tar.gz (3.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 11.1 MB/s eta 0:00:00
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for lxml, since package 'wheel' is not installed.
Installing collected packages: lxml
  Running setup.py install for lxml ... done
Successfully installed lxml-4.9.1
WARNING: You are using pip version 22.0.4; however, version 22.2.2 is available.
You should consider upgrading via the '/Users/matias/.pyenv/versions/3.10.5/bin/python3.10 -m pip install --upgrade pip' command.
(mt_scrapy)  ~/matias/MT/MTGithub/scrapy/welfare-lottery-scrapy   main ±  scrapy --help
Scrapy 2.6.2 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  commands      
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command
```
