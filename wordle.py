import random
import logging

words = ("About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began",
         "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun",
         "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below",
         "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy",
         "After", "Anger", "Award", "Birth", "Again", "Angle", "Aware", "Black",
         "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind",
         "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood",
         "Album", "Arena", "Basis", "Board", "Boost", "Buyer", "China", "Cover",
         "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash",
         "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime",
         "Bread", "Cause", "Clean", "Cross", "Break", "Chain", "Clear", "Crowd",
         "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve",
         "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily",
         "Broke", "Check", "Coast", "Dance", "Brown", "Chest", "Could", "Dated",
         "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death",
         "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown",
         "Depth", "Error", "Forum", "Guard", "Doing", "Event", "Found", "Guess",
         "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide",
         "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry",
         "Drawn", "Faith", "Front", "Heart", "Dream", "False", "Fruit", "Heavy",
         "Dress", "Fault", "Fully", "Hence", "Drill", "Fiber", "Funny", "Night",
         "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel",
         "Drove", "Fifty", "Glass", "House", "Dying", "Fight", "Globe", "Human",
         "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image",
         "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner",
         "Elite", "Fleet", "Grant", "Input", "Empty", "Floor", "Grass", "Issue",
         "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice",
         "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly",
         "Known", "Local", "Might", "Noise", "Label", "Logic", "Minor", "North",
         "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel",
         "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur",
         "Layer", "Lying", "Month", "Ocean", "Learn", "Magic", "Moral", "Offer",
         "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order",
         "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought",
         "Level", "Match", "Movie", "Paint", "Light", "Mayor", "Needs", "Paper",
         "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round",
         "Panel", "Press", "Raise", "Route", "Phase", "Price", "Range", "Royal",
         "Phone", "Pride", "Rapid", "Rural", "Photo", "Prime", "Ratio", "Scale",
         "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope",
         "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense",
         "Plain", "Proud", "Rival", "Serve", "Plane", "Prove", "River", "Seven",
         "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape",
         "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp",
         "Sheet", "Spare", "Style", "Times", "Shelf", "Speak", "Sugar", "Tired",
         "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today",
         "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total",
         "Shoot", "Spoke", "Taken", "Touch", "Short", "Sport", "Taste", "Tough",
         "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track",
         "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat",
         "Sized", "State", "Thank", "Trend", "Skill", "Steam", "Theft", "Trial",
         "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries",
         "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly",
         "Smile", "Stone", "Thick", "Trust", "Smith", "Stood", "Thing", "Truth",
         "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under",
         "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union",
         "Sound", "Stuck", "Threw", "Unity", "South", "Study", "Throw", "Until",
         "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound",
         "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong",
         "Usual", "Train", "Wheel", "Wrote", "Valid", "World", "Where", "Yield",
         "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth",
         "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"
         )


def game():
    wordle = random.choice(words).lower()
    
    #letters as a variable for letters you have used that are in the word
    letters = []
    user_input = input("Try and guess the 5 letter word: ").lower()
    place_holder = ["_", "_", "_", "_", "_"]
    if user_input == wordle:
        print(f"Congrats you got it on your first try, today's wordle is '{wordle}'")
    else:
        for i in range(5):
            if user_input[i] == wordle[i]:
                place_holder[i] = user_input[i]
            else:
                for char in user_input:
                    if char in wordle and char not in place_holder:
                        letters.append(char)
    
        print(place_holder)
        print(set(letters))
                
        #check for which letters where right
        for attempt in range(4):
            new_attempt = input(f"The last guess was incorrect, please try again {attempt+2}/5: ").lower()
            if new_attempt == wordle:
                print(f"Congrats on winning today's wordle! Your guess was correct today's word is '{wordle}'")
                break
            else:
                for i in range(5):
                    if new_attempt[i] == wordle[i]:
                        place_holder[i] = new_attempt[i]
            print(place_holder)
            print(set(letters))
    if new_attempt != wordle:
        print(f"Today's wordle was '{wordle}'. Try again tomorrow :)")
            
game()
