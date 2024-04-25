from dataclasses import dataclass

@dataclass
class AudioProcessingParams:
    file_path: str
    sample_rate: int = 44100
    channels: int = 2
