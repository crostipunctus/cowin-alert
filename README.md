# cowin-alert
#### Video Demo:  <URL HERE>
#### Description:

Cowin-alert is a web-app that alerts signed-up users if vaccination slots open in the district of their choosing. 

##### Background:

India has implemented an app registration based covid vaccination system. The app is called CoWin and can be viewed here:[CoWin](www.cowin.gov.in). The government has released public API's for developers to access information about vaccines. Some are protected API's and some are private and require a license. 
My app uses the public API's to access vaccination slots based on the user's chosen district - but this app is only for 18-44 year olds who are yet to take their first dose because only this age group needs to mandatorily register and rules about second doses are yet to be framed.
Currently it is very difficult to find vaccination slots because of vaccine shortages and government incompetence and many developers have made their own bots to check for vaccination slots. I thought this was a great opportunity for me to test the skills I have learned over the last year since I started cs50x 2020. (Note: I also completed cs50 Web Development with Python and Javascript.)

##### How the app works:
First the user signs up and provides their email and chooses a district. They are redirected to a page that informs them that the app is searching for slots and that they will receive a mail if slots become available. 
If a lot becomes available they will receive a mail from the id cowinreallysucks@gmail.com informing them of the number of slots available and the center they are available at. 

##### The mechanism:
The app uses a combination of python and javascript in the Django framework to gather information from the user about the district they are interested in. The app then makes an ajax fetch request to the CoWin api for information about slot availability. The python script then parses the json response to find slot availability in the relevant districts and saves the centers and slots to the database and sends mails to the respective users. Each slot is identified by a unique ssession id from the API: as the python script loops through the data received, if the session id exists it is not updated in the databse. If a new session id is found, it is added to the database and if slot availibility in this session is more than zero a mail is sent to the users. States and districts have been preloaded into the database by me (more on this later).
From start to end this is the program flow: 
1. The user visits the register page and registers provides email and district. Template: register.html. url: 'register'. Register.html includes a chained dropdown list which uses ajax in the file register.js and the context from the view to render.
2. On clicking submit user is redirected to url 'index' and the index.html template is rendered. The template has text telling them that the program is looking for slots. Javascript, in the form of the file cowin.js, then makes a fetch request to views.py via the url 'user_dict'. the user_dict view queries the database to find which districts have been selected by the users - this is to avoid getting data from `all` districts (there are more than 700 districts in India). Cowin.js then makes a fetch request to the CoWin API using the district id's it received in the last step and then send this data via a post request to the 'py_api' view. This part - from making the API call to sending it to the view - is on an interval timer of 3 seconds, which adds up to 100 API calls every 5 minutes - this is the maximum allowed by CoWIn. THe fetch post call also sends the district id to the py_api view.
3. The py_api view first uses the district id to get a list of all emails that the data needs to be sent to in case of slot availability. The data which consists of lists and dicts inside a dict is looped through, first to filter the data based on age and then to find session ids and slot availabilty. Note: the program can find dose 2 availability to implement later once the dose 2 guidelines are formalized. Slots are saved based on the session id and if slots are more than zero, mails are sent to the users using Django's inbuilt mailing feature. 


##### Problems and decisions:
Initially I didn't want to involve the database at all. The program would just fetch slot availability and notify the users but I realized that for multiple users with different districts this would not work. I needed a way to store user information. Also, in the previous version there was no way to make sure the program sent emails only when slots opened up rather than send mails every time it detected that there were more than zero slots available. I needed some kind of persistence to compare the fetched results with the previous results. Thus I decided to use the database to store data and then compare that to the new data coming in. 
I had considered using python to do the API call but I couldnt figure out how to set it on an interval and since javascript was available I decided to use AJAX. 
Looping through the data was a challenge because of the nested structure. For the slot availability one needs to access a dict inside list inside a dict inside a list inside a dict inside a dict! This took me a while to work out. 
The chained dropdown list in the register page was a challenge. The program had to first let the user choose a state, which required the view to provide a queryset of states for the select element to loop through. Then based on this choice an ajax call is made to get the districts in that particular state. Once this is selected and the register button is clicked the data is sent to the register view which then saves the user and then associates a district with that user. 

##### Models:
The models I have used are: State, District, User_details, Center(this is the vaccination center) and Slots. State, district, center and slots are self-explanatory. User_details is an extention of the default User model in Django to store district and dose information. 
