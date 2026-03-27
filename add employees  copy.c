//Author: Ajay Clarke 
// Date: N/A 
// Description: Group Project (Add Employee)

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define CSV_file "C:\\Users\\ajayc\\Desktop\\P2\\employee_records.csv"

// struct to receive Employee data
struct employee {
    char Employee_ID [10];
    char First_name  [40];
    char Last_name   [40];
    char Role        [40];
    char Status      [40];
    int  Hourly_rate;
};
struct employee emp;

// Forward declarations
FILE *open_file();
void  close_file(FILE *file);
void  Clean_file(struct employee *emp);
void  Add_Employee(struct employee *emp);
int   valid_id(char *idPtr);
int   Valid_status(char *status);
int   Valid_role(char *role);
void  list_emplyees(struct employee *emp);
void  find_employee(struct employee *emp);
void  Update_Record(struct employee *emp);


int main(){
    struct employee *empPtr = &emp;

    FILE *file = open_file();
    if (file == NULL) return 1;

    list_emplyees(empPtr);
    close_file(file);
    find_employee(empPtr);
    Update_Record(empPtr);

    return 0;
}


FILE *open_file(){
    FILE *file = fopen(CSV_file, "a");
    if (file == NULL){
        printf("File failed to open\n");
        return NULL;
    }
    printf("File open successful\n");
    Clean_file(&emp);
    return file;
}


void close_file(FILE *file){
    fclose(file);
}


void Clean_file(struct employee *emp){
    int clean_file;

    printf("Do you want a clean Document? 1 for no, 0 for yes: ");
    scanf("%d", &clean_file);

    if (clean_file == 0){
        FILE *file = fopen(CSV_file, "w");
        fclose(file);
        Add_Employee(emp);
    }
    else if (clean_file == 1){
        Add_Employee(emp);
    }
    else {
        printf("Invalid Input\n");
    }
}


int valid_id(char *idPtr){
    char existingID[10];
    char line[200];

    // FIX 1: was hardcoded string, now uses CSV_file macro
    FILE *file = fopen(CSV_file, "r");
    if (file == NULL) return 0;

    while (fgets(line, sizeof(line), file) != NULL){
        sscanf(line, "%[^,]", existingID);
        if (strcmp(existingID, idPtr) == 0){
            fclose(file);
            return 1;
        }
    }

    fclose(file);
    return 0;
}


int Valid_status(char *Status){
    int i = 0;
    while (Status[i] != '\0'){
        Status[i] = toupper(Status[i]);
        i++;
    }
    if (strcmp(Status, "ACTIVE")     == 0) return 1;
    if (strcmp(Status, "LEAVE")      == 0) return 1;
    if (strcmp(Status, "TERMINATED") == 0) return 1;

    printf("Invalid Status\n");
    return 0;
}


int Valid_role(char *role){
    // FIX 2: old code read uninitialized temp[] until '\n' — crash waiting to happen
    // correct approach: copy role into temp safely, then uppercase it
    char temp[40];
    int i = 0;

    strncpy(temp, role, sizeof(temp) - 1);
    temp[sizeof(temp) - 1] = '\0';

    while (temp[i] != '\0'){
        temp[i] = toupper(temp[i]);
        i++;
    }

    if (strcmp(temp, "MANAGER")   == 0) return 1;
    if (strcmp(temp, "DEVELOPER") == 0) return 1;
    if (strcmp(temp, "ANALYST")   == 0) return 1;
    if (strcmp(temp, "HR")        == 0) return 1;
    if (strcmp(temp, "ADMIN")     == 0) return 1;
    if (strcmp(temp, "ENGINEER")  == 0) return 1;
    if (strcmp(temp, "INTERN")    == 0) return 1;

    printf("Invalid Role\n");
    return 0;
}


void Add_Employee(struct employee *emp){
    int starter = 0;

    do {
        printf("Press 1 to Add Employee or -999 to stop: ");
        scanf("%d", &starter);

        if (starter > 1 || starter <= 0) break;

        printf("Enter Employee ID (max 9 characters): ");
        scanf("%s", emp->Employee_ID);

        if (strlen(emp->Employee_ID) <= 10){

            if (valid_id(emp->Employee_ID) == 1){
                printf("Error: ID already exists. Try a different ID.\n");
                continue;
            }

            printf("Enter Employee First name: ");
            scanf("%s", emp->First_name);

            printf("Enter Employee Last name: ");
            scanf("%s", emp->Last_name);

            // FIX 3: was "while(Valid_role != 1)" — missing () and argument
            // Valid_role is a function, you must call it: Valid_role(emp->Role)
            do {
                printf("Enter Role (Manager, Developer, Analyst, HR, Admin, Engineer, Intern): ");
                scanf("%s", emp->Role);
                if (Valid_role(emp->Role) == 0)
                    printf("Error: Invalid Role.\n");
            } while (Valid_role(emp->Role) == 0);

            do {
                printf("Enter Status (Active, Leave, Terminated): ");
                scanf("%s", emp->Status);
                if (Valid_status(emp->Status) == 0)
                    printf("Error: Invalid Status.\n");
            } while (Valid_status(emp->Status) == 0);

            printf("Enter employee Hourly rate: ");
            // FIX 4: was scanf("%d", emp->Hourly_rate) — missing & for address
            scanf("%d", &emp->Hourly_rate);

            // FIX 5: was fopen("CSV_file", "a") — CSV_file in quotes is a literal
            // string "CSV_file", not the macro. Remove the quotes to use the macro.
            FILE *file = fopen(CSV_file, "a");
            if (file == NULL){
                printf("File failed to open\n");
                return;
            }

            // FIX 6: Hourly_rate is an int so format specifier must be %d not %s
            fprintf(file, "%s,%s,%s,%s,%s,%d\n",
                emp->Employee_ID,
                emp->First_name,
                emp->Last_name,
                emp->Role,
                emp->Status,
                emp->Hourly_rate);

            fclose(file);
            printf("Employee added successfully.\n");

        } else {
            printf("ID is too long.\n");
        }

    } while (starter != -999);
}


