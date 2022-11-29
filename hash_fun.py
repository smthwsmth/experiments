def remove_marks(text, marks):
    for i in marks:
        text = text.replace(i, '')
    remove_marks.count += 1
    return text

remove_marks.__dict__.setdefault('count', 0)

text = 'Hi! Will we go together?'

print(remove_marks.count)
print(remove_marks(text, '!?'))
print(remove_marks.count)