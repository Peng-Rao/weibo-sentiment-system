from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd
import plotly.figure_factory as ff


def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    x = ['True Negative', 'False Positive']
    y = ['False Negative', 'True Positive']
    z = cm[::-1]
    z_text = [[str(y) for y in x] for x in z]
    fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text)
    fig.show()
