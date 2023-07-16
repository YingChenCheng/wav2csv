import warnings
import pandas as pd
import numpy as np
import librosa
warnings.filterwarnings('ignore')

class Utils:
  @classmethod
  def wav2csv(cls, audio_file, file_name, toCSV=False):
    tamano = 0
    lista = []

    print("Working with WAV files...")

    sonido, _ = librosa.load(audio_file, sr=None)
    sonido = np.delete(sonido, np.where(sonido == 0))
    lista.append(sonido)
    if len(sonido) > tamano:
      tamano = len(sonido)

    columns = np.arange(0, tamano)
    df = pd.DataFrame(lista, columns=columns).fillna(0)

    if toCSV:
      print("Saving CSV file...")
      df.to_csv(file_name, index=False)

    return df

if __name__ == "__main__":
  df = Utils().wav2csv("wav2csv/test.wav", "wav2csv/test.csv", toCSV=True)
  # print(df)
