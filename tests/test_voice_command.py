```python
import unittest
from src.voice_command import activateVoiceCommand

class TestVoiceCommand(unittest.TestCase):

    def setUp(self):
        self.voiceCommand = activateVoiceCommand()

    def test_activateVoiceCommand(self):
        self.assertEqual(self.voiceCommand.activate(), "Voice command activated")

    def test_deactivateVoiceCommand(self):
        self.assertEqual(self.voiceCommand.deactivate(), "Voice command deactivated")

    def test_voiceCommandStatus(self):
        self.voiceCommand.activate()
        self.assertEqual(self.voiceCommand.status(), "Voice command is active")

        self.voiceCommand.deactivate()
        self.assertEqual(self.voiceCommand.status(), "Voice command is not active")

if __name__ == '__main__':
    unittest.main()
```