#near-dublin app#

This app reads a list of cities around the world and outputs the names of those that are 500km or less from Dublin City
(coords: 53.333, -6.267).

Note that due to the purpose of this app, and in order to avoid over-engineering, exceptions are not thrown when a
problem is found (in format or anything) and None is returned instead.