# Gitproj
This is a project submission
1. Create a Repository in the Github.com with name Gitproj
![alt text](image-1.png)

2. Type the command on the local console  (Git bash) 
     nevkumar@NEVs-MacBook-Air Gitproj % git init
3. Type command to check the status 
    nevkumar@NEVs-MacBook-Air Gitproj % git status
4. Add the remote origin into local git 
    nevkumar@NEVs-MacBook-Air Gitproj % git branch
    * master
nevkumar@NEVs-MacBook-Air Gitproj % git fetch 
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 878 bytes | 175.00 KiB/s, done.
From https://github.com/nevrkumar4-spec/Gitproj
 * [new branch]      main       -> origin/main
nevkumar@NEVs-MacBook-Air Gitproj % git checkout main
branch 'main' set up to track 'origin/main'.
Switched to a new branch 'main'
nevkumar@NEVs-MacBook-Air Gitproj % git pull 
Already up to date.
nevkumar@NEVs-MacBook-Air Gitproj % ls
__pycache__	README.md	venv


5. Goto VSCode
   create a app.py under the dirctory workspace Gitproj
   steps to run the flask commands
    set envn  using the command
    >> python3 -m venv venv 
    >> source venv/bin/activate    
    Run the app.py with following command in terminal
    python3 app.py
![alt text](image-2.png)

![alt text](image-3.png)

Question 2 :Working with Changes & History

Add some new fucntion in the exiting app.py

@app.route("/query/<json_user_input>")
def query(json_user_input):
    if ( int(json_user_input) % 2 == 0):
        return f" The request variable is even "
    else:
        return f"The request variable is odd"
    
Run the file >>python3 app.py

Open the browser and type the url as http://127.0.0.1:5000/query/6
 out put should come as follows
 ![alt text](image-4.png)

Question 3: Branching & Feature Development

Type the command on the git =bash as 
>> git checkout -b featurebranch

Now modify the app.py with additional function for summ of two inout parameters

@app.route("/addition/<inputA>/<inputB>")    
def addition(inputA,inputB):
    return f"The sum of given input numbers are:{int(inputA)+int(inputB)}"
Run the command in Terminal
>> python3 app.py
Provide the input values as follows

https://127.0.0.1:5000/addition/2/3
 output will display on the browser as 
The sum of given input numbers are : 5