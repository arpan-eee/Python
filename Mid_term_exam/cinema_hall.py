# This code is for a cinema complex where there are multiple halls. 
# Shows for different halls are also different 

class StarCinema:
    __hall_list = []

    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        self.__hall_list.append(hall)

class Show:
    def __init__(self, show_id, movie_name, time, row, column) -> None:
        self.show_id = show_id
        self.movie_name = movie_name
        self.time = time
        self.row = row
        self.column = column
        self._seats = [[0] * self.column for _ in range(self.row)]

class Hall(StarCinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._show_list = []
        self._show_to_row = {}

    def entry_show(self, show_id, movie_name, time):
        show = Show(show_id, movie_name, time, self._rows, self._cols)
        self._show_list.append(show)
        self._show_to_row[show_id] = len(self._show_list) - 1

    def book_seats(self, show_id, seat):
        if show_id not in [show.show_id for show in self._show_list]:
            print("Invalid show ID")
        else:
            row_index = self._show_to_row[show_id]
            show = self._show_list[row_index]
            if seat[0] > self._rows or seat[0] < 1 or seat[1] > self._cols or seat[1] < 1:
                print("Invalid Seat")
            elif show._seats[seat[0] - 1][seat[1] - 1] == 1:
                print("Seat Already Booked")
            else:
                show._seats[seat[0] - 1][seat[1] - 1] = 1
                print("Seat Booked")

    def view_available_seats(self, show_id):
        if show_id not in [show.show_id for show in self._show_list]:
            print(f"Invalid show ID: {show_id}")
        else:
            row_index = self._show_to_row[show_id]
            show = self._show_list[row_index]
            available_seats = [(row + 1, col + 1) for row in range(self._rows) for col in range(self._cols) if
                                show._seats[row][col] == 0]

            print(f"Available seats for Show ID {show_id}: {available_seats}")

    def view_all_shows(self):
        for show in self._show_list:
            print(f'Movie Name: {show.movie_name} || Show Id: {show.show_id} || Time: {show.time}')


general = Hall(rows=12, cols=12, hall_no=101)

general.entry_show(show_id='S1', movie_name='Super Man', time='9:00 AM')
general.entry_show(show_id='S2', movie_name='Spider Man', time='12:00 PM')
general.entry_show(show_id='S3', movie_name='Hulk', time='3:00 PM')
general.entry_show(show_id='S4', movie_name='Iron Man', time='6:00 PM')

general.book_seats(show_id='S1', seat=(1, 1))
general.book_seats(show_id='S2', seat=(5, 5))
general.book_seats(show_id='S3', seat=(3, 3))
general.book_seats(show_id='S4', seat=(6, 2))
general.view_available_seats(show_id='S1')
general.view_available_seats(show_id='S2')
general.view_available_seats(show_id='S3')
general.view_available_seats(show_id='S4')

special = Hall(rows=3, cols=3, hall_no=102)

special.entry_show(show_id='S1', movie_name='Captain America', time='3:00 PM')
special.entry_show(show_id='S2', movie_name='Thor', time='4:00 PM')

special.book_seats(show_id='S1', seat=(2, 1))
special.book_seats(show_id='S2', seat=(2, 2))
special.view_available_seats(show_id='S1')
special.view_available_seats(show_id='S2')

general.view_all_shows()


