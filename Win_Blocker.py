
import os
import shutil
import re



os.system('cls')
patt = re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9-_]{0,61}[a-zA-Z0-9]{0,1}\.([a-zA-Z]{1,6}|[a-zA-Z0-9-]{1,30}\.[a-zA-Z]{2,3})$')
hostsFile = 'C:\Windows\System32\drivers\etc\hosts' #remember to add drive letter change logic
#and add some colorama





def blocker(website): #function to block website
    website2 = ''
    if website.startswith('www.'):
        website2 = website[4::]
    else:
        website2 = 'www.' + website

    with open(hostsFile, mode='a') as file: #append the text to hosts file to block
        file.write(f'127.0.0.1  {website}')
        file.write('\n')
        file.write(f'127.0.0.1  {website2}')
        file.write('\n')
    print('WEBSITE BLOCKED!')



def unblocker(website):  #function to unblock website
    flag = ''
    with open(hostsFile) as file:   #check if the website is already blocked
        for line in file:   #skip comment lines
            if line.startswith('#'):
                continue
            else:                   
                if website in line:
                    if website.startswith('www.'):
                        website = website[4::]
                    with open(hostsFile) as oldhosts, open('hosts', 'w') as newhosts:   #make new hosts file without blocked website in the current directory
                        for line in oldhosts:                                       
                            if website not in line:
                                newhosts.write(line)
        
                    shutil.copyfile('hosts', hostsFile)
                    os.remove('hosts')
                    print('WEBSITE UNBLOCKED!')
                    flag = 'website found'
                    break
                    

    
    if flag != 'website found': #line with the website in it wasnt found in the file
        print('website is not blocked')
                    
                    
    
            

    



#for some ease
blockList = ['block', 'Block', 'BLOCK']
unblockList = ['unblock', 'Unblock', 'UNBLOCK']

while True:
    blockunblock = input('Do you want to block or unblock a previously blocked website? (type block or unblock): ')
    if blockunblock not in blockList and blockunblock not in unblockList:
        print('Don\'t mess around...(e.g. facebook.com)')
        continue
    else:
        break


#flagging for breaking or continuing sake of inner while loops
flag = ''
while True:
    if flag == 'n':
        break
    if flag == 'y':
        pass
    
    
    website = input('Enter the website name: ') #getting and validating website name
    valid = re.fullmatch(patt, website)
    if website == '':
        print('Please enter something')
        continue
    if not valid:
        print('Please enter a valid website')
        continue
    
    
    #using block and unblock functions
    if blockunblock in blockList:
        try:
            blocker(website)
        except PermissionError:
            print('Permission Denied - please run CMD as administrator for this to work')
            break

        while True: # logic for the case if user wants to block another address
            more = input('Do you want to block another website? (y/n): ')
            if more in ['n', 'N']:
                print('Thanks for using Windows Website Blocker!')
                flag = 'n'
                break
            elif more in ['y', 'Y']:
                flag = 'y'
                break
            else:
                print('enter y for yes or n for no')
                continue 
    
    else:
        try:
            unblocker(website)
        except PermissionError:
            print('Permission Denied - please run CMD as administrator for this to work')
            break
        
        while True: #its also obvious
            more = input('Do you want to unblock another website? (y/n): ')
            if more in ['n', 'N']:
                print('Thanks for using Windows Website Blocker!')
                flag = 'n'
                break
            elif more in ['y', 'Y']:
                flag = 'y'
                break
            else:
                print('enter y for yes or n for no')
                continue
        