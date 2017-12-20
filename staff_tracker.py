"""Track when staff are in and out of the office."""

import os
import sqlite3

from all_actions import all_in, all_out
from roll_call import roll_call
from update_staff import update_staff


def main():
    """Run the application."""
    conn = sqlite3.connect('staff_tracker.db')
    cur = conn.cursor()
    cur.execute("""
        PRAGMA foreign_keys = ON;
        """)
    conn.commit()

    os.system('cls' if os.name == 'nt' else 'clear')
    print('{:=^79s}'.format('Staff Tracker 0.0'))

    session_complete = False

    while not session_complete:
        action = input('> ')

        if action.startswith('end') or action == 'exit' or action == 'done':
            session_complete = True
        elif action == 'roll call':
            roll_call(conn, cur)
        elif action == 'all in':
            all_in(conn, cur)
            print('All staff marked as \'in\'.')
            print()
        elif action == 'all out':
            all_out(conn, cur)
            print('All staff marked as \'out\'.')
            print()
        else:
            name, status = action.split(' ')
            update_staff(conn, cur, name, status)

    conn.close()
    print('Done.')


if __name__ == '__main__':
    main()
