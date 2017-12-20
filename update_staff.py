"""Update status for a specific staffer."""

from datetime import datetime
from uuid import uuid4


def update_staff(conn, cur, name, status):
    """Update status for a specific staffer."""
    cur.execute("""
        SELECT id from staffers WHERE name = ?;
        """, (name,))
    staffer_id = cur.fetchone()
    conn.commit()

    if staffer_id:
        staffer_id = staffer_id[0]
    else:
        print('Staffer \'{}\' not found.'.format(name))
        print()
        return

    if status == 'in':
        in_office = 1
    elif status == 'out':
        in_office = 0
    else:
        print('Invalid action.')
        print()
        return

    temp = (in_office, now(), staffer_id)
    cur.execute("""
        UPDATE staffers
        SET in_office = ?, updated = ?
        WHERE id = ?;
        """, temp)

    temp = (uuid4().hex, status, staffer_id, now())
    cur.execute("""
        INSERT INTO events
            (id, status, staffer_id, created)
        VALUES
            (?, ?, ?, ?)
        """, temp)
    conn.commit()
    name_capitalized = name.capitalize()
    print(name_capitalized + ' set to \'{}\'.'.format(status))
    print()


def now():
    """Return the current time in ISO 8601 format."""
    return datetime.now().isoformat()
