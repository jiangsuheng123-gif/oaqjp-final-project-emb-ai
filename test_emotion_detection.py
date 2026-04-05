from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case 1: joy emotion
        text_to_analyse = "I am glad this happened"
        emotion_scores = emotion_detector(text_to_analyse)
        self.assertEqual(emotion_scores['dominant_emotion'], 'joy')
        # Test case 2: anger emotion
        text_to_analyse = "I am really mad about this"
        emotion_scores = emotion_detector(text_to_analyse)
        self.assertEqual(emotion_scores['dominant_emotion'], 'anger')
        # Test case 3: disgust emotion
        text_to_analyse = "I feel disgusted just hearing about this"
        emotion_scores = emotion_detector(text_to_analyse)
        self.assertEqual(emotion_scores['dominant_emotion'], 'disgust')
        # Test case 4: sadness emotion
        text_to_analyse = "I am so sad about this"
        emotion_scores = emotion_detector(text_to_analyse)
        self.assertEqual(emotion_scores['dominant_emotion'], 'sadness')
        # Test case 5: fear emotion
        text_to_analyse = "I am really afraid that this will happen"
        emotion_scores = emotion_detector(text_to_analyse)
        self.assertEqual(emotion_scores['dominant_emotion'], 'fear')

unittest.main()