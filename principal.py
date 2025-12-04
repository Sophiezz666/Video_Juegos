import pandas as pd
import matplotlib.pyplot as plt
#
#clase principal
class VideoJuegos:
    def __init__(self, archivo_csv):
        self.df = pd.read_csv(archivo_csv)
        print("Clase VideoJuegos lista")
        