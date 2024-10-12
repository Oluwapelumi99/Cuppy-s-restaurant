# Cuppy's Restaurant

## Introduction
- This is a project demonstrating a restaurant booking system. In this project, I will create a system to reserve tables in a restaurant and users can also make changes to their booking. Users will also be able to leave reviews on what they think about this restaurant and they will be able to edit and delete these reviews if they wish to.
- Users will also have the opportunity to create their accounts which has to be done in order to make bookings or leave reviews and an email to verify their account when they register will be sent to their email address and they can also reset their password if they have forgotten their password.
- This site was made to put what I have learnt so far in HTML, CSS, JAVASCRIPT AND PYTHON to test.

<img width="1695" alt="Screenshot 2024-10-11 at 22 35 57" src="https://github.com/user-attachments/assets/d73fbc7e-7867-494b-8ca4-44ce425c359a">

## Table of Contents

## User Stroies
- User Goals
- Site owner goals
## Design
- Colour Scheme
- Typography
- Imagery
## Features
- Favicon
- Nav bar
- Home page
- Bookings page
- Reviews page
- Register page
- Sign up page
- Email verification page
## Testing
- Manual testing
- Automated testing
## Bugs
- Solved bugs
## Validator testing
- HTML
- CSS
- JAVASCRIPT
- PYTHON
## Accessibility
## Unfixed bugs
## Cloning and Forking
## Technologies used
## Deployment
## Credits
-Media
-Fonts
-Icons
-Content

### User Stories
- User Goals
- Site Owner Goals


## Design
  ### Color Scheme
- The colors used for this project are #ffc0cb: this is used for the background color on all the other pages asides the home page.
- The home page uses a background picture from www.pexels.com. A transparent background color has been applied on the background image so whatever is written on it will be visible.
- There are 5 food image slides on the home page and all the pictures are from www.pexels.com. This was done to improve the look of the home page and to further depict what the site is about.
- #fff4f9; has been used for the text color and colors of the icons, which provides a great contrast against the transparent background.
- On the sign in, sign-up and sign out buttons, The background color when the mouse hovers over it is #ffc0cb and text color is #000000; after hover background color is set back to #000000; and the text color has been set to #ffc0cb. These have all been done for added accessibility.
- All links text on this app have been set to inherit the text color on the page and text decoration is underline. This makes the link text and other text on the page uniform and does not make the site look out of place.

  ### Typography
- The prefered font used is 'dancing script' and sans-serif has been added as a fall back incase the browser does not load the prefered font.

  ### Imagery
- Image used on the home page matches the theme of the site. Image is seen below. It is gotten from https://www.pexels.com
<img width="1710" alt="Screenshot 2024-10-11 at 00 43 30" src="https://github.com/user-attachments/assets/239a1f5b-7119-48dc-bb30-2c1e8d0cf3c4">

### Features

### navigations
<img width="1710" alt="Screenshot 2024-10-11 at 01 18 50" src="https://github.com/user-attachments/assets/1186f933-d7ed-444a-bdcb-14de4f5eb67b">

- At the top of the page, we can see 'Cuppy's', which is the restaurant's name, clicking on Cuppy's lead us to the home_page as seen below.
<img width="1703" alt="Screenshot 2024-10-11 at 01 08 05" src="https://github.com/user-attachments/assets/fd0422a8-e487-4d77-8ee3-8e6f99cce32b">

- The navigation bar also shows the home pae and clicking on this will also take us to the home_page as seen below.
<img width="1703" alt="Screenshot 2024-10-11 at 01 08 05" src="https://github.com/user-attachments/assets/fd0422a8-e487-4d77-8ee3-8e6f99cce32b">

- The booking page link called 'BOOKINGS' can also be seen on the nav bar, clicking on this will take us to the booking page as seen below.
<img width="1710" alt="Screenshot 2024-10-11 at 01 09 20" src="https://github.com/user-attachments/assets/67a59977-8ba7-49ac-8c3b-33303aecb11f">

