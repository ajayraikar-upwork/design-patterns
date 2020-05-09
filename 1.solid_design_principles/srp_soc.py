# SRP (Single Responsiblity Principle) or SOC (Seperation of Concerns)
'''
* A class should only have one reason to change
* Seperation of concerns - different classes handling different, independent tasks/problems
'''

class Journal:
    def __init__(self):
        self.enteries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.enteries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.enteries[pos]

    def __str__(self):
        return '\n'.join(self.enteries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass

class PersistanceManager:

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()
j.add_entry('I read a book today, Neuromencer')
j.add_entry('I read a blog today')
print(f'Journal entries:\n{j}')


file = r'C:\temp\journal.txt'
PersistanceManager.save_to_file(j, file)

with open(file) as fh:
    print(fh.read())