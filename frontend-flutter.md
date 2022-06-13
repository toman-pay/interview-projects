## Flutter Developer Project Definition

### Goals
This project is meant to give us a rough idea about how much you are technically experienced and also show you what is the general type of tasks we do in Toman.

### Process
1. Read this file through and make sure you know what is the task at hand
1. [Fork a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) from this one and start implementing the task
1. [Submit a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) to this repository when you're done
1. We will review your pull request and estimate whether we can use your expertise in Toman
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

<img src="https://github.com/toman-pay/interview-projects/raw/main/frontend-flutter.png" width="223" height="400">

What we ultimately need is a page to submit a product description to our servers.
The design page can be found in [this Figma project](https://www.figma.com/file/jniwhCb5f7VEVQGrOkLOMe/Frontend-Project?node-id=0%3A1).

API documentation can be found at this [ReDoc page](https://redocly.github.io/redoc/?url=https://raw.githubusercontent.com/toman-pay/interview-projects/main/front-api-specification.json).
The referenced [server](https://run.mocky.io/v3/d1055cef-c469-49ed-835f-3a55d06f86f1) in the documentation is not an actual server and doesn't validate the requests, it always returns HTTP 204 response.

### Requirements

- When user clicks on the "شرایط و قوانین" link, the bottom sheet in the second page (Basic info - EULA) should appear
- Clicking on "شرایط و قوانین را می‌پذیرم" should mark the checkbox on the main page
- Clicking "تایید" should send the request described in the documentation
- We don't want the result to be pixel perfect, but the closer, the better
- Adding validation to input fields is **optional**, but if you felt like it you can make the price to always be a positive number
- The "تایید" button should be in disabled state until user activates the "شرایط و قوانین را می‌پذیرم" checkbox
