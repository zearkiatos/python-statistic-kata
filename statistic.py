import pandas
import numpy


data = pandas.read_csv("./data/data.csv")


dataFrame = pandas.DataFrame(data)

print(dataFrame)


def calculate_statistics(downloads: pandas.DataFrame) -> pandas.DataFrame:

    models = list(downloads["MODELO"].unique())
    row = {}
    new_list = []
    index_list = []

    for model in models:
        download = downloads[(downloads["MODELO"] == model)
                             & (downloads["PAGO"] > 0)]
        pago = download["PAGO"]
        starts = download["ESTRELLAS"]
        comments = download[download["COMENTARIO"] == True]
        if (len(download) > 0):
            if (not model in index_list):
                index_list.append(model)
            row = {
                "CANTIDAD": len(pago),
                "PROMEDIO": round(pago.mean(), 2),
                "MAXIMO": round(pago.max(), 2),
                "MINIMO":  round(pago.min(), 2),
                "ESTRELLAS": round(starts.mean(), 2),
                "DESV. ESTRELLAS": 0 if numpy.isnan(starts.std(axis=0, skipna=False)) else round(starts.std(axis=0, skipna=False), 2),
                "COMENTARIOs": len(comments)
            }
            new_list.append(row)

    new_list_dataframe = pandas.DataFrame(new_list, index=index_list)
    return new_list_dataframe


print(calculate_statistics(dataFrame))
