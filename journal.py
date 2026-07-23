import datetime

class Entry: #this is building the blueprint for the entry object to be used to create new entries
    def __init__(self, content, title = None, mood = None):
        self.date = datetime.datetime.now()
        self.title = title
        self.mood = mood
        self.content = content

    def view(self): #blueprint to extract previous entries 
        print(self.date)
        if self.title != None:
            print(self.title)
        if self.mood != None:
            print(self.mood)
        print(self.content)

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
        joined = "_|_".join([final_title, final_mood, content])
        with open("entries.txt", "a") as file:
            file.write(joined + "\n")
                  

        
    elif selection == "2": # section for viewing entries
        with open("entries.txt") as file:
            found_entry = False
            for line in file:
                print(line)
                found_entry = True
        if found_entry == False:
            print("No entries found")
    elif selection == "3": # section for searching by keyword
        kw = input("Enter keyword:  ").lower()
        with open("entries.txt") as file:
            flag = False
            for line in file:
                if kw in line.lower():
                    flag = True
                    print(line)
        if flag == False:
                print("Keyword not found.")
    elif selection == "4": #section for running analysis 
        print(f"Total Word Count = {word_count()}. Longest Entry = {longest_line()}.")
    elif selection == "5": #section to end program
        print("Quitting Program")
        break
    else:
        print("Invalid Entry.")

