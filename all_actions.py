"""Set all staff in or out."""

from datetime import datetime
from uuid import uuid4


def all_in(conn, cur):
    """Set all staffers in."""
    cur.execute("""
        SELECT id from staffers;
        """)
    staffers = cur.fetchall()
    staff_list = [s[0] for s in staffers]
    count = len(staff_list)

    temp = list(zip([now()] * count, staff_list))
    cur.executemany("""
        UPDATE staffers
        SET in_office = 1, updated = ?
        WHERE id = ?;
        """, temp)

    temp = list(zip(n_uuids(count), staff_list, [now()] * count))
    cur.executemany("""
        INSERT INTO events
            (id, status, staffer_id, created)
        VALUES
            (?, 'in', ?, ?);
        """, temp)
    conn.commit()


def all_out(conn, cur):
    """Set all staffers in."""
    cur.execute("""
        SELECT id from staffers;
        """)
    staffers = cur.fetchall()
    staff_list = [s[0] for s in staffers]
    count = len(staff_list)

    temp = list(zip([now()] * count, staff_list))
    cur.executemany("""
        UPDATE staffers
        SET in_office = 0, updated = ?
        WHERE id = ?;
        """, temp)

    temp = list(zip(n_uuids(count), staff_list, [now()] * count))
    cur.executemany("""
        INSERT INTO events
            (id, status, staffer_id, created)
        VALUES
            (?, 'out', ?, ?)
        """, temp)
    conn.commit()


def now():
    """Return current timestamp as ISO 8601 string."""
    return datetime.now().isoformat()


def n_uuids(n):
    """Return a list of uuids given a quantity."""
    list_of_uuids = []
    for i in range(n):
        temp = uuid4().hex
        list_of_uuids.append(temp)
    return list_of_uuids
