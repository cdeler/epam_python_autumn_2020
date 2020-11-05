I wrote some program that uses existing logger class that was provided by my client (task04.py).

Some time passed and now i need to use another logger class that writes output to file as well (from not_so_simple_logger module).

I tried doing this::

   import lib.not_so_simple_logger
   import lib.database
   db = lib.database.DatabaseClient(logger_cls=lib.not_so_simple_logger.Logger)

but it gives me an error::
   TypeError: __init__() missing 1 required positional argument: 'filename'

Make new logger and database client work together. Use functional style whenevr possible.
