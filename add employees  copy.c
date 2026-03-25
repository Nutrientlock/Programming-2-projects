//Author: Ajay Clarke 
// Date: N/A 
// Description: Group Project (Add Employee)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// struct to receive Employee data
typedef struct{
    char Employee_ID [10];
    char First_name [40];
    char Last_name [40];
    char Role [40];
    char Status [40];
} employee;

// Open File 
FILE *open_file();

// Close File
void close_file(FILE *file);

// function to appeand of create a new file
void Clean_file(employee *emp);

// Function to add Employee
void Add_Employee(employee *emp);

// Validate the uniqueness of ID number
int valid_id(char *idPtr);

// validate employee status
int Valid_status(char *status); 

// validate employee role
int Valid_role(char *role);

// list Employees
void list_emplyees(employee *emp);

// Find Employee
void find_employee(employee *emp);

// Update Employee
void update_employee(employee *emp);


int main(){
    employee emp;
    employee *empPtr = &emp;

    FILE *file = open_file(empPtr);
    if (file == NULL) return 1;
    list_emplyees(empPtr);
    close_file(file);
    find_employee(empPtr);
    update_employee(empPtr);

    return 0;
}

FILE *open_file(){
    FILE *file;
    file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "a");
    if (file == NULL){
        printf("File failed to open");
        return NULL;
    }
    else {
        printf("file open successful\n");
        return file;
    }
}

void close_file(FILE* file){
    fclose(file);
}

// function to appeand of create a new file
void Clean_file(employee *emp){
    int clean_file;

    printf("Do you want a clean Document 1 for no and 0 for yes: ");
    scanf("%d", &clean_file);

    if (clean_file == 0){
        FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "w"); 
        fclose(file);
        Add_Employee(emp);
    }
    else if (clean_file == 1){
        Add_Employee(emp);
    }
    else {
        printf("Invalid Input");
    }
}

// Validate the uniqueness of ID number
int valid_id(char *idPtr) {
    char line[200];
    char existingID[10];

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    if (file == NULL) {
        return 0; 
    }

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,]", existingID); 
        if (strcmp(existingID, idPtr) == 0) {
            fclose(file);
            return 1; 
        }
    }

    fclose(file);
    return 0;
}

// validate employee status
int Valid_status(char *Status){
    int i = 0;
    while (Status[i] != '\0'){
        Status[i] = toupper(Status[i]);
        i += 1;
    }
    if (strcmp(Status, "ACTIVE") == 0)     return 1;
    if (strcmp(Status, "LEAVE") == 0)      return 1;
    if (strcmp(Status, "TERMINATED") == 0) return 1;

    printf("Invalid Input");
    return 0;
}

// validate employee role
int Valid_role(char *role){
    int i = 0;
    char temp[40];
    strncpy(temp, role, sizeof(temp));
    temp[sizeof(temp) - 1] = '\0';

    while (temp[i] != '\0'){
        temp[i] = toupper(temp[i]);
        i++;
    }

    if (strcmp(temp, "MANAGER") == 0)    return 1;
    if (strcmp(temp, "DEVELOPER") == 0)  return 1;
    if (strcmp(temp, "ANALYST") == 0)    return 1;
    if (strcmp(temp, "HR") == 0)         return 1;
    if (strcmp(temp, "ADMIN") == 0)      return 1;
    if (strcmp(temp, "ENGINEER") == 0)   return 1;
    if (strcmp(temp, "INTERN") == 0)     return 1;

    printf("Invalid Role");
    return 0;
}

// Function to add Employee
void Add_Employee(employee *emp) {
    int starter = 0;

    do {
        printf("Press 1 Add Employee or -999 to stop: ");
        scanf("%d", &starter);
        if (starter > 1 || starter <= 0){
            break;
        }

        printf("Enter Employee ID,\nmust be 10 characters: ");
        scanf("%s", emp->Employee_ID);

        if (strlen(emp->Employee_ID) <= 10){

            if (valid_id(emp->Employee_ID) == 1) { 
                printf("Error: ID already exists. Try a different ID.\n");
                continue; 
            }

            printf("Enter Employee First name: ");
            scanf("%s", emp->First_name);

            printf("Enter Employee Last name: ");
            scanf("%s", emp->Last_name);

            do {
                printf("Enter Employee Role (Manager, Developer, Analyst, HR, Admin, Engineer, Intern): ");
                scanf("%s", emp->Role);
                if (Valid_role(emp->Role) == 0){
                    printf("\nError: Invalid Role.\n");
                }
            }
            while(Valid_role(emp->Role) == 0);

            do {
                printf("Enter Employee Status (Active, Leave, Terminated): ");
                scanf("%s", emp->Status);
                if (Valid_status(emp->Status) == 0){
                    printf("\nError: Invalid Status. Must be Active, On Leave, or Terminated: \n");
                }
            }
            while(Valid_status(emp->Status) == 0);

            FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "a"); 
            if (file == NULL) {
                printf("File Failed to open\n");
                return; 
            }

            fprintf(file, "%s,%s,%s,%s,%s\n",  
                emp->Employee_ID,
                emp->First_name,
                emp->Last_name,
                emp->Role,
                emp->Status
            );

            fclose(file);
            printf("Employee added successfully.\n");

        }
        else {
            printf("ID Number is Invalid");
        }
    } while(starter != -999 || starter < 2);
}


