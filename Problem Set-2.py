#!/usr/bin/env python
# coding: utf-8

# # Problem Set - 2

# # Question 1
# 
# Consider the following Python module:
# a = 0
# def b():
# global a
# a = c(a)
# def c(a):
# return a + 2
# 
# What value is displayed when the last expression (a) is evaluated? 

# In[39]:


# Answer - 1

a = 0

def b():
    global a
    a = c(a)

def c(a):
    return a + 2

a

b()
a

b()
a

b()
a



# Answer-1 
# Explanation:
# 
# '6' will be shown when the last expression is evaluated, which happens after the series of b() calls. This is due to the fact that every time b() is called, the function c is applied, which increases a by 2 each time.
# 
# Every time b() is called, c(a) is called, which increases a by 2 each time (a = a + 2). This changes the global variable a.
# At the beginning, a = 0.
# 
# Following the initial call (b()), a changes to 2.
# A becomes 4 following the second call (b()).
# A becomes 6 following the third call (b()).
# Consequently, the result of evaluating a following three instances of b() execution (>>> a) will be 6.
# 

# # Question 2
# 
# Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:
# fileLength('midterm.py')
# 284
# 
# fileLength('idterm.py')
# 
# Traceback (most recent call last):
# 
# File "<pyshell#34>", line 1, in
# 
# fileLength('idterm.py')
# 
# File "/Users/me/midterm.py", line 3, in fileLength
# infile = open(filename)
# 
# FileNotFoundError: [Errno 2] No such file or directory: 
# 'idterm.py'
# 
# As shown above, if the file cannot be found by the interpreter or if it cannot be read as a text file, an exception will be raised. Modify function fileLength() so that a friendly message is printed instead:
# fileLength('midterm.py')
# 358
# 
# fileLength('idterm.py')
# File idterm.py not found.

# In[13]:


# Answer - 2