- The other nav items are the Register and login links if the user has not yet registered an account but if the user as an account, it is just logout link next.
- The user has not logged in now.
<img width="1702" alt="Screenshot 2024-10-11 at 01 10 27" src="https://github.com/user-attachments/assets/2081b28d-1ec8-4ea5-a676-6827c6f3cdef">
- When the log in nav is clicked.
<img width="1700" alt="Screenshot 2024-10-11 at 01 12 22" src="https://github.com/user-attachments/assets/e9286488-8925-439a-97d3-0e321c97e6f6">
-If a user has logged in and the log out nav item is clicked.
<img width="1706" alt="Screenshot 2024-10-11 at 01 15 57" src="https://github.com/user-attachments/assets/16db7529-d6dc-47a1-bc2b-9b46b62ad91b">

- On the right corner of the nav bar, the log in status and user name has been added for easy visibility and to improve user's experience so they know if they are logged in and if they are not logged in, it says so as seen in the image below.



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

<img width="1702" alt="Screenshot 2024-10-10 at 23 22 26" src="https://github.com/user-attachments/assets/a0151be6-6627-4d49-b064-0f1573884109">

- This error was fixed by taking out the trailing div

<img width="1704" alt="Screenshot 2024-10-10 at 23 31 18" src="https://github.com/user-attachments/assets/2b946a87-ca60-469b-9c5c-4d52658dd191">

#### view_booking.html
- The view booking page which is relate to the view function customer bookings was tested and it presented an error as ssen below.
<img width="1702" alt="Screenshot 2024-10-10 at 23 47 36" src="https://github.com/user-attachments/assets/b871c2e6-55b7-4a03-b8e2-564af9f36bc4">

- The error was fixed by adding an opening form tag to the trailing closing form tag in login.html file.
<img width="1704" alt="Screenshot 2024-10-10 at 23 55 01" src="https://github.com/user-attachments/assets/be79a45e-a6e8-4aac-9362-08d32f8f9ab8">

#### cancel_booking.html
- The cancel booking page was tested and found no errors as shown below.
<img width="1699" alt="Screenshot 2024-10-10 at 23 58 44" src="https://github.com/user-attachments/assets/b52c47c8-e74a-4358-87e0-51d7bbd6905c">

#### create_review.html
-The create review page was tested by and showed errors as seen in the image below.
<img width="1704" alt="Screenshot 2024-10-11 at 00 11 55" src="https://github.com/user-attachments/assets/e7018f41-50d7-495a-9918-ab8f32e8ac4d">
 
- These errors were fixed by taking out the type = submit attribute as they are no longer buttons and have been changed to spans. Fixed screenshot can be seen below.
<img width="1705" alt="Screenshot 2024-10-11 at 00 15 30" src="https://github.com/user-attachments/assets/2cc3b18e-dfda-421f-8f45-a569f6be10f1">

#### reviews.html
- The reviews list page was tested and it returned no errors.
<img width="1702" alt="Screenshot 2024-10-11 at 00 27 57" src="https://github.com/user-attachments/assets/def40845-2d0f-480b-a234-ebdaf0a8e0c7">


### CSS testing
- The css was tested and it did not give any errors. Image seen below.
<img width="1704" alt="Screenshot 2024-10-11 at 03 36 21" src="https://github.com/user-attachments/assets/a0293f97-9dc6-4802-829d-ba26e4e5c91b">


- ### Javascript testing
- The Javascript was tested and it did not give any warnings. Image seen below.
<img width="1706" alt="Screenshot 2024-10-11 at 03 41 27" src="https://github.com/user-attachments/assets/72c37690-4b82-4e1b-a65b-8ae7c395da6a">

- ### Python testing
- 


### Lighthouse

- I confrimed that the colors and font chosen are easy to read and accessible by running it through lighthose in dev tools. And I also made sure all buttons were asseccible by screen readers by adding an aria-label attribute to each button and image.

