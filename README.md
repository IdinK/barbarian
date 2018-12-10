# Barbarian
Barbarian is a Python package for creating nice and colourful progress bars using the map() and apply() method as well as for loops.

## ProgressBar
To use a progress bar you need to initiate a ProgressBar object with the maximum progress amount (total) and call the show method of the object with the amount to update the progress bar.

```python
from barbarian import ProgressBar
from time import sleep

bar = ProgressBar(total=100)

for i in range(100):
  sleep(0.05)
  bar.show(amount=i+1)
```

You can also add your own text to the progress bar.

```python
bar = ProgressBar(total=100)
for i in range(100):
    sleep(0.05)
    bar.show(amount=i+1, text=f'working on {i}')
```


## map
You can also use the ProgressBar's map method instead of Python's map method. The output is an iterable. As soon as you turn the iterable object into a list the progress bar will be displayed.

```python
from barbarian import ProgressBar
from time import sleep

list1 = list(range(100))

def wait_and_double(x, wait_time):
    sleep(wait_time)
    return x*2

# this will not make the progress bar appear
iterable2 = ProgressBar.map(
    function=lambda x: wait_and_double(x=x, wait_time=0.05), 
    iterable=list1
)

# this will make the progress bar appear
list2 = list(iterable2)
```

## apply
ProgressBar also works with Panda's DataFrame and Series objects. 

```python
from barbarian import ProgressBar
from time import sleep
from pandas import DataFrame

data = DataFrame({
    'name':['Arminius', 'Boudica', 'Alaric', 'Attila', 'Genseric'],
    'ethnicity': ['German', 'Celt', 'Goth', 'Hun', 'Vandal']
})

data['name_and_ethnicity'] = ProgressBar.apply(
    data=data, 
    function=lambda x: x['name']+' the '+x['ethnicity']
)

data['name_lower'] = ProgressBar.apply(
    series=data['name'], 
    function=lambda x: x.lower()
)
```
