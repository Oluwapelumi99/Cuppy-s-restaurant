# Cuppy's Restaurant
![image of site](link to image) - use an image from AmIResponsive that shows the site on multiple devices

## Introduction
- This is a project demonstrating a restaurant booking system. In this project, I will create a system to reserve tables in a restaurant and users can also make changes to their booking. Users will also be able to leave reviews on what they think about this restaurant and they will be able to edit and delete these reviews if they wish to.
- Users will also have the opportunity to create their accounts which has to be done in order to make bookings or leave reviews and an email to verify their account and reset their account will be sent to their email address.
- This site was made to put what I have learnt so far in HTML, CSS, JAVASCRIPT AND PYTHON to test.

## Table of Contents

## User Experience
## Design
### Colour Scheme
### Typography
### Imagery
### Wireframes
### Figma/Full color mockup if produced
## Features
## Testing
## Technologies Used
## Cloning and forking.
## Deployment
## Credits

### User Stories
- User Goals
- Site Owner Goals

  ## Color Scheme
- The colors used for this project are #ffc0cb: this is used for the background color on all the other pages asides the home page.
- The home page uses a background picture from www.pexels.com. A transparent background color has been applied on the background image so whatever is written on it will be visible.
- There are 5 food image slides on the home page and all the pictures are from www.pexels.com. This was done to improve the look of the home page and to further depict what the site is about.
- #fff4f9; has been used for the text color and colors of the icons, which provides a great contrast against the transparent background.
- On the sign in, sign-up and sign out buttons, The background color when the mouse hovers over it is #ffc0cb and text color is #000000; after hover background color is set back to #000000; and the text color has been set to #ffc0cb. These have all been done for added accessibility.
- All links text on this app have been set to inherit the text color on the page and text decoration is underline. This makes the link text and other text on the page uniform and does not make the site look out of place.

  ## Typography
- The prefered font used is 'dancing script' and sans-serif has been added as a fall back incase the browser does not load the prefered font.


### Feature title - e.g. Navigation
Screenshot of implemented feature
Description of the value this feature has for the users

Repeat for each feature

## Testing

### Validation of Code
- I tested all the HTML pages with the W3C validatior which found a bug and the bug was fixed.
 #### index.html 
- The page presented with these errors on the first test.
<img width="1710" alt="Screenshot 2024-10-10 at 17 36 19" src="https://github.com/user-attachments/assets/722e4e35-91b5-407c-b6df-529a5c5eeca0">

- These errors were fixed by adding an alt text to the images, the pictures were later removed as they did not improve the user experience and were no longer needed. Also,the span was made into a div element and the closing p element was removed, then the page was tested again and it returned no errors as seen below.

<img width="1699" alt="Screenshot 2024-10-10 at 18 49 16" src="https://github.com/user-attachments/assets/ef7b4fc2-b43e-4114-9655-c9b071e2acad">

 #### booking.html
- The booking page presented with the errors as seen in the image below

<img width="1702" alt="Screenshot 2024-10-10 at 22 58 05" src="https://github.com/user-attachments/assets/56d48ea7-e59a-452b-af4c-eb7ed3852814">

- These errors were fixed by 






### Lighthouse


### Wave Webaim - accessibility testing
You can test your site for accessibility through the wave.webaim site - it needs to be deployed in order for it to test it. Fix any errors that it gives

### Manual Testing

You need to perform, and document everything you did to manually test your site.
At a minimum - you need to check every link on every page works as intended.
So that is check every link in the nav bar (do this on every single page because its a link in a different file) and any other links that appear on your site.
Test the responsiveness of the site - you can do this in the dev tools in responsive mode.
You should also load the site once deployed on as many devices you have access to. What is different from one device to the next? why is it different?

Test the user stories that you created earlier in the readme - did you satisfy the goal, how?

To write up the tests you can use a table,
| Feature being tested | Expected Outcome | Testing Performed | Actual Outcome | Result (Pass or fail) |
| -------------------- | ---------------- | ----------------- | -------------- | --------------------- |
| enter details here | enter details here | enter details here | enter details here | enter details here |

You should have tests for every section of every page.. individually.

### Automated Testing

- I started the automated testing by checking that the forms in my app are valid. 
- Started by creating a test_forms.py file and tested the form as seen in the image below.


## Technologies Used
- https://www.gitpod.io/
- https://code.visualstudio.com
- https://www.heroku.com
- https://pep8ci.herokuapp.com/
-

## Cloning and forking.
### CLONING
- On (https://github.com), navigate to the greeen <> code button on the right side of the page.
- copy the URL for the repository.
- To clone the repository using HTTPS, under HTTPS copy the URL
- To clone the repository using an SSH key, Click SSH then copy the URL.
- To clone a repository using github cli, click github cli then copy the URL.
- Open Terminal
- Change the current working directory to the location where you want the cloned directory.
- Type 'git clone', and then pate the URL you copied earlier.
- Press enter to create a local clone.

### FORKING
- On (https://github.com), navigate to the repository.
- In the top-right corner of the page, click Fork.
- Under 'owner', select the dropdown menu and click an owner for forked repository.
- By default, forks are named the same as their upstream repositories. Optionally, to further distinguish your fork, in the 'Repository name' field,type a name.
- Optionally, in the 'Description' field, type a description of your fork.
- Optionally, select copy the default branch only.
- Click create fork.


## Deployment
- This project has been deployed to https://www.heroku.com because heroku.
- The first step is to create an account on heroku and fill out the form provided.
- After submitting the form, an email will be sent to your email account to set password, then you can deploy your project.
- From the Heroku Dashboard, Click on the CREATE NEW APP. Then you name your app,then you select YOUR REGION, then click on 'CREATE APP'.
- Then  click on the SETTINGS tab on the next page.
- Then  create a CONFIG VAR which will hide details that you do not want others to see.
- Then move to the DEPLOY section on the heroku dashboard.
- Here choose to deploy from 'GITHUB' and confirm that you want to connect to github.
- Then search for your Github repository by typing in the name of the project.
- Click 'CONNECT' to link up Heroku app to github repository code.
- Then scroll down and choose how you want to deploy, whether 'MANUALLY' by clicking the 'DEPLOY BRANCH' option or 'AUTOMATICALLY' by clicking the 'ENABLE AUTOMATIC DEPLOYS'. 
- After app has been succesfully deployed, scroll back up and click on 'Open app' on the top right corner of the page, which takes you to the terminal to run your code.

## Credits
You need to credit where you got anything for your site from.. where are the images from, are they all from the same site? where did you get the content from, if you wrote it yourself, did you fact check anywhere? did you get code from anywhere? if so, it needs to be clearly marked in both the code and the readme.