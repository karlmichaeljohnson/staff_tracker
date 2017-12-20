"""Track when staff are in and out of the office."""

import json
import sqlite3

from datetime import datetime
from uuid import uuid4


def main():
    """Run the application."""
    db = 'staff_tracker.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("""
        PRAGMA foreign_keys = ON;
        """)
    conn.commit()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS staffers (
            id TEXT NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            in_office INTEGER NOT NULL,
            created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updated DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            CONSTRAINT name_email_unique UNIQUE (name, email));
        """)
    conn.commit()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id TEXT NOT NULL PRIMARY KEY,
            status TEXT NOT NULL,
            staffer_id TEXT NOT NULL,
            created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
            FOREIGN KEY (staffer_id) REFERENCES staffers (id));
        """)
    conn.commit()

    with open('staff_example.json', 'r') as in_file:
        staffers = json.load(in_file)

    staffer_l = [(staffer['name'], staffer['email']) for staffer in staffers]

    staff_list = list(
        (uuid4().hex,
            *staffer,
            0,
            now(),
            now())
        for staffer in staffer_l
    )

    cur.executemany("""
        INSERT INTO staffers VALUES (?, ?, ?, ?, ?, ?);
        """, staff_list)
    conn.commit()


def now():
    """Return a string of the current timestamp in ISO 8601 format."""
    return datetime.now().isoformat()


if __name__ == '__main__':
    main()