void list_emplyees(employee *emp){
    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    char line[200];

    if (file == NULL) {
        printf("Error: Employee file not found.\n");
        return;
    }

    fseek(file, 0, SEEK_END);
    long int size = ftell(file);

    if (size == 0) {
        printf("No employees found. File is empty.\n");
        fclose(file);
        return;
    }

    rewind(file);

    printf("\n%-10s %-20s %-20s %-15s\n", "ID", "Full Name", "Role", "Status");
    printf("--------------------------------------------------------------\n");

    while (fgets(line, sizeof(line), file) != NULL) {
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^\n]",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status);

        char Full_name[80];
        snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

        printf("%-10s %-20s %-20s %-15s\n",
            emp->Employee_ID,
            Full_name,
            emp->Role,
            emp->Status);
    }

    printf("--------------------------------------------------------------\n");
    fclose(file);
}


// find_employee
void find_employee(employee *emp){
    char line[200];
    char ID_search[10];
    int found = 0;

    printf("Enter the ID number of the person you wish to find: ");
    scanf("%s", ID_search);

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    if (file == NULL){
        printf("Error: Employee file not found.\n");
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^\n]",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status);

        if (strcmp(emp->Employee_ID, ID_search) == 0){
            found = 1;

            printf("\n%-10s %-20s %-20s %-15s\n", "ID", "Full Name", "Role", "Status");
            printf("--------------------------------------------------------------\n");

            char Full_name[80];
            snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

            printf("%-10s %-20s %-20s %-15s\n",
                emp->Employee_ID, Full_name, emp->Role, emp->Status);

            printf("--------------------------------------------------------------\n");
            break;
        }
    }

    if (found == 0){
        printf("Employee not found.\n");
    }

    fclose(file);
}


// update_employee
void update_employee(employee *emp){
    char line[200];
    char ID_search[10];
    int found = 0;
    int choice;

    printf("Enter the ID of the employee to update: ");
    scanf("%s", ID_search);

    FILE *file = fopen("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv", "r");
    if (file == NULL){
        printf("Error: Employee file not found.\n");
        return;
    }

    FILE *temp = fopen("C:\\Users\\ajayc\\Desktop\\P2\\temp.csv", "w");
    if (temp == NULL){
        printf("Error: Could not create temp file.\n");
        fclose(file);
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^\n]",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status);

        if (strcmp(emp->Employee_ID, ID_search) == 0){
            found = 1;

            printf("Employee found: %s %s | Role: %s | Status: %s\n",
                emp->First_name, emp->Last_name, emp->Role, emp->Status);
            printf("What would you like to update?\n");
            printf("1. Role\n2. Status\n3. Both\n");
            printf("Enter choice: ");
            scanf("%d", &choice);

            if (choice == 1 || choice == 3){
                do {
                    printf("Enter new Role (Manager, Developer, Analyst, HR, Admin, Engineer, Intern): ");
                    scanf("%s", emp->Role);
                    if (Valid_role(emp->Role) == 0){
                        printf("\nError: Invalid Role. Try again.\n");
                    }
                } while (Valid_role(emp->Role) == 0);
            }

            if (choice == 2 || choice == 3){
                do {
                    printf("Enter new Status (Active, Leave, Terminated): ");
                    scanf("%s", emp->Status);
                    if (Valid_status(emp->Status) == 0){
                        printf("\nError: Invalid Status. Try again.\n");
                    }
                } while (Valid_status(emp->Status) == 0);
            }
        }

        fprintf(temp, "%s,%s,%s,%s,%s\n",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status);
    }

    fclose(file);
    fclose(temp);

    if (found == 0){
        printf("Employee not found.\n");
        remove("C:\\Users\\ajayc\\Desktop\\P2\\temp.csv");
        return;
    }

    remove("C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv");
    rename("C:\\Users\\ajayc\\Desktop\\P2\\temp.csv",
           "C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv");

    printf("Employee updated successfully.\n");
}