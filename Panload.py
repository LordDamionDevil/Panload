
# -*- encoding: utf-8 -*-


import os, inspect

from requests import get

from subprocess import call, Popen # Mono & Multi

from time import sleep


def screen(): return os.system('clear')


class Coub:

    def __init__(self, url: str) -> None:

        self.__url = url

        self.__id = self.__url[21:] if self.__url.startswith(
            'http://') else self.__url[14:]

        self.__arch = get('http://coub.com/api/v2/coubs/' + self.__id).json()

        self.__data = [self.__arch['title'], self.__arch['audio_file_url']]

        if self.__arch['media_blocks']['external_raw_videos']:

            self.__data.append(
                self.__arch['media_blocks']['external_raw_videos'])

        else:

            screen()

            print('\n{0}Error{1} - It\'s not possible to download this coub\n'.format('\033[31m', '\033[37m'))

            exit(1)

        self.cb()

    def download(self, name: str, url: str, extension: str) -> None:

        self.__name=name

        self.__url=url if url.startswith('http://') else 'http://' + url

        self.__extension=extension if extension.startswith(
            '.') else '.' + extension

        with open(self.__name + self.__extension, 'wb') as archive:

            for chunk in get(self.__url).iter_content(chunk_size = 255):

                if chunk:
                    archive.write(chunk)

    def cb(self) -> None:

        self.download('Audio', self.__data[1], 'mp3')

        for item in self.__data[2]:

            self.download('Gif' + str(item['id']), item['url'], 'gif')

        # ffmpeg -i Video.mp4 -i Audio.mp3 -c:v copy -c:a aac -map 0:0 -map 1:0 -shortest Coub.mp4'

        sleep(5)

        call(['convert {1}/Gif* {1}/Video.mp4 && mencoder {1}/Video.mp4 -audiofile {1}/Audio.mp3 -oac copy -ovc copy -o {0}.mp4'.format(self.__data[0], os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))], shell = True)

        sleep(5)

        Popen(['rm -rf Gif* Video.mp4 Audio.mp3'], shell=True)

        screen()

        print('\n{0}Finished{1}\n'.format('\033[32m', '\033[37m'))


if __name__ == '__main__':

    screen()

    user = ''

    while True:

        user=input('\nPlease enter with a {0}coub{1} url : '.format(
            '\033[34m', '\033[37m'))

        if user.startswith('http://coub.com/view/') or user.startswith('coub.com/view/'):

            break

        else:

            screen()

            print('\n{0}Invalid{1} url {0}!{1}'.format('\033[31m','\033[37m'))

    print('\n{0}Connecting{1} ...\n'.format('\033[33m','\033[37m'))

    Coub(user)
