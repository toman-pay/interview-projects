## Junior Backend Developer Project Definition

### Goals
This project is meant to give us a rough idea about how much you are technically experienced and also show you what is the general type of tasks we do in Toman.

### Process
1. Read this file through and make sure you know what is the task at hand
1. [Fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) from this one and start implementing the task
1. [Submit a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to this repository when you're done
1. We will review your pull request and estimate whether or not we can use your expertise in Toman
1. We will send you an email informing you about the result of our estimation

### Metrics
We are mostly looking to find out **how** you work, rather than the result itself. So even though a functional result is important, the way it works and looks might be even more so.

We will be looking for things like this in your code:

- Code structure, formatting, and readability
- Applying common code conventions
- Usage of useful patterns
- Overall performance and reliability
- Extensibility

### Project
We want to implement a part of an [escrow account](https://en.wikipedia.org/wiki/Escrow) product. The page we are interested in is the product definition page.
For a better idea of what we're looking for, take a look at the following screenshot of the said page.

<img src="https://github.com/toman-pay/interview-projects/raw/main/backend-junior.png" width="223" height="400">

What we ultimately need is a REST endpoint that enables our front-end client to send a request to submit a product description to our servers. The submitted product should be stored in the database. The response to the request should be the success status and a follow-up ID if the submission was successful.
Here's an example of such a response, but you can change it if you wish:
```json
{
  "success": true,
  "id": 123
}
```

### Requirements

- You **don't** need to render any HTML whatsoever, we only want a REST API
- Providing an API Doc for the implemented endpoint is **optional** but we'd love to have one
- User authentication and authorization are **optional** but you can implement one if you felt like it
- All of the fields should be required
- The price should be a positive number
- Setting up Django Admin for this project is **optional**
- You can choose any DBMS that Django supports as your database backend
- The exact field names in the request body are **not** important, they just need to be readable
