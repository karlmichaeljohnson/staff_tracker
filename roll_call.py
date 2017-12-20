"""Report on headcoung and current staff in."""


def roll_call(conn, cur):
    """Print staff in and headcount."""
    cur.execute("""
        SELECT name
        FROM staffers
        WHERE in_office = 1
        ORDER BY name ASC;
        """)
    staffers_in_results = cur.fetchall()
    staffers_in = [s[0].capitalize() for s in staffers_in_results]
    headcount = len(staffers_in)

    cur.execute("""
        SELECT name
        FROM staffers
        WHERE in_office = 0
        ORDER BY name ASC;
        """)
    staffers_out_results = cur.fetchall()
    staffers_out = [s[0].capitalize() for s in staffers_out_results]
    # absent_count = len(staffers_out)

    if staffers_in:
        print('Staffers currently in the office:')
        counter = 1
        for staffer in staffers_in:
            print(str(counter) + '. ' + staffer)
            counter += 1
        print()
    if staffers_out:
        print('Staffers currently out of the office:')
        counter = 1
        for staffer in staffers_out:
            print(str(counter) + '. ' + staffer)
            counter += 1
        print()
    print('Current headcount: ' + str(headcount))
    print()
