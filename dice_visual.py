from plotly.graph_objs import bar, layout
from plotly import offline 
from die import die

# Create two D6 die
die_1 = Die()
die_2 = Die()

#Make some rolls, and store results in list 
results = []
for roll_num in range(1000):
    result = die_1.roll()+ die_2.roll()
    results.append(result)



#Analyse the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result +1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y= frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling 2 D6 die 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout' : my_layout}, filename='d6_d6.html')
