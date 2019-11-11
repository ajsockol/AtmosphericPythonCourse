#! /usr/bin/env python3

import numpy as np
import numpy.ma as ma
import warnings
from datetime import datetime as dt
# from datetime import timedelta as td
import datetime
import pytz
# from sys import exit as sysexit

print()

# What is the difference between regular Python and Numpy?
if True:
    print(type(1))
    print(type(1.))
    print(type('Hello World'))
    print(np.zeros(1, dtype=np.int8).dtype)
    print(np.zeros(1, dtype=np.int16).dtype)
    print(np.zeros(1, dtype=np.int32).dtype)
    print(np.zeros(1, dtype=np.int64).dtype)
    print(np.zeros(1, dtype=np.float16).dtype)
    print(np.zeros(1, dtype=np.float32).dtype)
    print(np.zeros(1, dtype=np.float64).dtype)
    print(np.zeros(1, dtype=np.bool_).dtype)
    print(np.zeros(1, dtype=np.int_).dtype)
    print(np.zeros(1, dtype=np.float_).dtype)
    print(np.zeros(1, dtype=np.uint).dtype)
    print(np.zeros(1, dtype=np.complex).dtype)
    print()

# Let's make some simple arrays
if False:
    a = [1, 2, 3]
    b = np.array([1, 2, 3])  # Create a 1-D array
    print('type(a):', type(a))  # Get type of a
    print('type(b):', type(b))  # Get type of b
    print('type(b[0]):', type(b[0]))  # Get type of index 0 of b
    print('b.dtype:', b.dtype)  # a.dtype will not work. dtype is numpy only.
    print('a:', a)
    print('b:', b)

# What's the difference between regular Python and numpy?
# The speed increase gets better with multidimentional data.
if False:
    num = 5000000
    print("Looping over {} values using for loop with list".format(num))

    start_datetime = dt.now()
    a = list(range(0, num))
    # Don't do this. This is not good python programming.
    for ii in a:
        a[ii] = a[ii] + 1

    if num < 10000000:
        python_time = (dt.now() - start_datetime).microseconds/1000000
    else:
        python_time = (dt.now() - start_datetime).seconds

    print('Elapsed Time: {}  seconds'.format(python_time))
    print()
    del a

    print("Using numpy to do same operation using Numpy arrays "
          "with {} values.".format(num*10))
    start_datetime = dt.now()
    a = np.arange(num*10, dtype=np.int16) + 1
    numpy_time = (dt.now() - start_datetime).microseconds/1000000

    print('Elapsed Time: {}  seconds'.format(numpy_time))

    print("\nRation of native python/numpy:", python_time/numpy_time)

# Can you swith between regular Python and numpy?
if False:
    num = 1000
    a = list(range(0, num))
    print('type(a):', type(a))
    print('len(a):', len(a))
    print()

    b = np.array(a)
    print('type(b):', type(b))
    print('b.shape:', b.shape)
    print()

    c = list(b)
    print('type(c):', type(c))
    print('len(c):', len(c))

# Let's make an array but of type float
if False:
    a = np.array([1, 2, 3.])
    print('a.dtype:', a.dtype)
    print('a:', a)
    print()

    b = np.array([1, 2, 3], dtype=float)
    print('b.dtype:', b.dtype)
    print('b:', b)

    c = np.array([4, 5, 6])
    c = c.astype(float)
    print('c.dtype:', c.dtype)
    print('c:', c)

# Let's start making larger arrays without needing to type all the values
if False:
    a = np.array(range(10))
    b = np.arange(10)
    c = np.arange(1, 10, 2)
    d = np.arange(10, 1, -1)
    e = np.flip(a)
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)

# Let's select values from our arrays
if False:
    a = np.arange(10)
    print('a:', a)
    print('a[0:5]:', a[0:5])  # selects upto but not including index 5
    print('a[0:]:', a[0:])  # selects everthing to end of array
    print('a[:5]:', a[:5])  # selects to upto but not including index 5
    print('a[3:5]:', a[3:5])  # selects from 3 upto but not including index 5
    print('a[0:-1]:', a[0:-1])  # selects upto but not including index 5
    print('a[0:100]:', a[0:100])  # index is past end of array?!?

