
# coding: utf-8

import os

import requests

import subprocess

from json import loads

from bs4 import BeautifulSoup


colours = { 'red': '\033[31m', 'blue': '\033[34m', 'blank': '\033[37m' }


def info () :

    info_n = input ( '\n\n\tNome do arquivo : ' )

    info_e = input ( '\n\tExtensão do arquivo : ' )

    info_u = input ( '\n\tUrl : ' )

    return [ info_n, info_u, info_e ]


def clear () :

    os.system ( 'cls' if os.name == 'nt' else 'clear' )


class Archive :

    def download ( self, name = None, url = None, ext = None ) :

        self.__name = name

        self.__url = url if url.startswith ( 'https://' ) or url.startswith ( 'http://' ) else 'http://' + url

        self.__ext = ext if ext.startswith ( '.' ) else '.' + ext

        request = requests.get ( self.__url )

        with open ( self.__name + self.__ext, 'wb' ) as archive :

            for chunk in request.iter_content ( chunk_size = 255 ) :

                if chunk :
                    archive.write ( chunk )

        print ( '\n\n\t{1}Done{2} - {0}\n'.format ( name, colours['red'], colours['blank'] ) )

    def combine ( self, vn, vu, ve, an, au, ae, fn, fe ) :

        print ( '\nLoading {0}...{1}\n'.format ( colours['blue'], colours['blank'] ) )

        self.download ( vn, vu, ve )

        self.download ( an, au, ae )

        self.__comand = 'ffmpeg -i {0}.{1} -i {2}.{3} -c:v copy -c:a aac -map 0:0 -map 1:0 -shortest {4}.{5}'.format ( vn, ve, an, ae, fn, fe )

        subprocess.Popen ( self.__comand.split (' '), shell = False )

        print ( '\n\nFile :\n\n\t{1}Done{2} - {0}\n'.format ( fn, colours['red'], colours['blank'] ) )

    def coub ( self, cn = None, cu = None, ce = None ) :

        self.__cname = cn

        self.__curl = cu if cu.startswith ( 'https://' ) or cu.startswith ( 'http://' ) else 'http://' + cu

        self.__cext = ce

        # -

        self.__coub = requests.get ( self.__curl ).text

        self.__soup = BeautifulSoup ( self.__coub, 'html.parser' )
        
        self.__soup = str ( self.__soup.find ( id = 'coubPageCoubJson' ) ) [47:-9]

        self.__soup = loads ( self.__soup )

        # -

        self.__mp4 = str ( self.__soup['file_versions']['html5']['video']['med']['url'][2:] )

        self.__mp3 = str ( self.__soup['file_versions']['html5']['audio']['med']['url'] )

        self.combine ( 'Video', self.__mp4, 'mp4', 'Audio', self.__mp3, 'mp3', self.__cname, self.__cext )


Panload = Archive ()


choose = '0'

off = [ '00000000', '0', 'Zero', 'zero' ]

if __name__ == '__main__' :

    while True :

        clear ();

        print ( '\nMenu :\n\n\t1 - Download\n\n\t2 - Concatenação\n\n\t3 - Download Coub\n' )

        choose = input ( 'Escolha : ' )

        if choose in off :

            clear ()

            exit ( 0 )

        elif choose == '1' :

            clear ();

            print ( '\nDown :')

            bank = info ()

            Panload.download ( * bank )

        elif choose == '2' :

            clear ();

            print ( '\nUnião : ' )

            vn = input ( '\n\n\tNome para o vídeo : ' )

            vu = input ( '\n\n\tUrl : ' )

            ve = input ( '\n\n\tExtensão do vídeo : ' )

            clear ();

            print ( '\nUnião : ' )

            an  = input ( '\n\n\tNome para o áudio : ' )

            au = input ( '\n\n\tUrl : ' )

            ae = input ( '\n\n\tExtensão áudio : ' )

            clear ();

            print ( '\nUnião : ' )

            fn = input ( '\n\n\tNome para o arquivo convertido : ' )

            fe = input ( '\n\n\tExtensão para o arquivo convertido : ' )

            clear ()

            Panload.combine ( vn, vu, ve, an, au, ae, fn, fe )

        elif choose == '3' :

            clear ()

            print ( '\nCoub : ' )

            bank_coub = info ()

            Panload.coub ( * bank_coub )

        else :

            print ( '\nOpção invalida' )

        out = input ( '\nZero para sair, outro digito para continuar : ' )

        if out in off :

            clear ()

            exit ( 0 )
