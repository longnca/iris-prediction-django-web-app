# Iris Prediction Web App using Scikit-learn and Django

## Introduction 

A simple project to practice building a web app using Django framework to predict Iris flower.

## Introduction to the Iris dataset

This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray.

The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

Read more about the Iris dataset [here](https://archive.ics.uci.edu/dataset/53/iris).

## How to install the dependencies

```bash
$ pipenv install --dev
```

## Machine learning model

I choose the **Support Vector Classification (SVC)** model since it's one of the models yielding the best accuracy and precision compared to other methods.

### Template Flow and Interaction

```mermaid
graph LR
    Base(('base.html')) -->|extends| Predict('predict.html')
    Predict -->|AJAX POST| PredictChancesURL(predict_chances in 'views.py')
    Predict -->|extends| Results('results.html')
    PredictChancesURL -->|returns JSON| Predict
    Results -->|view_results in 'views.py'| DB[("Database")]
```

### Models and Database

```mermaid
classDiagram
    class PredResults{
      +float sepal_length
      +float sepal_width
      +float petal_length
      +float petal_width
      +string classification
    }
    
    PredResults : - (iris_predict_app/models.py)

    class Database{
        Tables
    }

    PredResults --> Database: Stores to
```

### Views and URL Configuration

```mermaid
graph TD
    URLConfIris(iris/urls.py) --> URLConfApp(iris_predict_app/urls.py)
    URLConfApp -->|predict| ViewPredict(predict view)
    URLConfApp -->|iris_predict_app/| ViewPredictChances(predict_chances view)
    URLConfApp -->|results/| ViewResults(view_results view)

    ViewPredict -->|render| PredictT(predict.html)
    ViewPredictChances -->|process & respond| PredictAJAX
    ViewResults -->|render| ResultsT(results.html)

    PredictT -->|submit form| PredictAJAX("/iris_predict_app/")
    PredictAJAX -->|return data| PredictT
    ResultsT -->|display| DB[("Database")]
```