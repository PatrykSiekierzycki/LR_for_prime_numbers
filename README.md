!!!! IN PROGRESS !!!!

Author: Patryk Siekierzycki

!!!! Warning: The program on this stage is not protected and contain many other disadvantages also from programming art side. It will be improved. !!!!

Small machine learning project with attempt to use linear regression model to predict prime numbers.

!!!! Conclusion: linear regression is not a good algorithm for that task. !!!!

What program do:
- Create and provide to linear regression model three numpy arrays:
  1. Integer numbers
  2. Is number primal
  3. Is number even
- Train and test model untill its accuracy will be bigger than 90% or user press: q. When one from both will happend then the model with best accuracy will be saved as: prime_numbers_model_lr.pickle file.

The bigger number you provied to creat model:
- the longer you will wait for finish
- and the accuracy will be smaller

How to do something with problems above:
- change the size of test_size in line: x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y ,test_size=0.1) , but you should not use to big value. The default value is 0.1 what is 10% of all data.
- you can also provide bigger number of data, but time before data will be created, will be longer.
- there is a line in first function which is not necessery, but it can show you actual number which function work (line 21). You can delete that line, (It contain also commentary to be easier founded.) but you lost possibility to check actual number.

My observation:
- beter option for test_size (look above) is value 0.1 than 0.2.
- waiting for milion number take big amount of time.
