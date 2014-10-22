# teachdb - Simple module to ease fetching data from DoC TeachDB

- Initialise with your username as a parameter.
- Your password should be in the *IC_PASS* environment variable.

---

## Functions

### fetch_from_teachdb(self, table, **kwargs)
**Parameters:**
- *table*: The name of the table (e.g. 'Student')
- *kwargs*: Look in the *params* table to see what kwargs are supported.

**Returns:**
A list of dicts, each containing the info from a data row on TeachDB.

## get_all_students_from_year(self, year)
**Parameters**:
- *year*: The year to look up, e.g. 1, 2...

**Returns**:
A list of dicts of all the students in the given year.
