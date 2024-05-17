import requests
import numpy as np

def load_data(size="28"):
  if size in ["64", "128", "224"]:
    response = requests.get(f'https://zenodo.org/records/10519652/files/dermamnist_{size}.npz')

    with open(f'dermamnist_{size}.npz', 'wb') as file:
      file.write(response.content)
  elif size == "28":
    response = requests.get('https://zenodo.org/records/10519652/files/dermamnist.npz')
    with open('dermamnist_28.npz', 'wb') as file:
      file.write(response.content)
  else:
    raise Exception("Incorrect image size! Please select: 28, 64, 128 or 224.")

  data = np.load(f'dermamnist_{size}.npz')

  return data['train_images'], data['train_labels'], data['val_images'], data['val_labels'], data['test_images'], data['test_labels']
