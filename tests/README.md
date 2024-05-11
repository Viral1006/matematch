# Testing

We are primarily using unit testing to validate our software functionalities. Unit Testing tests individual components or units of the software. The tests are present in the "/src/tests" folder and are triggered using GitHub actions ("Unit_Tests.yml") whenever there is a push/pull request in the repository. 

If you need to run the test in your local system, use the following commands:

```
cd src
python manage.py test 
```

There are four test files for our software. They are:

#### 1. [test_url.py](https://github.com/rohitgeddam/FindMyRoomie/blob/README---Arun/src/tests/test_url.py):
Test code to validate the URLs of the web application. This tests whether the functionalities are mapped to their respective URLs. Tests the URLs of 'Homepage', 'My People', 'Find Room', 'My Room', and 'LogOut'.

#### 2. [test_model.py](https://github.com/rohitgeddam/FindMyRoomie/blob/README---Arun/src/tests/test_model.py):
Test code that creates a user object and checks if the values are correctly stored in the attributes.

#### 3. [test_views.py](https://github.com/rohitgeddam/FindMyRoomie/blob/README---Arun/src/tests/test_views.py):
Test code to check if the HTTP request was succesful (based on the status code).

#### 4. [test_utils.py](https://github.com/rohitgeddam/FindMyRoomie/blob/README---Arun/src/tests/test_utils.py):
Test code that validates the Email ID (checks if it is has a NCSU Email ID). 

#### 5. Live Server Test Demo:
Test code for live server test for Profile Edit Page and Profile Page. In order to run the test rename the 'liveserver.py' file to 'test_liveserver.py'.

https://user-images.githubusercontent.com/46688470/194781203-4a78dfb7-ee8a-480c-a8e6-7773f6479128.mp4


