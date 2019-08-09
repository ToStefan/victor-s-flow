# Victor's flow
Small CI/CD tool i use locally to automatically build, push, copy build, update and delete files.

## Instructions

  1) Update config.js with production properties
  2) Commit & Push front-end (React app)
  3) Build react app
  4) Revert config.js for local development
  5) Delete content of static folder inside back-end (Java Spring Boot app)
  6) Copy build content in static folder of back-end
  7) Delete content of build folder
  8) Update application.yml with prodaction properties
  9) Update Constants.java with production properties
  10) Commit & Push back-end
  11) Revert application.yml for local development
  12) Revert Constants.java for local development
  
### Repositories
* [stefantflc.me](https://github.com/ToStefan/stefantflc.me) - Back-end (Java Spring Boot app)
* [stefantlfc-react](https://github.com/ToStefan/stefantflc-react) - Front-end (React app)