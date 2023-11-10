<!--
 * @Author: matiastang
 * @Date: 2022-08-09 15:14:58
 * @LastEditors: matiastang
 * @LastEditTime: 2023-11-10 12:33:46
 * @FilePath: /welfare-lottery-scrapy/README.md
 * @Description: README
-->
# welfare-lottery-scrapy

测试

## 安装Scrapy

* 安装`Scrapy`：
```sh
$ pip3 install Scrapy -i https://pypi.douban.com/simple
```
* 安装`pymysql`、`apscheduler`
```sh
$ pip3 install pymysql -i https://pypi.douban.com/simple
```

然后，使用`scrapy startproject welfareLottery`创建新项目时，可能就会报下面错误：
```sh
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
```sh
$ conda install -c conda-forge lxml
```
安装完毕就可以正常使用了。
如果上述方法还是不行则使用下面的方法更新`lxml`
```sh
$ pip3 uninstall lxml  
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

scrapy crawl welfare_last -a count=1
Traceback (most recent call last):
  File "/usr/local/bin/scrapy", line 5, in <module>
    from scrapy.cmdline import execute
  File "/usr/local/lib/python3.10/dist-packages/scrapy/__init__.py", line 15, in <module>
    from scrapy.spiders import Spider
  File "/usr/local/lib/python3.10/dist-packages/scrapy/spiders/__init__.py", line 106, in <module>
    from scrapy.spiders.crawl import CrawlSpider, Rule
  File "/usr/local/lib/python3.10/dist-packages/scrapy/spiders/crawl.py", line 15, in <module>
    from scrapy.utils.spider import iterate_spider_output
  File "/usr/local/lib/python3.10/dist-packages/scrapy/utils/spider.py", line 24, in <module>
    from scrapy.utils.defer import deferred_from_coro
  File "/usr/local/lib/python3.10/dist-packages/scrapy/utils/defer.py", line 37, in <module>
    from scrapy.utils.reactor import _get_asyncio_event_loop, is_asyncio_reactor_installed
  File "/usr/local/lib/python3.10/dist-packages/scrapy/utils/reactor.py", line 8, in <module>
    from twisted.internet import asyncioreactor, error
  File "/usr/lib/python3/dist-packages/twisted/internet/asyncioreactor.py", line 19, in <module>
    from twisted.internet.posixbase import (
  File "/usr/lib/python3/dist-packages/twisted/internet/posixbase.py", line 19, in <module>
    from twisted.internet import error, tcp, udp
  File "/usr/lib/python3/dist-packages/twisted/internet/tcp.py", line 37, in <module>
    from twisted.internet._newtls import (
  File "/usr/lib/python3/dist-packages/twisted/internet/_newtls.py", line 18, in <module>
    from twisted.protocols.tls import TLSMemoryBIOFactory, TLSMemoryBIOProtocol
  File "/usr/lib/python3/dist-packages/twisted/protocols/tls.py", line 50, in <module>
    Connection(Context(TLSv1_METHOD), None)
  File "/usr/lib/python3/dist-packages/OpenSSL/SSL.py", line 674, in __init__
    res = _lib.SSL_CTX_set_ecdh_auto(context, 1)
AttributeError: module 'lib' has no attribute 'SSL_CTX_set_ecdh_auto'

pip3 uninstall pyopenssl
Found existing installation: pyOpenSSL 21.0.0
Not uninstalling pyopenssl at /usr/lib/python3/dist-packages, outside environment /usr
Can't uninstall 'pyOpenSSL'. No files were found to uninstall.
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

pip3 uninstall pyopenssl --break-system-packages

Usage:
  pip3 uninstall [options] <package> ...
  pip3 uninstall [options] -r <requirements file> ...

no such option: --break-system-packages

删除/usr/lib/python3/dist-packages/下面的pyOpenSSL-21.0.0.egg-info/文件夹

安装`pyopenssl`
```sh
pip3 install pyopenssl
Looking in indexes: http://mirrors.cloud.aliyuncs.com/pypi/simple/
DEPRECATION: The HTML index page being used (http://mirrors.cloud.aliyuncs.com/pypi/simple/pyopenssl/) is not a proper HTML 5 document. This is in violation of PEP 503 which requires these pages to be well-formed HTML 5 documents. Please reach out to the owners of this index page, and ask them to update this index page to a valid HTML 5 document. pip 22.2 will enforce this behaviour change. Discussion can be found at https://github.com/pypa/pip/issues/10825
Collecting pyopenssl
  Downloading http://mirrors.cloud.aliyuncs.com/pypi/packages/db/de/007b832ad7a95e6a73745609bbe123c407aa2c46bb0b8f765c8718294e7f/pyOpenSSL-23.3.0-py3-none-any.whl (58 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.8/58.8 KB 14.2 MB/s eta 0:00:00
DEPRECATION: The HTML index page being used (http://mirrors.cloud.aliyuncs.com/pypi/simple/cryptography/) is not a proper HTML 5 document. This is in violation of PEP 503 which requires these pages to be well-formed HTML 5 documents. Please reach out to the owners of this index page, and ask them to update this index page to a valid HTML 5 document. pip 22.2 will enforce this behaviour change. Discussion can be found at https://github.com/pypa/pip/issues/10825
Collecting cryptography<42,>=41.0.5
  Using cached http://mirrors.cloud.aliyuncs.com/pypi/packages/85/62/48bcebd955945d8da3fe9b84a679dbf4bf179e1ac36e583b7eaa47506758/cryptography-41.0.5-cp37-abi3-manylinux_2_28_x86_64.whl (4.4 MB)
Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.10/dist-packages (from cryptography<42,>=41.0.5->pyopenssl) (1.16.0)
Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.12->cryptography<42,>=41.0.5->pyopenssl) (2.21)
Installing collected packages: cryptography, pyopenssl
  Attempting uninstall: cryptography
    Found existing installation: cryptography 38.0.4
    Uninstalling cryptography-38.0.4:
      Successfully uninstalled cryptography-38.0.4
Successfully installed cryptography-41.0.5 pyopenssl-23.3.0
```

运行，差什么包，安装什么包。
ModuleNotFoundError: No module named 'pymysql'