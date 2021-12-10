# A simple FastAPI/Plotly/Heroku app

I followed the [Getting started on Heroku with Python tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) to create this app.

I then replaced the Django app with a FastAPI/Plotly app. The app provides a simple interface for investigating the [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture).

I believe that one should be able to more-or-less follow the above-linked Heroku tutorial, but cloning this repository in place of the [python-getting-started](https://github.com/heroku/python-getting-started) repository during the [Prepare the app](https://devcenter.heroku.com/articles/getting-started-with-python#prepare-the-app) stage.

## References

- [This repository on GitLab](https://gitlab.com/bmares/heroku-fastapi-plotly-demo)
- [This repository on GitHub](https://github.com/maresb/heroku-fastapi-plotly-demo)
- [Collatz conjecture Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [Getting started on Heroku with Python tutorial](https://devcenter.heroku.com/articles/getting-started-with-python)

## Sample endpoints

- [collatz.tensorial.com](http://collatz.tensorial.com/)
- [example Collatz sequence](http://collatz.tensorial.com/collatz/sequence/127)
- [example plot of multiple sequences](http://collatz.tensorial.com/collatz/graph/109328502982093486,209328502982093486,309328502982093486)

## Pricing considerations

Everything works great on the free tier, except that you can't use HTTPS. (Consequently, web traffic is unencrypted, and search results are penalized.) For HTTPS, one must upgrade to the next tier ("Hobby"), which is currently $7/month.
