# How models Work?  


## What is a ML Model? 
ML model is kinda like an entity that takes in traning data and uses patterns to give predictions. 


- Basic building blocks of Machine Learning models are the decision trees. 
- Traning a model is basically the process of fitting the data to the exisiting pattern. 
  
# Builiding a model, code-wise 

Model helps in prediction, the prediction equation has two parts 
X, y

``` 
y = X 

``` 
X is the data that's being supplied and y is the property/feature that's supposed to be predicted 

X mainly comprises of the data or the properties that are required so that the prediction can be made 

For example: 

``` 
y --> Probability of you passing or failing in an examination 
X --> [% of syllabus covered, no of mocks written, marks in mid1, marks in mid2] 
```

Using scikit learn, we **describe** the type of model we want 

``` 
model = sklearn.tree.DecisionTreeRegressor(random_state=1) 

specifying the random_state tells us how free can our model be
``` 

And then once our model is described, we use it to **fit** the data 

``` 
model.fit(X,y) 

```

Once the fitting/training of the model is completed, we then move on to 
the best part **predictions** 

``` 
prediction = model.predict(features_data) 

pass_or_fail = model.predicit(data_set[['% of syllabus covered', 'no of mocks written', 'marks in mid1', 'marks in mid2']])
``` 