- ### Home page
<img width="1703" alt="Screenshot 2024-10-12 at 01 02 36" src="https://github.com/user-attachments/assets/b8f8cd8e-5685-473a-95fb-1f1a0e45bb80">
<img width="1707" alt="Screenshot 2024-10-12 at 01 03 28" src="https://github.com/user-attachments/assets/c62fb028-3c09-4def-bc92-f59d0cf30c61">
<img width="1707" alt="Screenshot 2024-10-12 at 01 03 51" src="https://github.com/user-attachments/assets/fb1aa611-0607-4d96-b519-a6f8a487a66e">

- ### Bookings page 
<img width="1695" alt="Screenshot 2024-10-12 at 01 05 00" src="https://github.com/user-attachments/assets/c2262ae4-40f3-4f02-a609-65dd4135ed1b">
<img width="1700" alt="Screenshot 2024-10-12 at 01 05 16" src="https://github.com/user-attachments/assets/7d036862-8f0a-4736-aea3-82ecc52bde85">

- ### Reviews page 



- ### Register page
<img width="1708" alt="Screenshot 2024-10-12 at 01 06 49" src="https://github.com/user-attachments/assets/4eee25c5-4d1c-42a6-8b94-f6702597fc9f">
<img width="1710" alt="Screenshot 2024-10-12 at 01 07 06" src="https://github.com/user-attachments/assets/b56ad14b-9c90-4b41-87ce-1dcc1681e6d0">

- ### Login page
<img width="1708" alt="Screenshot 2024-10-12 at 01 08 18" src="https://github.com/user-attachments/assets/166fa607-f74e-4f87-bbfa-0638000524f4">
<img width="1710" alt="Screenshot 2024-10-12 at 01 08 34" src="https://github.com/user-attachments/assets/91d88e27-ce52-4650-a618-c9c946273aa2">

### Wave Webaim - accessibility testing
You can test your site for accessibility through the wave.webaim site - it needs to be deployed in order for it to test it. Fix any errors that it gives

### Manual Testing

- ### On the home page
- <img width="1703" alt="Screenshot 2024-10-11 at 01 08 05" src="https://github.com/user-attachments/assets/fd0422a8-e487-4d77-8ee3-8e6f99cce32b">
- A transparent background has been created on top of the background image, so it can provide a great contrast to see what is written on it.
- On the home page, a brief introduction is seen and number to call the restaurant on. Also, an email address that links directly to the restaurants email address as seen below.
<img width="1701" alt="Screenshot 2024-10-11 at 01 32 37" src="https://github.com/user-attachments/assets/47834070-34ec-448a-85f3-6ff458ad50bb">


- ### On the booking page
- In the middle of the home page, there is a link leading to the booking page which says 'BOOK A TABLE NOW'. Assuming a user is not logged in, when it is clicked it shows the page but does not show the booking form and says 'log in to make a booking' like the image below.
<img width="1702" alt="Screenshot 2024-10-11 at 01 35 13" src="https://github.com/user-attachments/assets/baa00319-5166-4913-8c21-28589f7bff54">

- If the user is logged in, it shows the booking form for users to make their bookings.
<img width="1707" alt="Screenshot 2024-10-11 at 01 38 45" src="https://github.com/user-attachments/assets/f9012591-afe5-433f-8557-68577fb9a686">

- If the form is not filled in correctly and the date has not been put in it says to fill in the date as the date is a required feild. 
<img width="1710" alt="Screenshot 2024-10-11 at 13 38 25" src="https://github.com/user-attachments/assets/e42e8397-d07a-4b38-8e7a-2f175f22277a"> 

-After a booking has been made, it displays a message that says booking has been made successfully and redirects to the home page as seen below.
<img width="1700" alt="Screenshot 2024-10-11 at 01 43 56" src="https://github.com/user-attachments/assets/fff55a6c-2c45-4b93-958e-29bcd2088eb0">

