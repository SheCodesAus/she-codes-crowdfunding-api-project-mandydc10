# Communitarian

This website is a crowdfunding website for public health and community-driven health initiatives

The main users of this site will be community and council members, and health professionals wanting to improve health measures in their local area, but are unable to gather the funds and support necessary to implement their public health projects.

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Goal Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy - maybe this shouldn't be allowed (haven't thought through yet)
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update - I do not want donations to be editable
  - [ ] Destroy - I do not want donations to be removed
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy - not sure if this should be an option yet

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create - Must be signed up and logged in
  - [ ] Limit who can retrieve - Anyone
  - [X] Limit who can update - Must be signed up and owner
  - [X] Limit who can delete - Must be signed in
- Pledge
  - [X] Limit who can create - Must be signed up and logged in
  - [X] Limit who can retrieve - Anyone can retrieve, but anonymous pledges will not show supporter names
  - [ ] Limit who can update - I do not want donations to be editable
  - [ ] Limit who can delete - I do not want donations to be removed
- User
  - [ ] Limit who can retrieve - I do not need this restricted
  - [X] Limit who can update - Must be logged in as specific User
  - [ ] Limit who can delete

### Implement relevant status codes

- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404

### Handle failed requests gracefully 

- [X] 404 response returns JSON rather than text

### Use token authentication

- [X] implement /api-token-auth/

## Additional features

- [ ] {Title Feature 1}

{{ description of feature 1 }}

- [ ] {Title Feature 2}

{{ description of feature 2 }}

- [ ] {Title Feature 3}

{{ description of feature 3 }}

### External libraries used

- [X] django-filter


## Part A Submission
**See files in github repository "docs" folder
- [x] A link to the deployed project. https://rough-sun-6905.fly.dev/projects/
- [x] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.**
- [x] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.**
- [x] A screenshot of Insomnia, demonstrating a token being returned.**
- [x] Your refined API specification and Database Schema.**

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser1",
	"email": "test@testuser.com"
}'
```

2. Sign in User

```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Authorization: Bearer undefined' \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser1",
	"password": "testingkitty"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token c058b5f7b952dcfd60b92cc97660c6935df4bf26' \
  --header 'Content-Type: application/json' \
  --data '	{
		"title": "Natural Playground",
		"description": "Help us build a playground using nature, educational and mentally stimulating for the local children",
		"goal": 2000,
		"image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fcivicwell.org%2Fcivic-resources%2Fcultivating-community-gardens%2F&psig=AOvVaw0pGpvR3rXms6ixIyGwfRbi&ust=1674810770679000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCJDFybry5PwCFQAAAAAdAAAAABAE",
		"is_open": true,
		"date_created": "2023-01-21T02:31:05.805000Z"
	}'
```