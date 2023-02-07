def translate(word,data):
    # converts to lower case
    w = word
    w = w.lower()
  
    if w in data:
        return data[w]
    # for getting close matches of word
    elif len(get_close_matches(w, data.keys())) > 0:             
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."