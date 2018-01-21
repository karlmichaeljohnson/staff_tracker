# staff_tracker
A simple "in-out" CLI tracker for headcount or fire emergencies.

## Setup
1. Create a JSON file with the names and email addresses of staff, following the format of `staff_example.json`. *Note:* the interface splits name and status strings on spaces, so use underscores instead of spaces in names.
2. Change line 40 in `build_db.py` to point to your new file.
3. Run `build_db.py`, which will create a database in the same directory as your application called `staff_tracker.db`.

## Usage
`staff_tracker.py` runs like a REPL, printing a new prompt after each input until `exit` or `done` is entered.

### Roll Call
Use the command `roll call` to see who is marked in and out.

### All In, All Out
Use the command `all in` to mark all staff in the database as in. Likewise, use `all out` to mark everyone out.

### Staffers
To mark an individual staffer in or out, use the schema `[name] [in/out]` to specify their status. Note that the tracker splits on spaces, so use underscores when setting up staff names instead of spaces.
