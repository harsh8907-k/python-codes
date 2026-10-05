a=str(input("Enter a comment: "))

if "money" in a or "buy now" in a or "subscribe this" in a or "click this" in a:
    print("This is a spam comment")
else:
    print("This is not a spam comment")