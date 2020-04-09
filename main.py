import tkinter as tk
import dicts
import search_functs
key = 'aa'
allowed = False


def show_info(info):
    global l1
    global l2
    global l3
    global l4
    global l5
    global l6
    global l7
    fname = info['name']
    lname = info['LName']
    space = ' '
    full_name = str(fname + space + lname)
    l1.destroy()
    l1 = tk.Label(master, text=full_name)
    l1.grid(row=6, column=2)

    l2.destroy()
    l2 = tk.Label(master, text=info['Social'])
    l2.grid(row=7, column=2)

    l3.destroy()
    l3 = tk.Label(master, text=info['AddressL1'])
    l3.grid(row=8, column=2)

    l4.destroy()
    l4 = tk.Label(master, text=info['AddressL2'])
    l4.grid(row=9, column=2)

    l5.destroy()
    l5 = tk.Label(master, text=info['Zip'])
    l5.grid(row=10, column=2)

    l6.destroy()
    l6 = tk.Label(master, text=info['City'])
    l6.grid(row=11, column=2)

    l7.destroy()
    l7 = tk.Label(master, text=info['State'])
    l7.grid(row=12, column=2)





def test_code(code):


    if code == key:
        print('yes')
    else:
        print('no')


def retrieve_input():
    inputs = a1.get()
    global allowed

    if inputs == key:
        allowed = True
        test.destroy()
    else:
        allowed = False

def search_social():
    inputs = e3.get()

    search = search_functs.get_by_social(dicts.Voters, inputs)
    id_number = search[0]

    return_voter_info(id_number)

def return_voter_info(voter_id):




    voter = str(voter_id)
    get_info = dicts.Voters.get(voter)




    show_info(get_info)







test = tk.Tk()


test.geometry('250x75')
tk.Label(test, text='Encryption Key:').grid(row=1)
a1 = tk.Entry(test)
a1.grid(row=1, column=1)
tk.Button(test,
          text="Enter",
          command = lambda: retrieve_input()).grid(row=3,
                                     column=1,
                                     sticky=tk.W,
                                     pady=4)
test.mainloop()
print(allowed)
if allowed == True:
    master = tk.Tk()
    master.geometry('800x600')
    master.title('Voter Registry')
    name = '                                            '
    l1 = tk.Label(master, text='')
    l2 = tk.Label(master, text='')
    l3 = tk.Label(master, text='')
    l4 = tk.Label(master, text='')
    l5 = tk.Label(master, text='')
    l6 = tk.Label(master, text='')
    l7 = tk.Label(master, text='')



    tk.Label(master, text="Social Security #").grid(row=1)
    tk.Label(master, text='ID #             ').grid(row=2)
    tk.Label(master, text="Name     ").grid(row=6)
    tk.Label(master, text="Social   ").grid(row=7)
    tk.Label(master, text="Address  ").grid(row=8)
    tk.Label(master, text="Add Line 2").grid(row=9)
    tk.Label(master, text="Zip Code ").grid(row=10)
    tk.Label(master, text="City     ").grid(row=11)
    tk.Label(master, text="State    ").grid(row=12)



    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)





    e3.grid(row=1, column=1)
    e4.grid(row=2, column=1)


    tk.Button(master,
            text="Search Soc",
            command=lambda: search_social()).grid(row=5,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
    tk.Button(master,
              text="Quit",
              command=master.quit).grid(row=5,
                                        column=5,
                                        sticky=tk.W,
                                        pady=4)



    master.mainloop()








