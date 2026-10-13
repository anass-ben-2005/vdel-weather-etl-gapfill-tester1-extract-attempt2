# ASSIGNMENT
Project: `weather_etl` -- attempt 2

## `weather_etl/extract.py` line 14 (`g_ext_retry`)

Loop over attempt numbers from 1 to MAX_ATTEMPTS inclusive. Each attempt: issue a GET request with params and a 10-second timeout, raise on a bad HTTP status, and return the JSON body on success. On the final attempt, let the exception propagate instead of retrying.

## About the automatic feedback and the AI notes

Each time you push, a program runs the course's hidden checks on your code and a note on your
feedback issue lists the checks that failed, by name and error type. That part does not use AI.

If your instructor has switched on AI notes, two more things can happen, and **text is then sent
to an external AI service provider** (the company that runs the language model):

- **When a check fails**, for the paragraph under the note, the service receives: the exercise
  and attempt, the names and error types of the failing checks, a short description of what each
  check expects, how many pushes each has failed on, a number per related topic summarising how
  you have done so far, and **the lines of your own code that you wrote inside the marked gaps,
  with three lines of context**.

- **Once, when all checks pass**, for a review the instructor reads (it is not shown to you),
  the service receives those same lines of your code, the exercise text and the same topic
  numbers.

It does **not** receive your name, your e-mail address, your GitHub username, the code of the
hidden tests, or any file or line outside the gaps and their three lines of context. The
provider's own terms apply to what it receives. The checks, not the AI, decide whether your code
is correct.

**To opt out**, tell your instructor. They switch AI notes off for you with one line in their
settings: you keep the hidden checks and the note listing the failed checks, and nothing else
changes.
