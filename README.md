## Application Design: Newsletter RAG GenAI Application

### HTML Files

- **index.html**: The landing page of the application. It should display an input field for the user to enter their email address and a button to submit the address.
- **success.html**: A confirmation page displayed after the user successfully submits their email. It can contain a message thanking the user for subscribing and provide links to follow the newsletter on social media.

### Routes

- **home**: The root route that renders the `index.html` file.
- **subscribe**: A POST route that handles the submission of the user's email address. It processes the email address for validation and stores it in a database or email marketing platform. It then redirects the user to the `success.html` page.