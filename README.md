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




