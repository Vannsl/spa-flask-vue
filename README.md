# spa-flask-vue
A Fullstack application with Python/Flask Backend and Vue Frontend. The frontend, a Single Page Application using the Vue-Router, requests a FAQ list from the server. This setup uses virtualenv. If you want to use Docker, go ahead!

# Development
1. Install the Frontend packages (see Frontend Build Setup below)
2. Enable your virtual environment run (see Backend Setup below)
2. To Run in Dev Mode: Run `cd frontend && npm run dev` and `FLASK_APP=run.py FLASK_DEBUG=1 flask run` (in the root directory).

# Backend

## Setup

```bash
mkdir backend && cd backend
virtualenv -p python3 venv
source venv/bin/activate
pip install Flask
pip install requests
pip install -U flask-cors
```

# Frontend

## Build Setup

``` bash
cd frontend

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
