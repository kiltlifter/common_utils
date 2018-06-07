import unittest
from common_utils import EspeakToMe, GoogleTextToSpeach


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.speak = EspeakToMe(wpm=180, voice='en-us')
        self.g_speak = GoogleTextToSpeach(
            gaccess_token='',
        )
        self.sample_text = """
        The State Department is evacuating several Americans from China amid health concerns about mysterious symptoms arising after unusual noises detected by U.S. diplomats and their families working in the consulate in Guangzhou.

After initial screenings by a medical team dispatched last month when the first incident was reported, the State Department has sent “a number” of ­affected people to the United States for further evaluation, State Department spokeswoman Heather Nauert said.
        """

    def test_00_basic_speak(self):
        text = 'Hello, my name is Sean.'
        self.speak.talk(text)

    def test_01_google_supported_voices(self):
        import json
        d = self.g_speak.supported_voices()
        with open('../files/supported_voices.json', 'w') as f:
            f.write(json.dumps(d, indent=4, sort_keys=True))

    def test_02_google_speach(self):
        self.g_speak.lang_code = 'en-GB'
        self.g_speak.lang_gender = 'FEMALE'
        self.g_speak.lang_name = 'en-GB-Standard-A'
        self.g_speak.text_to_mp3(self.sample_text, output_dir='../files', output_file='sample-{}.mp3'.format(self.g_speak.lang_name))


if __name__ == '__main__':
    unittest.main()
