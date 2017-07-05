
[Pan](https://pt.wikipedia.org/wiki/Pandora)[load](https://pt.wikipedia.org/wiki/Load)

![Panload](http://i.imgur.com/Ys0GJtw.png "Panload")

Aplicação [Cli](https://en.wikipedia.org/wiki/Command-line_interface) em [Python](https://www.python.org/) que realiza o download de arquivos de diversas extensões além de realizar o download de um vídeo e áudio e concatenar os mesmos. :milky_way:


#### Dependências

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe23c85d12144fef9588b09bc082c434)](https://www.codacy.com/app/Sphinxs/Panload?utm_source=github.com&utm_medium=referral&utm_content=Sphinxs/Panload&utm_campaign=badger)

As libs [os](https://docs.python.org/3.7/library/os.html) e [sys](https://docs.python.org/3.7/library/sys.html) por padrão vem no interpretador Python ( Built-in ), além destas duas libs são requeridas : ( Instalação com preferência em Python 3 ou seja `pip3 install ...` )

[Sub Process](https://docs.python.org/3.7/library/subprocess.html)

&

[Requests](http://docs.python-requests.org/en/master/)

Também é necessário instalar o [FFmpe](https://ffmpeg.org/) caso você deseje concatenar vídeo e áudio, o mesmo tem um guia de instalação para Mac, Windows & Linux nesta página **[aqui](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)**.

> Player : [Vlc Player](http://www.videolan.org/)

#### Execução

A execução se da de forma simples, basta realizar o `git clone` deste repositório, acessar o mesmo `cd Panload` e interpretar o arquivo `Panload.py` de preferência em `python3 Panload.py`. Os arquivos baixados serão salvos no diretório atual em que o arquivo `Panload.py` se encontra, vale avisar que caso você tenha realizado o download de um áudio com nome 'x' ou um vídeo com nome ' y ' ( Ou ambos ) e realize a e concatenação de um vídeo + áudio com o mesmo nome dos arquivos já baixados a exclusão de ' x ' e ' y ' vai ser realizada. Para desativar a exclusão edite a linha `68` removendo o seguinte trecho de código : `&& rm -rf {0}.{1} {2}.{3}`.

#### Motivação

A principal motivação e uso desta aplicação se faz presente pelo site [Coub](http://coub.com/explore/hot) que tem uma falta imensa de opções ( Que funcionem ) para realizar o download de vídeos / áudios da plataforma, então caso deseje realizar o download de um ' Coub ' acesse a página do mesmo e pressione `ctrl + u`, `ctrl + f` e digite **mp3** para encontrar o link do áudio ou **mp4** para encontrar o link do vídeo, então copie tal link e cole o mesmo na linha de comando desta aplicação ( *Panload* ). - Ps : O download de qualquer arquivo por parte dessa aplicação ( Até o momento ) necessita que a extensão de tal arquivo esteja implícita em sua [Uri](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) ( Url ) !

![Coub Download](http://i.imgur.com/JVvukrY.png "Download And Save Coub Videos")

#### Issues

* Inferência na obtenção das url's de sites como [Sound Cloud](https://soundcloud.com/), [Youtube](https://www.youtube.com/) & [Coub](http://coub.com/explore/hot)

* Verificação de arquivos locais na concatenação

* Escolha de diretório

* Compressor para os arquivos

* Implementação de Gui

#### Tratar

* Parâmetros errados

* Padronização do idioma ( Inglês )
