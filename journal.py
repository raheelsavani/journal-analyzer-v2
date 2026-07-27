import datetime

class Entry: #this is building the blueprint for the entry object to be used to create new entries
    def __init__(self, content, title = None, mood = None, date = None):
        if date == None:
            self.date = datetime.datetime.now()
        else:
            self.date = date
        self.title = title
        self.mood = mood
        self.content = content

    def view(self): #blueprint to extract previous entries 
        print(self.date)
        if self.title is None or self.title == "":
            print("Title not provided")
        else:
            print(f"Title: {self.title}")
        if self.mood is None or self.mood == "":
            print("Mood not provided")
        else:
            print(f"Mood: {self.mood}")
        print(self.content)

    @classmethod
    def from_line(cls, line):
        stripped = line.strip()
        split = stripped.split("_|_")
        date = split[0]
        title = split[1]
        mood = split[2]
        content = split[3]
        return cls(content, title, mood, date)

def word_count(): #function to get total count of words, called in section 4
    words = 0
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            split = stripped.split()
            words += len(split)
    return words

def longest_line(): #function to get longest entry, called in section 4
    longest = ""
    with open("entries.txt") as file:
        for line in file:
            stripped = line.strip()
            lst = stripped.split()
            final = " ".join(lst)
            if len(final) > len(longest):
                longest = final 
    return longest

print("Welcome to your journal. Enter 1 to Add Entry, 2 to View Entries, 3 to Keyword Search, 4 to Analyze, and 5 to Quit") #welcome message + instructions

try:
    file = open("entries.txt")
    file.close()
except FileNotFoundError:
    file = open("entries.txt", "a")
    file.close()

while True:
    selection = input("Please enter selection.  ").strip()
    if selection == "1": # section for adding entry
        title = input("Enter title: ")
        if title == "":
            title = None
        mood = input(" Enter current mood: ")
        if mood =="":
            mood = None
        content = input("Please type journal entry now: ")
        new_entry = Entry(content, title, mood)
        if new_entry.title == None:
            final_title = ""
        else:
            final_title = new_entry.title
        if new_entry.mood == None:
            final_mood = ""
        else:
            final_mood = new_entry.mood
        timestamp = new_entry.date.strftime("%m/%d/%y  %I:%M %p")
        joined = "_|_".join([timestamp, final_title, final_mood, content])
        with open("entries.txt", "a") as file:
            file.write(joined + "\n")
                  

        
    elif selection == "2": # section for viewing entries
        with open("entries.txt") as file:
            found_entry = False
            for line in file:
                new_entry = Entry.from_line(line)
                new_entry.view()
                print("")
                found_entry = True
        if found_entry == False:
            print("No entries found")
    elif selection == "3": # section for searching by keyword
        kw = input("Enter keyword:  ").lower()
        if kw == "":
            print("Cannot search using a blank keyword")
            continue
        with open("entries.txt") as file:
            flag = False
            for line in file:
                new_entry = Entry.from_line(line)
                if kw in new_entry.title.lower() or kw in new_entry.mood.lower() or kw in new_entry.content.lower():
                    flag = True
                    new_entry.view()
                    print("") #this is to make sure the next print wont be hugging the bottom of this one
        if flag == False:
            print("Keyword not found.")
    elif selection == "4": #section for running analysis 
        print(f"Total Word Count = {word_count()}. Longest Entry = {longest_line()}.")
    elif selection == "5": #section to end program
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

