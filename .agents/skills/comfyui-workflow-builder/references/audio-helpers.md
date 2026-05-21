# Audio Helpers

```python
import soundfile as sf
import numpy as np
import torch

def _wav_to_audio(path: str) -> dict:
    """Load WAV → ComfyUI AUDIO dict."""
    data, sr = sf.read(path, dtype="float32")
    if data.ndim == 1:
        data = data[np.newaxis, :]
    else:
        data = data.T
    data = data[np.newaxis, ...]
    return {"waveform": torch.from_numpy(data), "sample_rate": sr}

def _audio_to_wav(audio_dict: dict, path: str) -> str:
    """ComfyUI AUDIO dict → WAV file."""
    wav = audio_dict["waveform"]
    sr = int(audio_dict.get("sample_rate", 22050))
    if isinstance(wav, torch.Tensor):
        wav = wav.cpu().numpy()
    wav = np.asarray(wav)
    if wav.ndim == 3:
        wav = wav[0]
    if wav.ndim == 1:
        wav = wav[np.newaxis, :]
    sf.write(path, wav.T, sr)
    return path
```
