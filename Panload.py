
# -*- coding: utf-8 -*-

import os

import sys

import requests

from subprocess import call


def clear () :

    '''

        Stackoverflow.com/questions/16242025/term-environment-variable-not-set

        call ( 'clear', shell = True )

    '''

    os.system ( 'clear' )


class Archive ( object ) :

    def __init__ ( self ) :

        pass


    def download ( self, name = None, url = None, ext = None ) :

        if name == None or url == None or ext == None :

            clear ()

            print ( '\nError - Parameters\n' )

            sys.exit ( 1 )

        self.name = name

        self.url = url if url.startswith ( 'https://' ) or url.startswith ( 'http://') else 'http://' + url

        self.ext = ext if ext.startswith ( '.' ) else '.' + ext

        requ = requests.get ( self.url )

        with open ( self.name + self.ext, 'wb' ) as arch :

            for chunk in requ.iter_content ( chunk_size = 255 ) :

                if chunk :
                    arch.write ( chunk )

        print ( '\n\nDownload done - {0}\n'.format (name) )


    def combine ( self, vname, vurl, vext, aname, aurl, aext, fname, fext ) :

        print ( '\nBaixando ...' )

        self.download ( vname, vurl, vext )

        self.download ( aname, aurl, aext )

        # comand = 'ffmpeg -i {0}.{1} -i {2}.{3} -vcodec copy -acodec copy {4}.{5} && rm -rf {0}.{1} {2}.{3}'.format ( vname, vext, aname, aext, fname, fext )

        comand = 'ffmpeg -i {0}.{1} -i {2}.{3} -c:v copy -c:a aac -map 0:0 -map 1:0 -shortest {4}.{5} && rm -rf {0}.{1} {2}.{3}'.format ( vname, vext, aname, aext, fname, fext )

        call ( comand, shell = True )

        clear ()

        print ( '\n\nDownload done - {0}\n'.format (fname) )


Panload = Archive ()


while True :

    clear (); print ( '\nMenu :\n\n\t1 - Download\n\n\t2 - Concatenação\n')

    choose = 0

    try :

        choose = int ( input ( 'Informe sua escolha : ' ) )

    except Exception as Error :

        raise Exception ( '{0} - Try Again'.format ( Error ) )


    if choose == 1 :

        clear (); print ( '\nDownload :')

        dnome = input ( '\n\tInforme um nome para o arquivo : ' )

        durl = input ( '\n\tInforme a url do arquivo : ' )

        dext = input ( '\n\tInforme a extensão do arquivo : ')


        Panload.download ( dnome, durl, dext )

    elif choose == 2 :

        clear (); print ( '\nConcatenação :')

        vnome = input ( u'\n\tInforme um nome para o vídeo : ' )

        vurl = input ( u'\n\tInforme a url do vídeo : ' )

        vext = input ( u'\n\tInforme a extensão do vídeo : ' )

        clear (); print ( '\nConcatenação :')

        aname  = input ( u'\n\n\tInforme um nome para o áudio : ' )

        aurl = input ( u'\n\tInforme a url do áudio : ' )

        aext = input ( u'\n\tInforme a extensão áudio : ' )

        clear (); print ( '\nConcatenação :')

        fname = input ( u'\n\n\tInforme o nome do arquivo final : ' )

        fext = input ( u'\n\tInforme a extensão do arquivo final : ' )

        clear ()

        Panload.combine ( vnome, vurl, vext, aname, aurl, aext, fname, fext )

    else :

        print ( '\nOpção invalida' )


    out = input ( '\nDigite 0 para sair ou outro digito para continuar : ' )

    if ( out == '0' ) :

        clear ()

        sys.exit (0)