void list_emplyees(struct employee *emp){
    char line[200];
    char Full_name[80];

    // FIX 7: was fopen("CSV_file") — macro must be used without quotes
    FILE *file = fopen(CSV_file, "r");
    if (file == NULL){
        printf("Error: Employee file not found.\n");
        return;
    }

    fseek(file, 0, SEEK_END);
    long int size = ftell(file);
    if (size == 0){
        printf("No employees found. File is empty.\n");
        fclose(file);
        return;
    }
    rewind(file);

    printf("\n%-10s %-20s %-20s %-15s %-15s\n",
        "ID", "Full Name", "Role", "Status", "Hourly Rate");
    printf("--------------------------------------------------------------\n");

    while (fgets(line, sizeof(line), file) != NULL){
        // FIX 8: Hourly_rate is int — must use %d not %[^\n]
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%d",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        // FIX 9: was using local First_name/Last_name which were never filled
        // must use emp->First_name and emp->Last_name
        snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

        // FIX 10: Hourly_rate is int — printf format must be %d not %s
        printf("%-10s %-20s %-20s %-15s %-15d\n",
            emp->Employee_ID,
            Full_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate);
    }

    printf("--------------------------------------------------------------\n");
    fclose(file);
}


void find_employee(struct employee *emp){
    char line[200];
    char ID_search[10];
    char Full_name[80];
    int found = 0;

    printf("Enter the ID number of the person you wish to find: ");
    scanf("%s", ID_search);

    // FIX 11: was fopen("CSV_file") — macro must be used without quotes
    FILE *file = fopen(CSV_file, "r");
    if (file == NULL){
        printf("Error: Employee file not found.\n");
        return;
    }

    while (fgets(line, sizeof(line), file) != NULL){
        // FIX 12: Hourly_rate needs %d
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%d",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        if (strcmp(emp->Employee_ID, ID_search) == 0){
            found = 1;

            printf("\n%-10s %-20s %-20s %-15s %-15s\n",
                "ID", "Full Name", "Role", "Status", "Hourly Rate");
            printf("--------------------------------------------------------------\n");

            snprintf(Full_name, sizeof(Full_name), "%s %s", emp->First_name, emp->Last_name);

            // FIX 13: Hourly_rate printf format must be %d not %s
            printf("%-10s %-20s %-20s %-15s %-15d\n",
                emp->Employee_ID,
                Full_name,
                emp->Role,
                emp->Status,
                emp->Hourly_rate);

            printf("--------------------------------------------------------------\n");
            break;
        }
    }

    if (found == 0) printf("Employee not found.\n");

    fclose(file);
}


void Update_Record(struct employee *emp){
    char line[200];
    char ID_search[10];
    int found = 0;
    int choice;

    printf("Enter the ID of the employee to update: ");
    scanf("%s", ID_search);

    // FIX 14: was fopen("CSV_file") — macro must be used without quotes
    FILE *file = fopen(CSV_file, "r");
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
        sscanf(line, "%[^,],%[^,],%[^,],%[^,],%[^,],%d",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            &emp->Hourly_rate);

        if (strcmp(emp->Employee_ID, ID_search) == 0){
            found = 1;

            printf("Found: %s %s | Role: %s | Status: %s | Rate: %d\n",
                emp->First_name, emp->Last_name,
                emp->Role, emp->Status, emp->Hourly_rate);

            printf("1. Update Role\n2. Update Status\n3. Update Both\n");
            printf("Enter choice: ");
            scanf("%d", &choice);

            if (choice == 1 || choice == 3){
                do {
                    printf("Enter new Role (Manager, Developer, Analyst, HR, Admin, Engineer, Intern): ");
                    scanf("%s", emp->Role);
                    if (Valid_role(emp->Role) == 0)
                        printf("Error: Invalid Role. Try again.\n");
                } while (Valid_role(emp->Role) == 0);
            }

            if (choice == 2 || choice == 3){
                do {
                    printf("Enter new Status (Active, Leave, Terminated): ");
                    scanf("%s", emp->Status);
                    if (Valid_status(emp->Status) == 0)
                        printf("Error: Invalid Status. Try again.\n");
                } while (Valid_status(emp->Status) == 0);
            }
        }

        fprintf(temp, "%s,%s,%s,%s,%s,%d\n",
            emp->Employee_ID,
            emp->First_name,
            emp->Last_name,
            emp->Role,
            emp->Status,
            emp->Hourly_rate);
    }

    fclose(file);
    fclose(temp);

    if (found == 0){
        printf("Employee not found.\n");
        remove("C:\\Users\\ajayc\\Desktop\\P2\\temp.csv");
        return;
    }

    remove(CSV_file);
    rename("C:\\Users\\ajayc\\Desktop\\P2\\temp.csv", CSV_file);
    printf("Employee updated successfully.\n");
}