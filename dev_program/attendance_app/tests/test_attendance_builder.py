from src.attendance_builder import build_attendance_object


def test_build_attendance_object():
    raw_attendance = {
        'Title': 'General',
        'Id': '220492dd-c020-49b9-bb1c-64b665217a8d',
        'Attended participants': 7,
        'Start Time': '10/18/22, 5:49:42 PM',
        'End Time': '10/18/22, 7:53:52 PM',
        'Duration': {
            'hours': 2,
            'minutes': 4,
            'seconds': 10
        },
        'Participants': [
            {
                'Full Name': 'Santiago Martinez Saavedra',
                'Join time': '10/18/22, 7:49:42 PM',
                'Leave time': '10/18/22, 7:53:52 PM',	
                'Duration': {
                    'Hours': 0,
                    'Minutes': 6,
                    'Seconds': 26
                },	
                'Email': 'Santiago.Martinez@fundacion-jala.org',
                'Role': 'Presenter',
                'Participant ID (UPN)': 'Santiago.Martinez@fundacion-jala.org'
            },
            {
                'Full Name': 'Random Random Random',
                'Join time': '10/18/22, 5:49:42 PM',
                'Leave time': '10/18/22, 7:50:52 PM',	
                'Duration': {
                    'Hours': 1,
                    'Minutes': 46,
                    'Seconds': 26
                },	
                'Email': 'randomname.randomlastname@fundacion-jala.org',
                'Role': 'Presenter',
                'Participant ID (UPN)': 'randomname.randomlastname@fundacion-jala.org'
            }
        ]
    }

    attendance = build_attendance_object(raw_attendance)
    assert attendance is not None
    assert type(attendance) is Attendance
    assert attendance.start_datetime == raw_attendance['Start Time']

    ## assert summary object
    assert attendance.summary is not None
    assert type(attendance.summary) is Summary
    assert attendance.summary.title == raw_attendance['Title']
    assert attendance.summary.id == raw_attendance['Id']
    assert attendance.summary.attended_participants == raw_attendance['Attended participants']
    assert attendance.summary.start_time == raw_attendance['Start Time']
    assert attendance.summary.end_time == raw_attendance['End Time']
    assert attendance.summary.duration.hours == raw_attendance['Duration']['hours']
    assert attendance.summary.duration.minutes == raw_attendance['Duration']['minutes']
    assert attendance.summary.duration.seconds == raw_attendance['Duration']['seconds']

    ## assert participant object
    assert type(attendance.participants) is not None
    assert type(attendance.participants) is list
    assert len(attendance.participants) == len(raw_attendance['Participants'])
    assert all(type(participant) is Participant for participant in attendance.participants)
    assert len(attendance.participants) == 2, "expected 2 participants"

    