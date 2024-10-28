from EmotionDetection.emotion_detection import emotion_detector

import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):    
        # Test case for Dominant Emotion = joy
        result_1 = emotion_detector('I am glad this happened')
        dominant_key = ''
        dominant_val = max(result_1.values())
        for k,v in result_1.items():
            if v == dominant_val:
                dominant_key = k
        self.assertEqual(dominant_key, 'joy')
        
        # Test case for dominant emotion = anger
        result_2 = emotion_detector('I am really mad about this')
        dominant_key = ''
        dominant_val = max(result_2.values())
        for k,v in result_2.items():
            if v == dominant_val:
                dominant_key = k
        self.assertEqual(dominant_key, 'anger')
        
        # Test case for dominant emotion = disgust
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        dominant_key = ''
        dominant_val = max(result_3.values())
        for k,v in result_3.items():
            if v == dominant_val:
                dominant_key = k
        self.assertEqual(dominant_key, 'disgust')

        # Test case for dominant emotion = sadness
        result_4 = emotion_detector('I am so sad about this')
        dominant_key = ''
        dominant_val = max(result_4.values())
        for k,v in result_4.items():
            if v == dominant_val:
                dominant_key = k
        self.assertEqual(dominant_key, 'sadness')

        # Test case for dominant emotion = fear
        result_5 = emotion_detector('I am really afraid that this will happen')
        dominant_key = ''
        dominant_val = max(result_5.values())
        for k,v in result_5.items():
            if v == dominant_val:
                dominant_key = k
        self.assertEqual(dominant_key, 'fear')
    
unittest.main()