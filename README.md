This is a Python script that takes a user input, n, and computes 2^n using the algorithm outlined by Pingala in *Chandaḥśāstra*.

The script is designed to show the algorithm step-by-step. Here is an example of what the script outputs:

```
Please enter a number: 6
6 is even, so this step is SQUARE
Now we halve 6 to get...
3 is odd, so so this step is DOUBLE
Now we subtract 1 from 3 to get...
2 is even, so this step is SQUARE
Now we halve 2 to get...
1 is odd, so so this step is DOUBLE
Now we subtract 1 from 1 to get...
Goose egg
Now we have our steps:
['square', 'double', 'square', 'double']
Which we reverse to get:
['double', 'square', 'double', 'square']

Starting with a value of 1, let's follow the steps:
multiplying 1 by 2
yielded 2
squaring 2
yielded 4
multiplying 4 by 2
yielded 8
squaring 8
yielded 64
2^6 is 64
```

I learned about this algorithm in the article "[The Power of Two...in Poetry?](http://digitaleditions.walsworthprintgroup.com/article/The_Power_of_Two_._._._in_Poetry%3F/2298573/276852/article.html)" by Amy Shell-Gellasch and J.B. Thoo, which was published in *Math Horizons* in November 2015.
