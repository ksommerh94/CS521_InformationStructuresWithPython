'''
Karen Sommer

CS 521 Spring 2021

Assignment 7

String slicing problems

BASED ON PROF. PINSKYs CODE MADE IN CLASS
'''



x = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

x_list = x.split("\n")

# this inserts an extra newline after last line
def print_file_list(x_list, line, pos, sep="^"):
    for index, sentence in enumerate(x_list):
        if index != line:
            print(sentence)
        else:
            new_sentence=sentence[:pos] + sep + sentence[pos:]
            print(new_sentence)
    print("----------------")
    return

#-----------------------------------------------------------------------------------------
#                            10 as specified in the document
#-----------------------------------------------------------------------------------------

def cmd_h(x, line, pos): # move cursor to the left
    if pos > 0:
        pos = pos - 1
    elif line > 0:
        line = line - 1
        sentence = x[line]
        pos = len(sentence)
    return x, line, pos

def cmd_l(x, line, pos): # move right one position
    current_sentence = x[line]
    if pos < len(current_sentence):
        pos = pos + 1
    elif line < len(x) - 1:
        line = line + 1
        pos = 0
    return x, line, pos

def cmd_j(x, line, pos):    # move up vertically one line
    if line > 0:
        previous_sentence = x[line - 1]
        if pos < len(previous_sentence):
            line = line -1
        else:
            line = line - 1
            pos = len(previous_sentence)
    return x, line, pos

def cmd_k(x, line, pos):    # move down vertically one line
    if line < len(x) - 1:
        next_sentence = x[line + 1]
        if pos < len(next_sentence):
            line = line + 1
        else:
            line = line + 1
            pos = len(next_sentence)
    return x, line, pos

def cmd_X(x, line, pos):     # delete character to left
    if pos > 0:
        sentence = x[line]
        new_sentence = sentence[: pos -1] + sentence[ pos : ]
        x[line] = new_sentence
        pos = pos -1
    return x, line , pos

def cmd_D(x, line, pos):   # remove from cursor to end of current line
    if (pos==0):
        x.pop(line)
    else:
        current_sentence = x[line]
        new_sentence = current_sentence[ : pos]
        x[line] = new_sentence
    return x, line, pos

def cmd_dd(x, line, pos):  # delete current line, move to start of next line, only if have next line
    if line < len(x) - 1:
        x.pop(line)
        pos = 0
    return x, line, pos

def cmd_ddp(x, line, pos):     # transpose two adjacent line
    if line < len(x) - 1:
        current_sentence = x[line]
        next_sentence = x[line + 1]
        x[line] = next_sentence
        x[line + 1] = current_sentence
        line = line + 1
    return x, line, pos

def cmd_n(x, line, pos, target):    # find first occurence of target after cursor
    for next_line, next_sentence in enumerate(x):
        if next_line>=line:
            target_position = next_sentence.find(target)
            if target_position >= 0:
                line = next_line
                pos=target_position
                break
    return x, line, pos

def cmd_wq(x, file_name): #write your representation as text file and save it
    f = open(file_name, "a")
    f.truncate(0)
    str=''.join(x)
    f.writelines(str.replace('.', '.\n'))
    f.close()
    print('Save!')

#-----------------------------------------------------------------------------------------
#                            10 made by my own
#-----------------------------------------------------------------------------------------


def cmd_x(x, line, pos):     # delete character to right
    if pos< len(x[line]):
        sentence = x[line]
        new_sentence = sentence[: pos] + sentence[ pos+1 : ]
        x[line] = new_sentence
        #pos = pos+1
    return x, line , pos

def cmd_DollarSign(x, line, pos):# Go to end of line
    pos=len(x[line])
    return x, line , pos

def cmd_a(x, line, pos, target):# append target after cursor
    sentence = x[line]
    new_sentence = sentence[:pos] + target + sentence[pos : ]
    x[line] = new_sentence
    return x, line, pos

def cmd_r(x, line, pos, target): # replace character at cursor
    if pos< len(x[line]):
        sentence=x[line]
        new_sentence=sentence[:pos]+target+sentence[pos+1:]
        x[line]=new_sentence
    return x, line, pos

def cmd_C(x, line, pos, change): #Change rest of line
    current_sentence = x[line]
    new_sentence = current_sentence[ : pos] + change
    x[line] = new_sentence
    return x, line, pos

def cmd_i(x, line, pos, target): # append target before cursor
    sentence = x[line]
    if pos>0:
        new_sentence = sentence[:pos] + target + sentence[pos+1 : ]
        x[line] = new_sentence
        pos+= len(target)
    else:
        new_sentence = target + sentence[pos: ]
        x[line] = new_sentence
        pos+= len(target)
    return x, line, pos

def cmd_I(x, line, pos, target): #Insert text at start of line
    sentence = x[line]
    new_sentence = target + sentence
    x[line] = new_sentence
    pos+= len(target)
    return x, line, pos

def cmd_A(x, line, pos, target): #Append text at end of line
    sentence = x[line]
    new_sentence =sentence + target
    x[line] = new_sentence
    return x, line, pos

def cmd_0(x, line, pos):#Move to start of line (zero)
    pos=0
    return x, line , pos

def cmd_H(x, line, pos):#Move to first  line on screen
    line=0
    pos=0
    return x, line , pos


line_id =1 ; delta = 2

print_file_list(x_list, line_id, delta)

print('cmd_H:')
x_list, line_id, delta = cmd_H(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)



#-----------------------------------------------------------------------------------------
#                                       PRINTS FOR TESTING
#-----------------------------------------------------------------------------------------





print('10 as specified in the document')

print('cmd_h:')
x_list, line_id, delta = cmd_h(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_l:')
x_list, line_id, delta = cmd_l(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_j:')
x_list, line_id, delta = cmd_j(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_k:')
x_list, line_id, delta = cmd_k(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_X:')
x_list, line_id, delta = cmd_X(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_D:')
x_list, line_id, delta = cmd_D(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_dd:')
x_list, line_id, delta = cmd_dd(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_ddp:')
x_list, line_id, delta = cmd_ddp(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_n:')
x_list, line_id, delta = cmd_n(x_list, line_id, delta, "better")
print_file_list(x_list, line_id, delta)

print('cmd_wq:')
cmd_wq(x_list,"wq_hw7.txt")

print('10 made by my own')

print('cmd_x:')
x_list, line_id, delta = cmd_x(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_DollarSign:')
x_list, line_id, delta = cmd_DollarSign(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_a:')
x_list, line_id, delta = cmd_a(x_list, line_id, delta,'TEST')
print_file_list(x_list, line_id, delta)

print('cmd_r:')
x_list, line_id, delta = cmd_r(x_list, line_id, delta,'T')
print_file_list(x_list, line_id, delta)

print('cmd_C:')
x_list, line_id, delta = cmd_C(x_list, line_id, delta,'ADD NEW TEXT')
print_file_list(x_list, line_id, delta)

print('cmd_i:')
x_list, line_id, delta = cmd_i(x_list, line_id, delta,'NEW')
print_file_list(x_list, line_id, delta)

print('cmd_I:')
x_list, line_id, delta = cmd_I(x_list, line_id, delta,'START ')
print_file_list(x_list, line_id, delta)

print('cmd_A:')
x_list, line_id, delta = cmd_A(x_list, line_id, delta,' END')
print_file_list(x_list, line_id, delta)

print('cmd_0:')
x_list, line_id, delta = cmd_0(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)

print('cmd_H:')
x_list, line_id, delta = cmd_H(x_list, line_id, delta)
print_file_list(x_list, line_id, delta)
