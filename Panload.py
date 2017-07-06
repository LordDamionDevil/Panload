
# -*- coding: utf-8 -*-

import os

import sys

import json

import requests

from subprocess import call

from bs4 import BeautifulSoup


def clear () :

    os.system ( 'clear || cls' )


class Archive ( object ) :

    def __init__ ( self ) :

        pass


    def download ( self, name = None, url = None, ext = None ) :

        if name == None or url == None or ext == None :

            clear ()

            print ( u'\nError Download - Parameters\n' )

            sys.exit ( 1 )

        self.__name = name

        self.__url = url if url.startswith ( 'https://' ) or url.startswith ( 'http://' ) else 'http://' + url

        self.__ext = ext if ext.startswith ( '.' ) else '.' + ext

        # -

        requ = requests.get ( self.__url )

        with open ( self.__name + self.__ext, 'wb' ) as arch :

            for chunk in requ.iter_content ( chunk_size = 255 ) :

                if chunk :
                    arch.write ( chunk )

        print ( '\n\nDone - {0}\n'.format ( str ( name ) ) )


    def combine ( self, vname, vurl, vext, aname, aurl, aext, fname, fext ) :

        print ( '\nLoading ...' )

        self.download ( vname, vurl, vext )

        self.download ( aname, aurl, aext )

        # self.__comand = 'ffmpeg -i {0}.{1} -i {2}.{3} -vcodec copy -acodec copy {4}.{5} && rm -rf {0}.{1} {2}.{3}'.format ( vname, vext, aname, aext, fname, fext )

        self.__comand = 'ffmpeg -i {0}.{1} -i {2}.{3} -c:v copy -c:a aac -map 0:0 -map 1:0 -shortest {4}.{5} && rm -rf {0}.{1} {2}.{3}'.format ( vname, vext, aname, aext, fname, fext )

        call ( self.__comand, shell = True )

        clear ()

        print ( '\n\nDone - {0}\n'.format ( fname ) )


    def coub ( self, url = None, fname = None, fext = None ) :

        self.__cname = fname

        self.__cext = fext

        self.__curl = url if url.startswith ( 'https://' ) or url.startswith ( 'http://') else 'http://' + url

        # -

        self.__cb = requests.get ( self.__curl ).text

        self.__sp = BeautifulSoup ( self.__cb, 'html.parser' )

        self.__sp = str ( self.__sp.find ( id = 'coubPageCoubJson' ) ) [47:-9]

        self.__sp = json.loads ( self.__sp )

        # -

        self.__mp4 = str ( self.__sp['file_versions']['html5']['video']['high']['url'] )

        self.__mp3 = str ( self.__sp['file_versions']['html5']['audio']['high']['url'] )

        self.combine ( 'Vd', self.__mp4, 'mp4', 'Ad', self.__mp3, 'mp3', self.__cname, self.__cext )


Panload = Archive ()


while True :

    clear ();

    print ( '\nMenu :\n\n\t1 - Download\n\n\t2 - Concatenação\n\n\t3 - Download Coub\n')

    choose = 0

    try :

        choose = int ( input ( 'Sua escolha : ' ) )

    except Exception as Error :

        raise Exception ( '{0} - Try Again'.format ( Error ) )


    if choose == 1 :

        clear ();

        print ( '\nDownload :')

        dnome = input ( '\n\tNome para o arquivo : ' )

        durl = input ( '\n\tUrl do arquivo : ' )

        dext = input ( '\n\tExtensão do arquivo : ')

        Panload.download ( dnome, durl, dext )

    elif choose == 2 :

        clear ();

        print ( '\nConcatenação : ' )

        vnome = input ( u'\n\tNome para o vídeo : ' )

        vurl = input ( u'\n\tUrl do vídeo : ' )

        vext = input ( u'\n\tExtensão do vídeo : ' )

        clear ();

        print ( '\nConcatenação : ' )

        aname  = input ( u'\n\n\tNome para o áudio : ' )

        aurl = input ( u'\n\tUrl do áudio : ' )

        aext = input ( u'\n\tExtensão áudio : ' )

        clear ();

        print ( '\nConcatenação : ' )

        fname = input ( u'\n\n\tNome para o arquivo convertido : ' )

        fext = input ( u'\n\tExtensão para o arquivo convertido : ' )

        clear ()

        Panload.combine ( vnome, vurl, vext, aname, aurl, aext, fname, fext )

    elif choose == 3 :

        clear ()

        print ( '\nDownload Coub : ' )

        url = input ( '\n\n\tInforme a url : ' )

        cnm = input ( '\n\tNome para o arquivo : ' )

        cex = input ( '\n\tExtensão do arquivo : ' )

        Panload.coub ( url, cnm, cex )

    else :

        print ( '\nOpção invalida' )

    out = input ( '\n0 Para sair ou outro digito para continuar : ' )

    if ( out == '0' ) :

        clear ()

        sys.exit ( 0 )
