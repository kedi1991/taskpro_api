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

1. User
The user with an account with TaskPRO.
Adding a new user automatically creates a profile with a default profile photo.

2. Profile
The user group with specific attributes and rights to individual fucntionality of the API

3. Task
The assigned duty to a user. this can be assigned to self or by another person. All tasks must belong to a project

4. Project
The specific common goal for all persons. Tasks are assigned to different people based on the goals of the project


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
 


