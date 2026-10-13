# Intentionally empty of code.
#
# Its presence is the point: pytest adds this directory (the repo root) to sys.path when it
# finds a conftest.py here, which is what lets `pytest tests/visible` import the
# `weather_etl` package. Please leave it in place.