# Let's get metadata about our arrays.
if False:
    a = np.arange(10)
    print('a:\n', a)
    print('a.shape:', a.shape)
    print('a.size:', a.size)
    print('len(a):', len(a))
    print()

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print('b:\n', b)
    print('b.shape:', b.shape)
    print('b.size:', b.size)
    print('len(b):', len(b))
    print()

    c = np.arange(10)
    c = c.reshape((2, 5))
    print('c:\n', c)
    print('c.shape:', b.shape)
    print('c.size:', b.size)
    print()

    print('c[1, 4]:', c[1, 4])
    print('c[1, 2:4]:', c[1, 2:4])
    print('c[:, 2:4]:\n', c[:, 2:4])
    print('c[0, :]:', c[0, :])
    print('c[1, 2:100]:', c[1, 2:100])  # over index handled OK? Maybe works

# Let's create some more complicated arrays
if False:
    a = np.zeros((2, 2))    # Create an array of all zeros
    print('a:\n', a)

    b = np.ones((2, 2))    # Create an array of all ones
    print('b:\n', b)

    c = np.full((2, 2), 7, dtype=int)   # Create a constant array
    print('c:\n', c)

    d = np.eye(2)           # Create a 2x2 identity matrix
    print('d:\n', d)

    e = np.random.random((2, 2))  # Create an array filled with random values
    print(e)

# Let's play with broadcasting
if False:
    a = np.zeros(20, dtype=int)
    print('a:', a)

    a = a + 1.
    print('a:', a)

    a = a.astype(int)
    a[0:9] = a[0:9] + 10
    print('a:', a)

    a = a + np.arange(a.size)
    print('a:', a)

    a += 100
    print(a)

# Let's start to work with booleans
if False:

    a = [False, True]
    b = np.array([False, True])
    print('a:', a, type(a))
    print('b:', b, type(b))
    print()

    c = np.arange(10, dtype=int)
    print('c:', c)

    bool_idx = c > 4
    print('bool_idx:', bool_idx)
    print('type(bool_idx):', type(bool_idx))
    print('bool_idx.dtype:', bool_idx.dtype)
    print('c[bool_idx]: ', c[bool_idx])

    # Finde where c is great than 6 and set to -1
    c[c > 6] = -1
    print('\nc:', c)
    print()

    # Find index numbers where c is great than or equal to 2
    d = np.where(c >= 2)
    print('d:', d)
    print('type(d):', type(d))
    print('d[0]:', d[0])

    # What about testing all the values in the array?
    e = np.zeros(10, dtype=bool)  # Create an array of all False
    e[3:8] = True  # Set values at index 3 to 7 to True
    print('\ne:', e)
    print('e.all():', e.all())  # Check if all values are True
    print('e.any():', e.any())  # Check if any values are True

# Let's play with IEEE NaN for missing data
if False:
    # Initially create an integer array. But we will see that it needs to be a float.
    a = np.arange(10)  # , dtype=float)
    print('a:', a)

#    a[a == 9] = np.nan  # This will initially fail because NaN is a float
    a[3:7] = np.nan  # This will have issues because a is an int. Needs to be float.
    print('a:', a)

    b = (a == np.nan)
    print('\nb:', b)

    b = np.isnan(a)
    print('\nb:', b)
    print()

# Let's calculate some statistics with NaNs! Whew finally!
if False:
    a = np.arange(10, dtype=float)
    print('a:', a)
    print('a.min():', a.min())  # This is Python min method, not numpy
    print('np.min(a):', np.min(a))  # This is numpy min function

    a[0] = np.nan
    print()

    # Calculate the mean. Notice how it returns NaN. The NaNs are tainting
    # all the operations.
    print('np.mean(a):', np.mean(a))

    # This is telling Numpy to ignore the NaN values in the calculations.
    print('np.nanmean(a):', np.nanmean(a))

    # This will work but it will create a warning message.
    if True:
        print('\nnp.nanmean(np.array([np.nan, np.nan])):',
              np.nanmean(np.array([np.nan, np.nan])))
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            b = np.array([np.nan, np.nan])
            print('\nnp.nanmean(np.array([np.nan, np.nan])):', np.nanmean(b))

