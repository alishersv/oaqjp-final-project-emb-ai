import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector1(self):
        prediction = emotion_detector('I am glad this happened')
        self.assertEqual(prediction['dominant_emotion'],'joy')
    def test_emotion_detector2(self):
        prediction = emotion_detector('I am really mad about this')
        self.assertEqual(prediction['dominant_emotion'],'anger')
    def test_emotion_detector3(self):
        prediction = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(prediction['dominant_emotion'],'disgust')
    def test_emotion_detector4(self):
        prediction = emotion_detector('I am so sad about this')
        self.assertEqual(prediction['dominant_emotion'],'sadness')
    def test_emotion_detector5(self):
        prediction = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(prediction['dominant_emotion'],'fear')
    
unittest.main()