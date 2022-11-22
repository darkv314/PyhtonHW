from src.duration import Duration


class Participant:
    
    def __init__(self, full_name: str, join_time: str, leave_time: str,
    in_meeting_duration: Duration, email: str, role: str, id: str):
        self.full_name = full_name
        self.join_time = join_time
        self.leave_time = leave_time
        self.in_meeting_duration = in_meeting_duration
        self.email = email
        self.role = role
        self.id = id
        self.name = None
        self.middle_name = None
        self.first_surname = None
        self.second_surname = None
        full_name_list = full_name.split()
        if len(full_name_list) == 4:
            self.name, self.middle_name, self.first_surname, self.second_surname = full_name_list
        elif len(full_name_list) == 3:
            self.name, self.first_surname, self.second_surname = full_name_list
        elif len(full_name_list) == 2:
            self.name, self.first_surname = full_name_list
        else:
            self.name = full_name