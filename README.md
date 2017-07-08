
[Pan](https://pt.wikipedia.org/wiki/Pandora)[load](https://en.wikipedia.org/wiki/Load_testing)

![Panload](http://i.imgur.com/oirUiHl.png "Panload")

Aplicação [Cli](https://en.wikipedia.org/wiki/Command-line_interface) em [Python 3](https://www.python.org/) que realiza o download de arquivos de diversas extensões, download de um vídeo + áudio e faz a união dos mesmos, além de realizar o download de vídeos do [Coub](http://coub.com/explore/hot).

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe23c85d12144fef9588b09bc082c434)](https://www.codacy.com/app/Sphinxs/Panload?utm_source=github.com&utm_medium=referral&utm_content=Sphinxs/Panload&utm_campaign=badger)


#### Dependências

As libs [os](https://docs.python.org/3.7/library/os.html) e [sys](https://docs.python.org/3.7/library/sys.html) por padrão vem no interpretador Python ( Built-in ), além destas libs são requeridas : ( Python 3 : `pip3 install ...` )

* [Json](https://docs.python.org/3.7/library/json.html)

* [Sub Process](https://docs.python.org/3.7/library/subprocess.html)

* [Requests](http://docs.python-requests.org/en/master/)

* [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)

Também é necessário instalar o [FFmpeg](https://ffmpeg.org/) caso você deseje concatenar um vídeo e um áudio, o mesmo tem um guia de instalação para Mac, Windows & Linux nesta página **[aqui](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)**.

> Player : [Vlc Player](http://www.videolan.org/)

#### Execução

A execução se da de forma simples, basta realizar o `git clone` deste repositório por Https ou Ssl, acessar o mesmo `cd Panload` e interpretar o arquivo `Panload.py`. Os arquivos baixados serão salvos no diretório atual em que o arquivo `Panload` se encontra, vale avisar que caso você tenha realizado o download de um áudio com nome ' x ' ou de um vídeo com nome ' y ' ( Ou ambos ) e realize a união de um vídeo + áudio com o mesmo nome e extensão dos arquivos já baixados a exclusão de ' x ' e ' y ' vai ser realizada. Para desativar a exclusão edite a linha `69` removendo o seguinte trecho de código : `&& rm -rf {0}.{1} {2}.{3}`. Também vale dizer que a implementação realizada aqui tem como intuito a prática de conhecimentos teóricos por parte do autor, caso você deseje realizar o download de vídeos ou até mesmo obter informações do Coub ou qualquer outro site adicionado futuramente nessa aplicação, procure a Api do mesmo pois ela fornece uma conexão simplificada para a obtenção de qualquer que seja o dado em questão.

#### Motivação

A principal motivação e uso desta aplicação se faz pelo site [Coub](http://coub.com/explore/hot) que tem uma grande falta de opções ( Que funcionem ) para realizar o download de vídeos ou áudios da plataforma, caso deseje realizar o download de um ' Coub ' acesse a página do vídeo em questão, copie sua [Uri](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) ( Url ) e logo após faça os paços de interpretação do arquivo `Panload` como já explicado acima.

![Coub Download](http://i.imgur.com/S9vDpox.png "Download And Save Coub Videos")

#### Issues

* Inferência na obtenção das urls de sites como [Sound Cloud](https://soundcloud.com/) & [Youtube](https://www.youtube.com/)

* Verificação de arquivos locais na concatenação

* Escolha de diretório

* Compressor

* Implementação de Gui

* Lista de arquivos disponíveis para download & união

#### Tratar

* Parâmetros errados

* Padronização do idioma ( Inglês )

* Segurança da call

* Chaves do dicionário ( Coub )