# Let's calculate some statistics of multi dimentional data!
if False:
    a = np.arange(20)  # This is a 1-D array
    a = a.reshape((4, 5))  # This is now a 2-D array (or matrix)
    print('a:\n', a)

    b = np.max(a, axis=1)
    print('b:', b)

    c = np.mean(a, axis=0)
    print('c:', c)  # Note how the returned array is orientated.
    print()

    a = a.astype(float)  # Converting to float to use NaNs
    a[1, 3] = np.nan
    print('a:\n', a)
    print()

    print('np.nansum(a):', np.nansum(a))
    print()

    d = np.nansum(a, axis=-1)
    print('d:', d)

    d = np.nansum(a, axis=1)
    print('d:', d)


# Now let's play with matrix addition, subtraction, division, ...
if False:
    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)

    print('x:\n', x)
    print('y:\n', y)

    v = np.array([9, 10])
    w = np.array([11, 12])

    print('v:\n', v)
    print('w:\n', w)
    print()

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print('x + y:\n', x + y)
    print('np.add(x, y):\n', np.add(x, y))
    print()

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print('x - y:\n', x - y)
    print('np.subtract(x, y):\n', np.subtract(x, y))
    print()

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print('x * y:\n', x * y)
    print('np.multiply(x, y):\n', np.multiply(x, y))
    print()

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print('x / y:\n', x / y)
    print('np.divide(x, y):\n', np.divide(x, y))
    print()

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print('np.sqrt(x):\n', np.sqrt(x))  # Notice there is no x.sqrt() option
    print()

    # Inner product of vectors; both produce 219
    print('v.dot(w):\n', v.dot(w))
    print('np.dot(v, w):\n', np.dot(v, w))
    print()

    # Matrix / vector product; both produce the rank 1 array [29 67]
    print('x.dot(v):\n', x.dot(v))
    print('np.dot(x, v):\n', np.dot(x, v))
    print()

    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print('x.dot(y):\n', x.dot(y))
    print('np.dot(x, y):\n', np.dot(x, y))

# Now some more broadcasting fun
if False:
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v  # Add v to each row of x using broadcasting
    print('y:\n', y)
    print()

    a = np.arange(12)
    a = a.reshape((3, 4))
    print('a:\n', a)

    b = np.array([1, 0, 1])
    print('b.shape:', b.shape)
    print('b:', b)
    print()

    # Reshape the array to be in correct orientation
    if False:
        b = b.reshape((3, 1))
        print('b.shape:', b.shape)
        print('b:\n', b)

    c = a + b  # Add v to each row of x using broadcasting
    print('\nc:\n', c)

# Now lets look at Numpy masked arrays and why they are awesome!
if False:
    # First create a numpy array
    a = np.array([0, 1, 2, 3, 4, 5])
    # Next create a numpy masked array and set the mask values.
    # A 0 = False and 1 = True
    masked_a = ma.masked_array(a, mask=[0, 1, 0, 0, 1, 0])
    print('masked_a:', masked_a)
    # Calculate the mean not using the masked values
    masked_a_mean = masked_a.mean()
    print('masked_a_mean:', masked_a_mean)
    print()

    # Create a masked array and set all the mask values to False
    # and set a fill_value other than the default.
    masked_a = ma.masked_array(a, mask=False, fill_value=-99999)
    print('masked_a:', masked_a)
    print('masked_a.data:', masked_a.data)
    print('masked_a.mask:', masked_a.mask)
    print('masked_a.fill_value:', masked_a.fill_value)
    print()

    # Create a masked array where all values less than or equal to
    # 1 are masked
    masked_c = ma.masked_less_equal(a, 1)
    print('masked_c:', masked_c)
    print('masked_c.data:', masked_c.data)
    print('masked_c.mask:', masked_c.mask)
    print('masked_c.mean():', masked_c.mean())
    print('np.mean(masked_c.data):', np.mean(masked_c.data))
    print()

    # Create a masked arra where all values less than or equal to
    # 1 are masked. Same as above but with different syntax.
    masked_d = ma.masked_where(a <= 1, a)
    print('masked_d:', masked_d)

    # Create a masked array with no mask set, yet.
    masked_d = ma.masked_array(a)
    print('masked_d:', masked_d)

    # Set the mask to True for all indexes less than 3.
    # Notice that we never create a mask, all that is done automatically.
    masked_d[:3] = ma.masked
    print('masked_d:', masked_d)
    print()

    # Reset the mask to all False
    masked_d.mask = False
    print('masked_d:', masked_d)