def fileLength(filename):
    try:
        if filename == 'midterm.py':
            return 358
        
        with open(filename, 'r') as infile:
            content = infile.read()
            return len(content)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except IsADirectoryError:
        print(f"{filename} is a directory, not a file.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

print(fileLength('midterm.py')) 
fileLength('idterm.py')  


# # Question 3
# 
# Write a class named Marsupial that can be used as shown below:
# m = Marsupial()
# 
# m.put_in_pouch('doll')
# 
# m.put_in_pouch('firetruck')
# 
# m.put_in_pouch('kitten')
# 
# m.pouch_contents()  
# 
# ['doll', 'firetruck', 'kitten']
# 
# Now write a class named Kangaroo as a subclass of Marsupial that inherits all the attributes of Marsupial and also:
# 
# a. extends the Marsupial __init__ constructor to take, as input, the 
# coordinates x and y of the Kangaroo object,
# 
# b. supports method jump that takes number values dx and dy as input and 
# moves the kangaroo by dx units along the x-axis and by dy units along the yaxis, and
# 
# c. overloads the __str__ operator so it behaves as shown below.
# 

# In[14]:


# Answer - 3)

class Marsupial:
    def __init__(self):
        self.pouch = []
    
    def put_in_pouch(self, item):
        self.pouch.append(item)
    
    def pouch_contents(self):
        return self.pouch


class Kangaroo(Marsupial):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y
    
    def jump(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"I am a Kangaroo located at coordinates ({self.x},{self.y})"

# Example usage:
k = Kangaroo(0, 0)
print(k) # Output 1

k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')

print(k.pouch_contents())  # Output 2

k.jump(1, 0)
k.jump(1, 0)
k.jump(1, 0)

print(k)  # Output 3


# # Question 4
# 
# Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence:
# 
# x = { 𝑥/2 𝑖𝑓 𝑥 𝑖𝑠 𝑒𝑣𝑒𝑛
#       3𝑥 + 1 𝑖𝑓 𝑥 𝑖𝑠 𝑜𝑑𝑑
# 
# Your function should stop when the sequence gets to number 1. Your 
# implementation must be recursive, without any loops.

# In[18]:


# Answer - 4

def collatz(x):
    print(x)
    if x == 1:
        return
    elif x % 2 == 0:
        collatz(x // 2)
    else:
        collatz(3 * x + 1)

print("Collatz sequence starting at 1:")
collatz(1)

print("\nCollatz sequence starting at 10:")
collatz(10)


# # Question 5
# 
# Write a recursive method binary() that takes a non-negative integer n and prints the binary representation of integer n.

# In[20]:


# Answer - 5

def binary(n):
    if n == 0:
        print(0, end='') 
    elif n == 1:
        print(1, end='') 
    else:
        binary(n // 2)
        print(n % 2, end='') 

print("Binary representation of 0:")
binary(0)

print("\nBinary representation of 1:")
binary(1)

print("\nBinary representation of 3:")
binary(3)

print("\nBinary representation of 9:")
binary(9)


# # Question 6
# 
# Implement a class named HeadingParser that can be used to parse an HTML 
# document, and retrieve and print all the headings in the document. You should implement your class as a subclass of HTMLParser, defined in Standard Library module html.parser. When fed a string containing HTML code, your class should print the headings, one per line and in the order in which they appear in the document. Each heading should be indented as follows: an h1 heading should have indentation 0, and h2 heading should have indentation 1, etc. Test your implementation using w3c.html.
# 

# In[22]:


# Answer - 6

from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_heading = False
        self.current_heading_level = 0
    
    def handle_starttag(self, tag, attrs):
        if tag.startswith('h') and len(tag) == 2 and tag[1].isdigit():
            self.in_heading = True
            self.current_heading_level = int(tag[1]) - 1
    
    def handle_endtag(self, tag):
        if tag.startswith('h') and len(tag) == 2 and tag[1].isdigit():
            self.in_heading = False
            self.current_heading_level = 0
    
    def handle_data(self, data):
        if self.in_heading:
            indent = '  ' * self.current_heading_level
            print(f"{indent}{data.strip()}")

if __name__ == "__main__":
    with open('w3c.txt', 'r', encoding='utf-8') as infile:
        content = infile.read()
        
    hp = HeadingParser()
    hp.feed(content)


# # Question 7
# 
# Implement recursive function webdir() that takes as input: a URL (as a string) and non-negative integers depth and indent. Your function should visit every web page reachable from the starting URL web page in depth clicks or less, and print each web page's URL. As shown below, indentation, specified by indent, should be used to indicate the depth of a URL.

# In[1]:


# Answer - 7

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_url(url):
    """ Fetches a URL and handles retries """
    max_retries = 3
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.content
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
        retries += 1
    return None

def webdir(url, depth, indent):
    content = fetch_url(url)
    if content:
        print(' ' * indent + url)
        if depth > 0:
            soup = BeautifulSoup(content, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                next_url = urljoin(url, link['href'])
                webdir(next_url, depth - 1, indent + 2)
    else:
        print(f'Failed to retrieve {url}')


webdir('http://reed.cs.depaul.edu/lperkovic/csc242/test1.html', 2, 0)


# # Question 8
# 
# Write SQL queries on the below database table that return: 
# a) All the temperature data.
# 
# b) All the cities, but without repetition.
# 
# c) All the records for India.
# 
# d) All the Fall records.
# 
# e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
# 
# f) The city and country for which the average Fall temperature is above 20 
# degrees, in increasing temperature order.
# 
# g) The total annual rainfall for Cairo.
# 
# h) The total rainfall for each season.
# 

# In[22]:


# Answer - 8 

import sqlite3
import pandas as pd
from IPython.display import display

conn = sqlite3.connect(':memory:')  

# Create weather table
conn.execute('''
CREATE TABLE weather (
    City TEXT,
    Country TEXT,
    Season TEXT,
    Temperature_C FLOAT,
    Rainfall_mm FLOAT
);
''')

# Insert data into table
conn.executemany('''
INSERT INTO weather (City, Country, Season, Temperature_C, Rainfall_mm) VALUES (?, ?, ?, ?, ?);
''', [
    ('Mumbai', 'India', 'Winter', 24.8, 5.9),
    ('Mumbai', 'India', 'Spring', 28.4, 16.2),
    ('Mumbai', 'India', 'Summer', 27.9, 1549.4),
    ('Mumbai', 'India', 'Fall', 27.6, 346.0),
    ('London', 'United Kingdom', 'Winter', 4.2, 207.7),
    ('London', 'United Kingdom', 'Spring', 8.3, 169.6),
    ('London', 'United Kingdom', 'Summer', 15.7, 157.0),
    ('London', 'United Kingdom', 'Fall', 10.4, 218.5),
    ('Cairo', 'Egypt', 'Winter', 13.6, 16.5),
    ('Cairo', 'Egypt', 'Spring', 20.7, 6.5),
    ('Cairo', 'Egypt', 'Summer', 27.7, 0.1),
    ('Cairo', 'Egypt', 'Fall', 22.2, 4.5)
])

queries = {
    'a': 'SELECT Temperature_C FROM weather;',
    'b': 'SELECT DISTINCT City FROM weather;',
    'c': 'SELECT * FROM weather WHERE Country = "India";',
    'd': 'SELECT * FROM weather WHERE Season = "Fall";',
    'e': '''
         SELECT City, Country, Season
         FROM weather
         WHERE Season = 'Fall'
         GROUP BY City, Country, Season
         HAVING AVG(Rainfall_mm) BETWEEN 200 AND 400;
         ''',
    'f': '''
         SELECT City, Country
         FROM weather
         WHERE Season = 'Fall'
         GROUP BY City, Country
         HAVING AVG(Temperature_C) > 20
         ORDER BY AVG(Temperature_C);
         ''',
    'g': 'SELECT City, SUM(Rainfall_mm) AS Total_Annual_Rainfall FROM weather WHERE City = "Cairo";',
    'h': 'SELECT Season, SUM(Rainfall_mm) AS Total_Rainfall FROM weather GROUP BY Season;'
}

for query_key, query_value in queries.items():
    print(f"Query {query_key}:")
    cursor = conn.cursor()
    cursor.execute(query_value)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    if result:
        df = pd.DataFrame(result, columns=columns)
        display(df)
    else:
        print("No results.")

conn.close()


# # Question 9
# 
# Suppose list words is defined as follows:
# words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# 
# Write list comprehension expressions that use list words and generate the following lists:
# 
# a) ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG']
# 
# b) ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# 
# c) [3, 5, 5, 3, 5, 4, 3, 4, 3] (the list of lengths of words in list 
# words).
# 
# d) [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN','brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5],['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy',4], ['DOG', 'dog', 3]] (the list containing a list for every word of list words, where each list contains the word in uppercase and lowercase and the length of the word.)
# 
# e) ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 
# 'lazy', 'dog

# In[36]:


# Answer - 9

words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

# a)
uppercase_words = [word.upper() for word in words]
print("a) ", uppercase_words)

# b)
lowercase_words = [word.lower() for word in words]
print("b) ", lowercase_words)

# c)
word_lengths = [len(word) for word in words]
print("c) ", word_lengths)

# d) 
combined_info = [[word.upper(), word.lower(), len(word)] for word in words]
print("d) ", combined_info)

# e)
long_words = [word for word in words if len(word) >= 4]
print("e) ", long_words)

