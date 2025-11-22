# Account management

## Overview
 This is a console 
based python 
application which 
allows users to sign 
up, log in, store 
notes, view 
registered accounts, 
and delete accounts – 
all in single runtime 
session. It stotes 
data temporarily.

## Features
 * Sign up  – Create a user account with username, age, gender and password validation
 * Log in   – Authenticate user with username and password
 * Notepad  – Store user’s note inside the system
 * Change password - Update password while logged in     
 * List accounts -  Display all registered users along with their info 
 * Delete account  - Remove an account using correct login credentials 
 * Exit     - Close the program

## How to run
* Ensure python 3.x is installed
* Run the script in terminal
* Follow the on-screen menu instructions

## Workflow
```
                          ┌────────────────────────┐
                          │   Start the Program    │
                          └───────────┬────────────┘
                                      │
                                      ▼
                      ┌─────────────────────────────────┐
                      │ Display Main Menu Options (1–5) │
                      └───────────┬─────────┬──────────┬─────────┬────────┐
                                  │         │          │         │        │
                                  ▼         ▼          ▼         ▼        ▼
                          ┌────────────┐ ┌─────────┐ ┌────────┐ ┌────────┐ ┌────────┐
                          │  Sign Up   │ │ Log In  │ │ List   │ │ Delete │ │  Exit  │
                          └─────┬──────┘ └───┬─────┘ │Accounts│ │Account │ └───┬────┘
                                │            │       └───┬────┘ └──┬─────┘     │
                                ▼            ▼           │         │           ▼
              ┌─────────────────────────┐ ┌─────────────────────┐  │     ┌────────────┐
              │ Enter user details &    │ │ Enter username &    │  │     │  Thank You │
              │ validate (age, gender)  │ │ password to login   │  │     └────────────┘
              └────────┬────────────────┘ └───┬────────────────┘   │
                       │                      │ Correct?           │
                  ________ Correct?           │ ________           │
                 │ Yes   │ No                 │Yes      │ No       │
                 ▼       ▼                    ▼         ▼          ▼
     ┌────────────────┐ ┌──────────────┐ ┌──────────────────┐ ┌─────────────┐
     │ Create account │ │ Show error & │ │ Login successful │ │ Show error  │
     │ successfully   │ │ repeat input │ │ (User Menu)      │ │ message     │
     └───────┬────────┘ └───────┬──────┘ └─────────┬────────┘ └──────┬──────┘
             │                  │                  │                 │
             │                  │                  ▼                 │
             │                  │      ┌────────────────────────┐    │
             │                  │      │ Show User Login Menu   │    │
             │                  │      │ 1. Notepad             │    │
             │                  │      │ 2. Change Password     │    │
             │                  │      │ 3. Logout              │    │
             │                  │      └──────────┬─────────────┘    │
             │                  │                 │                  │
             │                  │                 ▼                  │
             │                  │    ┌─────────────────────────┐     │
             │                  │    │ Perform selected action │     │
             │                  │    └──────────┬──────────────┘     │
             │                  │               │                    │
             │                  └───────────────┴───────────────► Back to Main Menu
             │
             └──────────────────────────────► Back to Main Menu
```
## Screenshot
<img width="374" height="384" alt="Screenshot 2025-11-18 222600" src="https://github.com/user-attachments/assets/4fae4a50-2654-4ae7-b48d-b22e00ccf30f" />

<img width="406" height="488" alt="Screenshot 2025-11-18 222621" src="https://github.com/user-attachments/assets/ba4286ed-2fb2-4775-b462-9c806efcb1e4" />

<img width="353" height="375" alt="Screenshot 2025-11-18 222513" src="https://github.com/user-attachments/assets/e2acffa5-ccdc-4bd6-8325-a16c9f613f24" />
