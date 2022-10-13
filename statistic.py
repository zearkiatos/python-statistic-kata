import pandas
import numpy


data = pandas.read_csv("./data/data.csv")


dataFrame = pandas.DataFrame(data)

def add_quantity(data:any, quantity:any)->int:

    data["CANTIDAD_GRATUITOS"] = quantity

    return data



def calculate_statistics(downloads: pandas.DataFrame) -> pandas.DataFrame:

    models = list(downloads["MODELO"].unique())
    row = {}
    new_list = []
    index_list = []

    downloads["CANTIDAD_GRATUITOS"] = 0

    for model in models:
        pagos = downloads[(downloads["MODELO"] == model) & (downloads["PAGO"] == 0)]
        index = list(pagos.index)
        quantity = len(pagos)
        if (len(index) > 0):
            for i in index:
                downloads.loc[i, ["CANTIDAD_GRATUITOS"]] = quantity  

    for model in models:
        download = downloads[(downloads["MODELO"] == model)
                             & (downloads["PAGO"] > 0)]
        pago = download["PAGO"]
        starts = download["ESTRELLAS"]
        comments = download[download["COMENTARIO"] == True]
        free_quantity = downloads[(downloads["MODELO"] == model) & (downloads["CANTIDAD_GRATUITOS"] == len(pago))]
        are_all_free = len(free_quantity) > 0
        if (len(download) > 0 and not are_all_free):
            if (not model in index_list):
                index_list.append(model)
            row = {
                "CANTIDAD": len(pago),
                "PROMEDIO": round(pago.mean(), 2),
                "MAXIMO": round(pago.max(), 2),
                "MINIMO":  round(pago.min(), 2),
                "ESTRELLAS": round(starts.mean(), 2),
                "DESV. ESTRELLAS": 0 if numpy.isnan(starts.std(axis=0, skipna=False)) else round(starts.std(axis=0, skipna=False), 2),
                "COMENTARIOS": len(comments)
            }
            new_list.append(row)

    new_list_dataframe = pandas.DataFrame(new_list, index=index_list)
    return new_list_dataframe.sort_index()


print(calculate_statistics(dataFrame))