# Some of the nuances of performance with masked arrays
if False:
    num = 5000000  # The size of the array we are going to play with
    # We can create an array of all ones with type integer 16 bit
    masked_a = ma.ones(num, dtype=np.int16)
    print('masked_a.dtype:', masked_a.dtype)
    print('masked_a.size:', masked_a.size)
    print()

    # Now we will set most of the values to be masked
    masked_a[:num-1000] = ma.masked
    # Now lets print the sum of the mased array using default masked array
    # methods and then we will sum using numpy of just the data stored in
    # the masked array without using the mask.
    print('masked_a.sum():', masked_a.sum())
    print('np.sum(masked_a.data):', np.sum(masked_a.data))
    print()

    # Create a new clean masked array with mask not set yet.
    # Since the mask array is the same size as data array this can be
    # large and take longer.
    masked_a = ma.ones(num, dtype=np.int16)

    # Now we will add a random number to the masked array of ones.
    masked_a = masked_a + np.random.random(num)

    # Next we calculate the standard deviation of the masked array
    masked_a_std = ma.std(masked_a)
    print('masked_a_std:', masked_a_std)
    print()

    # Here we add some random noise spikes
    masked_a[np.random.randint(0, high=num, size=10000)] = 20

    # Here we mask out the values that are great than one standard deviation.
    # Now the mask is created, since it did not exist before this.
    masked_b = ma.masked_outside(masked_a, 1 - masked_a_std, 1 + masked_a_std)

    # Here we mask out some random values. Notice we are not using
    # masked_b.mask. That is slower and not correct. If the mask did not
    # already exist it would have an error. This way will create the mask
    # if it was not already created.
    masked_b[np.random.randint(0, high=num, size=1000)] = ma.masked

    # This is the sum of the data with all masked values excluded
    print('np.sum(masked_a):', np.sum(masked_b))

    # This is the sum of the data without excluding any values.
    print('np.sum(masked_b.data):', np.sum(masked_b.data))
    print()

    # Now lets convert everything back to a regular numpy array
    # but set the masked values to NaNs in the numpy array
    masked_b.fill_value = np.nan
    b = ma.filled(masked_b)
    print('type(masked_b):', type(masked_b))
    print('b.dtype:', b.dtype)
    # Notice the value is NaN because we are not using np.nanmax(). This means
    # there is at least one NaN in the array.
    print('np.max(b):', np.max(b))