- The booking logic has been designed in the function to check for available tables before making a booking, as the booking only accomodates one couple or only one person so a table can only be available at a time. If the time the user is picking is not available, it says table is already reserved as seen below.
<img width="1710" alt="Screenshot 2024-10-11 at 02 04 33" src="https://github.com/user-attachments/assets/1c7d0535-6844-44d0-a9ca-f7961633de73">

- The link on the booking page which says 'view booking' if they already have a booking, when that is clicked, it shows a detail of all the bookings that customer has made.
<img width="1707" alt="Screenshot 2024-10-11 at 02 13 39" src="https://github.com/user-attachments/assets/533dad49-0551-4805-9ce4-671a65e039b9">

- When the booking user views their bookings, they have the option to either edit or cancel their bookings.

- If the user chooses to edit the booking, example of a booking is shown below:
<img width="1709" alt="Screenshot 2024-10-11 at 02 28 27" src="https://github.com/user-attachments/assets/46f175c6-2073-4b5c-8ae3-954bcf89ba14">

- If user chooses to edit this booking, it takes them to the booking form and creates an instance of the booking in the form so the form is already prepopulated with the old details like the image below:
<img width="1705" alt="Screenshot 2024-10-11 at 02 31 45" src="https://github.com/user-attachments/assets/29544960-6bf1-4142-b607-7abe882d3c83">

- Once booking has been updated, it directs to the home page and displays a success message. As seen below:
<img width="1706" alt="Screenshot 2024-10-11 at 02 36 04" src="https://github.com/user-attachments/assets/7af8d389-ff7c-450c-84a8-70537a011d8c">

- A function to only make changes to bookings have been implemented and it will not allow users to make changes to bookings 72 hours before booking date.
<img width="1709" alt="Screenshot 2024-10-11 at 02 34 34" src="https://github.com/user-attachments/assets/b9b6cfb1-9592-43cb-88e1-b74a995709bf">

- If the user chooses to cancel their booking, It asks them if they are sure about deleting their booking as shown in the mage below:
<img width="1703" alt="Screenshot 2024-10-11 at 02 18 40" src="https://github.com/user-attachments/assets/9a571940-05c4-4759-80c1-2b92add58982">

- If the user clicks on yes, it deletes the booking from the database and shows a success message, as seen below: The user had 3 booking now there are just 2.
<img width="1708" alt="Screenshot 2024-10-11 at 02 21 16" src="https://github.com/user-attachments/assets/7abad95e-3426-47ac-8dde-f947c12a8ebb">

- However, if the user does not have any booking, it displays a message that says 'You do not have any bookings. Please complete the form to make bookings' and displays the booking form. Image shown below.
<img width="1707" alt="Screenshot 2024-10-11 at 02 23 50" src="https://github.com/user-attachments/assets/1f0a944a-49c9-44f1-9b3b-0756add2b198">


- ### On the review page
- On the bottom right of the home page, there is a link to the reviews page that says 'Read all {{ review_count }} reviews', (this updates depending on how many reviews the restaurant has. ) ' Once this link is clicked it shows all the reviews the restaurant has. As seen below:
<img width="563" alt="Screenshot 2024-10-11 at 12 40 09" src="https://github.com/user-attachments/assets/f2b59b9a-ae55-4add-8f3f-816fcb5da472">

- When the link is clicked, it takes us to the page read all the reviews.
<img width="1704" alt="Screenshot 2024-10-11 at 12 48 39" src="https://github.com/user-attachments/assets/7c0239a7-5835-42b7-ac17-41b94b29796d">

- To create reviews, user will click on 'write reviews' and it will take them to the review form page. as seen below.
<img width="1707" alt="Screenshot 2024-10-11 at 23 07 51" src="https://github.com/user-attachments/assets/7ba58bd6-41d6-4fd0-9a12-21473f7a7879">

