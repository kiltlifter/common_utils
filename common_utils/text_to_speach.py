# -*- coding: utf-8 -*-
"""
Module Docstring
"""

from subprocess import Popen, PIPE
import requests
import os
from datetime import datetime
import base64

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"


class EspeakToMe:
    def __init__(self, espeak_path: str=None, word_gap: int=10, wpm: int=160, voice: str='en-us'):
        self.cmd_path = '/usr/bin/espeak' if not espeak_path else espeak_path
        self.word_gap = word_gap
        self.wpm = wpm
        self.voice = voice

    def talk(self, text: str=None):
        cmd = 'espeak -g {} -s {} -v {} \'{}\''.format(self.word_gap, self.wpm, self.voice, text)
        with Popen(cmd, shell=True, stdout=None, stderr=None) as s:
            pass

    def text_to_wav(self, text: str, output_dir: str=None, output_file: str=None):
        output = os.path.join(os.path.abspath(output_dir), output_file if output_file else 'espeak-audio-{}.mp3'.format(datetime.now().isoformat()))
        cmd = 'espeak -g {} -s {} -v {} -w {} \'{}\''.format(self.word_gap, self.wpm, self.voice, output, text)
        with Popen(cmd, shell=True, stdout=None, stderr=None) as s:
            pass



class GoogleTextToSpeach(requests.Session):
    def __init__(
            self, gaccess_token: str, lang_code: str='en-US', lang_name: str='en-US-Standard-C', lang_gender='FEMALE',
            audio_encoding='MP3'):
        super(GoogleTextToSpeach, self).__init__()
        self.gaccess_token = gaccess_token
        self.headers['Authorization'] = 'Bearer {}'.format(self.gaccess_token)
        self.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.base_url = 'https://texttospeech.googleapis.com'
        self.lang_code = lang_code
        self.lang_name = lang_name
        self.lang_gender = lang_gender
        self.audio_encoding = audio_encoding

    def _build_payload(self, text: str, output_dir: str='.', output_file: str=None):
        return {
            'input': {
                'text': text
            },
            'voice': {
                'languageCode': '{}'.format(self.lang_code),
                'name': '{}'.format(self.lang_name),
                'ssmlGender': '{}'.format(self.lang_gender)
            },
            'audioConfig': {
                'audioEncoding': '{}'.format(self.audio_encoding)
            }
        }, os.path.join(os.path.abspath(output_dir), output_file if output_file else 'synthesized_speach-{}.mp3'.format(datetime.now().isoformat()))

    def synthesize(self, text: str, output_dir: str=None, output_file: str=None):
        data, output_file = self._build_payload(text, output_dir, output_file)
        r = self.request(method='POST', url=self.base_url + '/v1beta1/text:synthesize', json=data)
        r.raise_for_status()
        return r.json(), output_file

    def text_to_mp3(self, text: str, output_dir: str=None, output_file: str=None):
        d, o = self.synthesize(text, output_dir, output_file)
        with open(o, 'wb') as f:
            b = base64.b64decode(d.get('audioContent'))
            f.write(b)

    def supported_voices(self):
        r = self.request(method='GET', url=self.base_url + '/v1beta1/voices')
        return r.json()

