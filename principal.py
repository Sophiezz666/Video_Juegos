import pandas as pd
import matplotlib.pyplot as plt

class VideoJuegos:
    def __init__(self, archivo_csv):
        self.df = pd.read_csv(archivo_csv)
        print("Clase VideoJuegos lista")
        