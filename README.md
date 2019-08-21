# Victor's flow
Small CI/CD tool i use locally to automatically build, push, copy, update and delete files.

## Instructions

  1) Update config.js with production properties
  2) Commit & Push front-end
  3) Build react app
  4) Revert config.js for local development
  5) Move build to static folder of back-end
  6) Update application.yml with prodaction properties
  7) Commit & Push back-end
  8) Revert application.yml for local development
  
### Repositories
* [stefantflc.me](https://github.com/ToStefan/stefantflc.me) - Back-end (Java Spring Boot app)
* [stefantlfc-react](https://github.com/ToStefan/stefantflc-react) - Front-end (React app)