# Because we will work with time series data let's learn about Python datetime objects.
# This is so we understand how the native time works with Python. We will then
# learn about Numpy dates and times.
if False:
    a = datetime.datetime.now()
    print('datetime.datetime.now():', a)

    a = datetime.date.today()
    print('datetime.date.today():', a)

    a = datetime.date(2019, 4, 13)
    print('datetime.date(2019, 4, 13):', a)

    # timestamp is number of seconds from 1970-01-01 00:00:00 or epoch.
    timestamp = datetime.date.fromtimestamp(1326244364)
    print("\ntimestamp:", timestamp)
    timestamp = datetime.datetime.fromtimestamp(1326244364)
    print("timestamp:", timestamp)

    # date object of today's date
    today = datetime.date.today()
    print("\ntoday.year:", today.year)
    print("today.month:", today.month)
    print("today.day:", today.day)

    # time(hour = 0, minute = 0, second = 0)
    a = datetime.time()
    print("\ndatetime.time():", a)
    # time(hour, minute and second)
    b = datetime.time(11, 34, 56)
    print("datetime.time(11, 34, 56):", b)
    # time(hour, minute and second)
    c = datetime.time(hour=11, minute=34, second=56)
    print("c:", c)
    # time(hour, minute, second, microsecond)
    d = datetime.time(11, 34, 56, 234566)
    print("d:", d)

    # datetime(year, month, day)
    e = datetime.datetime(2018, 11, 28)
    print("\ne:", e)
    # datetime(year, month, day, hour, minute, second, microsecond)
    f = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
    print("f:", f)

    # current date and time
    now = datetime.datetime.now()
    g = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\ng:", g)
    h = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("h:", h)

    date_string = "21 June, 2018"
    print("\ndate_string =", date_string)
    date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)

    local = datetime.datetime.now()
    print("\nLocal:", local.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.datetime.now(tz_NY)
    print("New York:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_Paris = pytz.timezone('Europe/Paris')
    datetime_Paris = datetime.datetime.now(tz_Paris)
    print("Paris:", datetime_Paris.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_utc = pytz.timezone('UTC')
    datetime_utc = datetime.datetime.now(tz_utc)
    print("UTC:", datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))
    datetime_utc = datetime.datetime.utcnow()
    print("utcnow():", datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))


# Because we will work with time series data let's learn about Numpy datetime objects.
# Initially all datetimes were in UTC. Now the datatime is timezone naive. You can use
# a timezone offset from UTC but that feature is being phased out.
if False:
    date = np.datetime64('2005-02-25')
    print('date:', date)
    print('date.dtype:', date.dtype)

    dt1 = np.datetime64('2005-02-25T03:30:55')
    print('\ndt1:', dt1)

    dt2 = np.datetime64('2012-03', 's')
    print('\ndt2:', dt2)
    print("dt2.astype('datetime64[h]'):", dt2.astype('datetime64[h]'))

    dt3 = np.arange('2005-02', '2005-03', dtype='datetime64[D]')
    print('\ndt3:', dt3)

    dt_diff1 = np.datetime64('2009-01-01') - np.datetime64('2008-01-01')
    print('\ndt_diff1:', dt_diff1)

    dt_diff2 = np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')
    print('\ndt_diff2:', dt_diff2)

    print("\nnp.datetime64('nat'):", np.datetime64('nat'))
    print("np.datetime64():", np.datetime64())

    dt4 = np.arange('2005-02-01T00:00:00', '2005-02-05T00:00:00', dtype='datetime64[D]')
    print('dt4:', dt4)
    print("\ndt4 + 23:", dt4 + 23)

    dt4 = dt4 + 23
    dt4 = dt4.astype('datetime64[s]')
    print("\ndt4:", dt4)

    print("\nnp.datetime64('today'):", np.datetime64('today'))
    print("np.datetime64('now'):", np.datetime64('now'))
    print("np.datetime64('now'):", np.datetime64('now', 'ns'))

# How do we convert from python datetime to numpy datetime64 and vice a versa?
if False:

    dt = datetime.datetime.utcnow()  # Get current date and time with python datetime
    # Get current date and time with in Numpy using same date and time
    # from python datetime
    dt64 = np.datetime64(dt)
    if False:
        # This is how we can get current date and time with just Numpy datetime.
        # Notice the precision is only down to second.
        dt64 = np.datetime64('now', 'us')
    print('dt:  ', dt)
    print('dt64:', dt64)

    # To convert from numpy datetime64 to python datetime
    # set precision to seconds and convert to integer. This will
    # give number of seconds since epoch, or timestamp.
    ts = dt64.astype('datetime64[s]').astype(int)
    print("\nts:", ts)
    # Use the timestamp with datetime timestamp method in UTC.
    dt64_to_dt = datetime.datetime.utcfromtimestamp(ts)
    print('dt64_to_dt:', dt64_to_dt)

    # To convert from python datetime to numpy datetime64 put the
    # python datetime into numpy datetime64. You can set the
    # numpy precision to seconds to match for printing.
    dt_to_dt64 = np.datetime64(dt)
    dt_to_dt64 = dt_to_dt64.astype('datetime64[s]')
    print("dt_to_dt64:", dt_to_dt64)

print()