- After review has been created, it sends a success message. saying 'review created'
<img width="1710" alt="Screenshot 2024-10-11 at 23 08 22" src="https://github.com/user-attachments/assets/a2cd4c02-7008-4ea6-83c8-a150ae9512f4">

-And the review is updated to the database.
<img width="1706" alt="Screenshot 2024-10-11 at 23 08 39" src="https://github.com/user-attachments/assets/9c2a5367-1d21-4928-a70d-461ea4e41af0">


-  As it can be seen from the image below, users who have not written a review cannot edit or delete other people's review.
<img width="1704" alt="Screenshot 2024-10-11 at 12 48 39" src="https://github.com/user-attachments/assets/7c0239a7-5835-42b7-ac17-41b94b29796d">
- In the picture below, a review has been made by the currently logged in user, which bring the number of reviews to 4. And it has the option to edit or delete the review. Now cuppystaff is logged in and cuppystaff can now make changes to their reviews.
<img width="1710" alt="Screenshot 2024-10-11 at 12 54 48" src="https://github.com/user-attachments/assets/1a24884f-355c-43ef-ad4f-18f5d7095e89">

- If they click on edit button, It takes them to the review form and the body of the form is already pre-populated by the previous review the user wrote.As seen below.
<img width="1701" alt="Screenshot 2024-10-11 at 12 57 53" src="https://github.com/user-attachments/assets/9a7d0467-f103-41cd-abb8-17ddfa876570">

-After the review has been edited, It sends a success message as seen below.
<img width="1709" alt="Screenshot 2024-10-11 at 12 58 34" src="https://github.com/user-attachments/assets/1d29da57-d2c6-4e4d-b97a-b28392a37a07">

- And when I view the review, the new content have been added to it.
<img width="1706" alt="Screenshot 2024-10-11 at 12 59 01" src="https://github.com/user-attachments/assets/52efff45-f91b-4190-ad20-551681732df6">

- If the user chooses to delete their review, It asks them if they want to delete the review with a Modal.
<img width="1689" alt="Screenshot 2024-10-11 at 13 03 07" src="https://github.com/user-attachments/assets/fa9b81af-d2b7-41f0-af3a-62f1e97d95ec">

- If they click on close, it takes them back to the review page. However, if they click on yes, their review is immediately deleted from the database. And it can be seen from the picture that the number of reviews is now back to 3.
<img width="1707" alt="Screenshot 2024-10-11 at 13 05 52" src="https://github.com/user-attachments/assets/b1471eb9-cab8-4e60-b7cc-9a407f64ad9e">

- If I go back to the reviews page, the review is no longer there.
<img width="1710" alt="Screenshot 2024-10-11 at 13 08 33" src="https://github.com/user-attachments/assets/648f5360-f421-407a-a50f-d8eda6e0c5f4">

- ### On the register page
- Users can create an account by clicking on the Register text in the nav bar, which takes them to the register page as seen below.
<img width="1708" alt="Screenshot 2024-10-11 at 23 16 46" src="https://github.com/user-attachments/assets/c17a730f-c567-4ecc-8d6a-8e95729420ed">

- After they have signed up, an email verification link is sent to their email address for them to verify their email account as shown below.
<img width="1707" alt="Screenshot 2024-10-11 at 23 24 01" src="https://github.com/user-attachments/assets/01f243da-36e9-4467-aa24-f39fe833adf0">

-An email that was received from the restaurant app is seen in the screenshot below.
<img width="1271" alt="Screenshot 2024-10-11 at 23 24 17" src="https://github.com/user-attachments/assets/cfde29d8-e0e7-484d-b1ee-adb7d0de247b">

- After ther user clicks on the link sent to their email, it redirects them to the confirm email page.
<img width="1186" alt="Screenshot 2024-10-11 at 23 31 11" src="https://github.com/user-attachments/assets/5bbab981-711c-4eeb-b269-acef5cd8d660">

-After confirmation, it takes them to the sign in page now. And sends a success messgae as seen below:
<img width="1705" alt="Screenshot 2024-10-11 at 23 31 29" src="https://github.com/user-attachments/assets/5e7c0b1b-ff76-40d5-957b-eb7a7b8dd479">

