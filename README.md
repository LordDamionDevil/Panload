
[Panload]

![Panload](http://i.imgur.com/oirUiHl.png "Panload")

Aplicação Cli em Python 3 que realiza o download de vídeos do [Coub](http://coub.com/explore/hot).

#### Dependências

* [Os](https://docs.python.org/3.7/library/os.html)

* [Inspect](https://docs.python.org/3.7/library/inspect.html)

* [Requests](http://docs.python-requests.org/en/master/)

* [Sub Process](https://docs.python.org/3.7/library/subprocess.html)

* [Time](https://docs.python.org/3.7/library/time.html)


Também é recomendado instalar o [FFmpeg](https://ffmpeg.org/) caso você deseje concatenar um vídeo a um áudio, o mesmo tem um guia de instalação para Mac, Windows & Linux nesta página **[aqui](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)**.

> Player : [Vlc Player](http://www.videolan.org/)

#### Execução

> pip install requests subprocess & apt install mencoder

`python3 Panload.py` - [Coub](http://coub.com/view/wpst2)

#### Feature

Criar sessão para baixar os coub's de terceiros, além fazer o download dos vídeos de forma direta

Merge do vídeo / gif e audio no time correto

Tokenizar o comando do subprocess
