class student:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return 'There is no such user'
        else:
            return self.name[user_id]


if __name__ == '__main__':
    student = student()
    print('User Alon has been added with id ', student.set_name('Alon'))
    print('User associated with id 0 is ', student.get_name(0))