- After the user can click on sign in and the user is successfully signed in then it sends a success message.
<img width="1710" alt="Screenshot 2024-10-11 at 23 32 29" src="https://github.com/user-attachments/assets/c6a200fc-ccd5-402f-a1ae-e3da81bb41fa">

- ### On the Log in page 
- Users who already registered an account can log into their account.The log in page has been set to extend base.html and it looks like this now.
<img width="1710" alt="Screenshot 2024-10-11 at 03 13 55" src="https://github.com/user-attachments/assets/401beb75-5314-4638-abfa-fa65af8590b6">

- ### On the log out page
- Users who have been logged in can log out of their account whenever they want.The log out page has been set to extend base.html and it looks like this now.
<img width="1706" alt="Screenshot 2024-10-11 at 01 15 57" src="https://github.com/user-attachments/assets/16db7529-d6dc-47a1-bc2b-9b46b62ad91b">
- And when the user signs out, It sends a success message that says 'You've been signed out'.

- ### Forgot password page
- Users can reset their password if they have forgotten it.
- On the sign in page, there is a link that says 'Forgot password?'
<img width="1709" alt="Screenshot 2024-10-11 at 23 39 34" src="https://github.com/user-attachments/assets/64c7cca6-f6fd-4d2f-8610-f040aac8a0cc">

- If user clicks on it, it takes them to the reset password page, here they can put in their email address so they can be sent an email.
<img width="1710" alt="Screenshot 2024-10-11 at 23 39 46" src="https://github.com/user-attachments/assets/c42b926b-09fb-418d-9178-43c041f822bd">

- After that, it confirms that an email has been sent.
<img width="1710" alt="Screenshot 2024-10-11 at 23 40 04" src="https://github.com/user-attachments/assets/342be8c3-ee73-4eab-81c7-7eb9eedae6df">

- Email that was sent it seen below.
<img width="1269" alt="Screenshot 2024-10-11 at 23 40 20" src="https://github.com/user-attachments/assets/20d7bf94-f344-4864-add2-783be64f78c4">

- Then I can change my password.
<img width="1710" alt="Screenshot 2024-10-11 at 23 40 59" src="https://github.com/user-attachments/assets/3ee17800-781a-47df-9490-1999fdb641b7">

- After, it sends a success message that my password has been changed successfully
<img width="1706" alt="Screenshot 2024-10-11 at 23 41 17" src="https://github.com/user-attachments/assets/8b445b29-ece5-409a-91b5-26af465b88ba">

- ### Footer
<img width="1703" alt="Screenshot 2024-10-11 at 03 17 30" src="https://github.com/user-attachments/assets/0d80efab-e5ec-403e-b943-d6ed2a07180e">
- The footer contains a block copyright of 'Cuppy's Restaurant'.
- It also contains links to facebook, instagram, twitter and youtube which are social media and they are working as seen in the pictures below.
<img width="1701" alt="Screenshot 2024-10-11 at 03 29 48" src="https://github.com/user-attachments/assets/ae5ad45c-291d-47ba-add4-d2e46b02fb2d">
<img width="1708" alt="Screenshot 2024-10-11 at 03 30 22" src="https://github.com/user-attachments/assets/9a9266b9-f5c6-4f23-8bca-a71fdb430a00">
<img width="1708" alt="Screenshot 2024-10-11 at 03 30 40" src="https://github.com/user-attachments/assets/1128bf40-3d5a-4249-9e7d-43cd7f0c452d">
<img width="1708" alt="Screenshot 2024-10-11 at 03 30 54" src="https://github.com/user-attachments/assets/bf7e90e2-8e0e-4fbd-b119-0b7b6ee508aa">

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
- https://djangoproject.com
- Lighthouse on google chrome
- Chrome dev tools
- https://ui.dev/amiresponsive

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