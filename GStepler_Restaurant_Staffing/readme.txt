README - restaurant_staffing.py

Loading data:
- To load data into the program, open the top left file menu and select "Load".
- This will load .json data from a specified file pointer, defined in the load_employees() function.
- Data is read from the .json list of dictionaries, and each dictionary is converted into an Employee object.
- Defaults to employees.json

Saving data:
- To save data from the program to a .json file, open the top left file menu and select "Save All".
- This will save the data currently held in memory to a specified file pointer, defined in the save_info() function.
- Defaults to employees.json

Listbox:
- The listbox includes all imported/added/edited candidates.
- It can be navigated using the scroll wheel.
- Candidates can be selected by double-left-clicking (double-button-1)

Switching modes:
- There are two modes for the program: Edit/Add/Delete (Employee Management) Mode and Interview Rating mode.
- Switch between the two via the Mode menu.

Employee Management Mode:
- Allows you to add, edit, and delete employees/candidates from memory.
- Add candidates by entering information into the fields below the listbox, then clicking "Add" button.
- Edit candidates by double clicking the candidate in the listbox, editing information in the fields below,
  then clicking "Save" button.
- Delete candidates by double clicking the candidate in the listbox, then clicking "Delete" button.
- The program will automatically switch between add/edit/delete 'modes' based on your selections.

Interview Rating Mode:
- Allows you to rate a candidate's performance in interviews based on 4 questions.
- Double click a candidate in order to proceed with rating their performance. You can double click
  a different candidate at any time before clicking "Hire" or "Save"
- Click a radio button below the question to score the candidate.
- Clicking "Calculate Average" will calculate and display the average score for the candidate based on the
  current radio button selections.
        - If the average is above 3.8, a "Hire" option will appear. Clicking this will save the score and hire
          the candidate.
        - Otherwise, click "Rate" to save the average score for the candidate.