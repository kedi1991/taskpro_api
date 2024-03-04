**TASK PRO v3.0**

![Mockup image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709507051/taskpro/responsive_design_kifar2.png)

[View live website](https://taskproapi-af20c66822dd.herokuapp.com/)


TaskPRO 3 is a task management app built using the Django rest framework. This applciation runs a front end based on React JS and a banckend based on Django Rest Framework.

This project is a reconfiguration of the dual project setup into a unified project

The goal for this project was to build a platform for project managers to keep track of tasks assiged to multiple people and keep track of all activities for easy follow up.

### Desired features
 - Simple and intuitive design
 - Responsive design to accomodate all screen sizes
 - User registration and authentication
 - Send alerts 
 - Create, read, update, deletion of projects and tasks
 - Filtering of tasks by status
 - Assign tasks to multiple users.


**Entities**

1. User (system)
The user with an account with TaskPRO.
Adding a new user automatically creates a profile with a default profile photo.

2. Profile (custom)
The user group with specific attributes and rights to individual functionality of the API

| Attribute name | Description | Data type|
|-----------------|-----------------|-----------------|
| owner | The user name | User|
|created_at | Date of creation of the user| DateTimeField|
|updated_at | Date of creation of updating the user details| DateTimeField|
|name |The full name of the user |CharField |
|about | The biography|TextField |
|image |The profile picture of the user |ImageField |


3. Task (custom)
The assigned duty to a user. this can be assigned to self or by another person. All tasks must belong to a project

| Attribute name | Description | Data type|
|-----------------|-----------------|-----------------|
| owner(FK) | The user who created the task | User|
|created_at | Date of creation of task| DateTimeField|
|task_name |The name of the task |CharField |
|description | The details of the task|TextField |
|assignees |Who the task is assigned to |User |
| related_name| | |
| project| The project in which the task belongs| Project|
| status| The status of the task (see status fields below) .|IntegerField |
|attachment|Any files related to the task|CharField|


*The use of attachments was disabled due to project timeline limitations


3.1. Status values

| Status choice | status value |
|-----------------|-----------------|
| 0 | Pending|
|1 | Executing|
|2 |Completed |
|3 |Blocked |


4. Project (custom)
The common task to be achived by users. Uers are assigned tasks to achieve the objective of the project. Any authenticated user can create a project.

owner = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

| Attribute name | Description | Data type|
|-----------------|-----------------|-----------------|
|owner(FK) | The user who created the project | User|
|created_at | Date of creation of project| DateTimeField|
|project_name |The name of the project |CharField |
|updated_at | When the project was updated|TextField |


### The API
The admin panel to the API can be accessibke from https://8000-kedi1991-taskproapi-kar66wgnemb.ws-eu108.gitpod.io/admin/login/?next=/admin/ 

Username: admin2024

Password: admin2024


### Wireframes
![sign in](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1705632444/taskpro/signin_wireframe_cunai8.png)

![sign up](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1705632444/taskpro/signup_wireframe_rssaam.png)

![nav bar](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1705632444/taskpro/top_navbar_wireframe_hvggy8.png)

![page view](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1705632445/taskpro/page_area_wireframe_adryuw.png)



### User stories

#### Navigation & Authentication

 - Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages
 - Routing: As a user I can navigate through pages quickly so that I can view content seamlessly without page refresh
 - Authentication - Sign up: As a user I can create a new account so that I can access all the features for signed up users
 - Authentication - Sign in: As a user I can sign in to the app so that I can access functionality for logged in users
 - Authentication - Logged in Status: As a user I can tell if I am logged in or not so that I can log in if I need to
 

#### Managing Tasks
 - Create tasks: As a logged in user I can create tasks so that I can view them later
 - View all tasks: As a user I can view the details of all tasks so that I can learn more about them
 - Edit task: As a task owner I can edit my tasks so that I can make corrections or update my task after they have been created
 - Delete tasks: As an owner of a task I can delete my task so that I can control removal of my tasks from the projects
 
 
#### Managing Projects
 - Create projects: As a logged in user I can create projects so that I can view them later
 - View all tasks: As a user I can view the details of all projects so that I can learn more about them
 - Edit project: As a project owner I can edit my projects so that I can make corrections or update my projects after they have been created
 - Delete projects: As an owner of a project I can delete my project so that I can control removal of my projects application
 

## Evolution of the app
The application has evolved from the first version to this current state following multiple changes in the user interface to consume API data and present it in a more user friendly way. The summary of interfaces are show below

### Task list
![image old tasks](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709507054/taskpro/list_tasks_old_qdknvq.png)

![iamge new task](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511141/taskpro/task_success_b0uhbt.png)


## Features Testing

### Home page
The home page includes a welcome message and  nav bar to access all other fetures of the app

![home page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709510404/taskpro/hpage_feme0g.png)

### Sign in
clicking the sign in link at the top right corner of the top nav bar, you will be able to see a login form. Enterign your credentials will allow you login. There is a possibility of signing up ebe after clicking the sign in link incase you do not have an account.

![sign in page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709510691/taskpro/signin_xmigwu.png)

![sign up page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709507053/taskpro/signup_page_old_bloxyr.png)


### Add task
After login, you will be able to add tasks into the database. Clinking add tasks link at the top right corner of the nav bar will display a page to add tasks. You will as well be shown a list of assignees (users in the system) and projects to categorise the task under

On successfull submission, you will get a notification of success.

![add task page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511141/taskpro/task_ee_fqa8ov.png)

![new task data page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511140/taskpro/not_task_xqgawy.png)

![new task success page image](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511141/taskpro/task_success_b0uhbt.png)

### Edit task
You can edit a task by clickign the blue button at the bottom of the task card. After editing the task, you can save changes.

![edit task](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511357/taskpro/edit_Task_a1vnz6.png)

### Delete task
You can delete a task or project using the same procedure. You cannot delete the task or project of another user. You will received a failed notification alert.

![failed delete task](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709511357/taskpro/delete_Fail_ikvdkp.png)


## Deployment of the app
1. This app contains 2 repositories merged into one
![dual project git](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709514115/taskpro/dualgit_efr0od.png)
9. Install white noise to manage static files using <code>pip3 install whitenoise==6.4.0</code> and add the dependency to requirements.txt file
10. Create a staticfiles directory in the root of the API repository
11. In the settings.py file, add whitnoise in the MIDDLEWARE list
12. In the TEMPLATES list, add <code> os.path.join(BASE_DIR, 'staticfiles', 'build')</code> in the DIRS key
13. Add <code> STATIC_ROOT = BASE_DIR / 'staticfiles'</code> and <code> WHITENOISE_ROOT = BASE_DIR / 'staticfiles' / 'build'</code> to the static files section
14. In the urls.py file, Remove the root_route view from the .views imports and Import the TemplateView from the generic Django views
15. In the url_patterns list, remove the root_route code and replace it with the TemplateView pointing to the index.html file
16. At the bottom of the file, add the 404 handler to allow React to handle 404 errors
17. Add api/ to the beginning of all the API URLs, excluding the path for the home page and admin panel
18. Open the axiosDefaults.js file, comment back in the axios.defaults.baseURL and set it to "/api"
19. Collect the admin and DRF staticfiles to the empty staticfiles directory you created earlier, with the following command in the terminal <code>python3 manage.py collectstatic </code>
20. cd into the front end project and Then run the command to compile and move the React files <code>npm run build && mv build ../staticfiles/. </code>
21. In the root directory of your project, create a new file named runtime.txt and Inside the runtime.txt, add the following line:<code>python-3.9.16</code>
22. Run the Django server, in the terminal type <code>python3 manage.py runserver</code>
23. Open the preview on port 8000


## Known issues
1. The top nav bar may not didplay the sign in status on some pages. In this case,  click sign in link to reveal the other links and the sign in status
2. When adding a project, sometimes, tou may be requested to authenticate, click sign in and you will see the logged in status in the nav bar. Then proceeed to create a project
3. the search filter at the top of the projects and task pages does not work. It has not been configured on time to meet project submission deadlines.
4. The addition of the task and project view may disappear on smaller screens. Thos was noticed after project compilations and deployment adn could not be changed on time.
5. No notification is displayed for blank inputs to the new task form and project forms.

## Planned features
1. Have cpability of tracking progress of tasks and projects
2. Enable user to update their profile details
3. Improve the user interface.
4. Add bootstrap notifications to all actions

## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python

### Libraries, frameworks and dependencies

- [Axios](https://axios-http.com/docs/intro) - Used axios to send API requests from the React project to the API.
- [JWT](https://jwt.io/) - library to decode out JSON Web token. Justification: I used JWT to prevent unauthenticated user from making extra network requests to refresh their access token. Also used to remove the timestamp from the browser when the user refreshes token expires or the user logs out.
- [React](https://17.reactjs.org/) - JavaScript library for building user interfaces
- [React-Bootstrap 4.6](https://react-bootstrap-v4.netlify.app/)  used Bootstrap React library for UI components, styling and responsiveness.
- [React Router](https://v5.reactrouter.com/web/guides/quick-start) - Used to enable the navigation among views of various components and control what the user sees depending on the URL they have accessed in the browser.

### Tools & Programs

- [Am I Responsive](http://ami.responsivedesign.is/) was used to create the multi-device mock-up
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Cloudinary](https://cloudinary.com/) to store static files
- [Favicon.io](https://favicon.io) for making the site favicon
- [Gitpod](https://gitpod.io/) was IDE used for writing code
- [GitHub](https://github.com/) was used as a remote repository
- Validation:
  - [ESLint](https://eslint.org/) used to validate JSX code
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/) used to validate performance, accessibility, best practice and SEO of the app

![lighthouse](https://res.cloudinary.com/dr7uvhdmd/image/upload/v1709516454/taskpro/lighthouse_qswyyf.png)



## Thanks to
- The slack community and CI tutors
- My mentor Gareth McGirr for the troubleshooting tips
